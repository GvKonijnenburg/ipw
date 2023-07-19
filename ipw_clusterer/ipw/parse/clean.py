import pandas as pd
from bs4 import BeautifulSoup

def _clean_string(string:str) -> str:
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
        df[column] = df[column].apply(_clean_string)
    return df