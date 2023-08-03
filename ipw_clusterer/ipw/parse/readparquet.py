import logging
from tkinter.messagebox import QUESTION
import pandas as pd
import pyarrow.dataset as ds
from pathlib import Path
from ..enums import Question

PARQUET_SUFFIX = '.parquet'
path = None
screen_answer = None

def _parse(table_name: str) -> pd.DataFrame:
    parquet_path = path / f"{table_name}{PARQUET_SUFFIX}"
    table = ds.dataset(parquet_path).to_table()
    df = table.to_pandas()

    logging.info(f'Number of records in table {table_name}: {len(df)}')

    if 'case_id' in df.columns:
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

def get_answer(question):
    returnvalue = screen_answer[screen_answer['question_id'] == question.value]
    returnvalue = returnvalue.drop(['question_id', 'screen_id'], axis = 1)
    returnvalue = returnvalue.rename(columns = {'answer': str(question)})
    return returnvalue

def get_situation():
    situation1 = _parse('situation')
    situation1 = situation1.drop('situation_id', axis = 1)
    
    description = get_answer(Question.DESCRIPTION)
    future = get_answer(Question.FUTURE)
    solution = get_answer(Question.SOLUTION)
    situation2 = description.merge(solution, left_on = 'case_id', right_on = 'case_id', how = 'outer') 
    situation2 = situation2.merge(future, left_on = 'case_id', right_on = 'case_id', how = 'outer') 

    returnvalue = pd.concat([situation1, situation2]).drop_duplicates(subset='case_id', keep='last')
    return returnvalue

def get_plan():
    plan1 = _parse('plan')
    plan1 = plan1.drop(['plan_id', 'milestones'], axis = 1)
    
    plan2 = get_answer(Question.PERSPECTIVE)
    questions = [Question.BREAKTHROUGH, Question.EXCEPTION, Question.DO_SELF, Question.SUPPORT, Question.TREATMENT, Question.SCENARIOS]

    for question in questions:
        answers = get_answer(question)
        plan2 = plan2.merge(answers, left_on = 'case_id', right_on = 'case_id', how = 'outer') 

    returnvalue = pd.concat([plan1, plan2]).drop_duplicates(subset='case_id', keep='last')

    return returnvalue



def read(path_in: str) -> pd.DataFrame:
    global screen_answer
    global path
    path = Path(path_in)
    screen_answer = _parse('screen_answer').drop_duplicates()
    
    case = _parse('case')
    
    situation = get_situation()
    plan = get_plan()
    
    df_sit_pln = plan.merge(situation, left_on = 'case_id', right_on = 'case_id', how = 'outer', suffixes = ('_pln', '_sit'))
    df = df_sit_pln.merge(case, left_on = 'case_id', right_on = 'id', how = 'left')
    
    df.drop('case_id', axis = 1, inplace = True)

    to_drop = [
        'title',
        'collection_id',
        'author_id'
    ]
    df = df.drop(to_drop, axis = 1)
    df = df.set_index('id')

    return df