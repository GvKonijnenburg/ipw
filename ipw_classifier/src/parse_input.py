import logging
import pandas as pd
import pyarrow.dataset as ds
from bs4 import BeautifulSoup
from pathlib import Path

PARQUET_SUFFIX = '.parquet'

def _parse(path: Path, table_name: str) -> pd.DataFrame:
    parquet_path = path / f"{table_name}{PARQUET_SUFFIX}"
    table = ds.dataset(parquet_path).to_table()
    df = table.to_pandas()

    logging.info(f'Number of records in table {table_name}: {len(df)}')

    if 'case_id' in df.columns:
        if not df['case_id'].is_unique:
            raise ValueError(f'Duplicate values found in "case_id" column in table {table_name}.')
        
        df.rename(columns = {'id': f'{table_name}_id'}, inplace = True)
    
    columns_to_drop = set([
        'author',
        'rights', 
        'created',
        'updated',
        'deleted',
        'owners',
        'source',
        'closed'
        ])
    columns = columns_to_drop.intersection(set(df.columns))  
    
    for col_name in columns:
        df.drop(col_name, axis = 1, inplace = True)
    return df

def load(path_in: str) -> pd.DataFrame:
    path = Path(path_in)
    
    
    case = _parse(path, 'case')
    situation = _parse(path, 'situation')
    plan = _parse(path, 'plan')
    
    df_sit_pln = plan.merge(situation, left_on = 'case_id', right_on = 'case_id', how = 'outer', suffixes = ('_pln', '_sit'))
    df = df_sit_pln.merge(case, left_on = 'case_id', right_on = 'id', how = 'left')
    
    df.drop('case_id', axis = 1, inplace = True)

    to_drop = [
        'plan_id',
        'situation_id',
        'title',
        'collection_id',
        'author_id'
    ]
    df = df.drop(to_drop, axis = 1)
    df = df.set_index('id')

    return df

def clean_string(string:str) -> str:
    returnvalue = ''
    if string is not None and not isinstance(string, float):
        
        # parse html
        soup = BeautifulSoup(string, 'html.parser')
        returnvalue = soup.getText()
        
        # remove '\n'
        returnvalue = returnvalue.replace('\\n', '')
    return returnvalue


def clean(df: pd.DataFrame) -> pd.DataFrame:
    for column in df.columns:  
        df[column] = df[column].apply(clean_string)
    return df