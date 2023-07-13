import logging
import pandas as pd
import pyarrow.dataset as ds
from settings.constants import DATA_PATH
from models import Case
from pathlib import Path
from typing import List
from uuid import UUID

def _parse(table_name: str) -> pd.DataFrame:
    parquet_path = DATA_PATH / f'{table_name}.parquet'
    table = ds.dataset(parquet_path).to_table()
    df = table.to_pandas()

    logging.info(f'Number of records in table {table_name}: {len(df)}')

    if 'case_id' in df.columns:
        if not df['case_id'].is_unique:
            raise ValueError(f'Duplicate values found in "case_id" column in table {table_name}.')
        
        df.rename(columns = {'id': f'{table_name}_id'}, inplace = True)
   
    return df
    
def row_to_case(row: pd.Series) -> Case:  
    id = UUID(int=int.from_bytes(row['id'], 'little'))  
    case = Case(  
        id=id,  
        perspective=row['perspective'],  
        milestones=row['milestones'],  
        scenarios=row['scenarios'],  
        breakthrough=row['breakthrough'],  
        exception=row['exception'],  
        do_self=row['do_self'],  
        support=row['support'],  
        treatment=row['treatment'],  
        description=row['description'],  
        solution=row['solution'],  
        future=row['future']  
    )  
    return case  

def main() -> List[Case]:
    case = _parse('case')
    situation = _parse('situation')
    plan = _parse('plan')
    
    df_sit_pln = plan.merge(situation, left_on = 'case_id', right_on = 'case_id', how = 'outer', suffixes = ('_pln', '_sit'))
    df = df_sit_pln.merge(case, left_on = 'case_id', right_on = 'id', how = 'left')
    logging.info(f'Number of records in combined table: {len(df)}')
    df = df[df['status'] == 'closed']
    logging.info(f'Number of closed records in combined table: {len(df)}')
        
    returnvalue = []
    for index, row in df.iterrows():
        case = row_to_case(row)

        if case.norm != 0.0:
            returnvalue.append(case)
        
    return returnvalue