import pandas as pd
import unicodedata
from bs4 import BeautifulSoup

def _clean_string(string:str) -> str:
    returnvalue = ''
    if string is not None and not isinstance(string, float):
        
        # parse html
        soup = BeautifulSoup(string, 'html.parser')
        returnvalue = soup.getText()
        
        # remove '\n'
        returnvalue = returnvalue.replace('\\n', '')

        # remove 'xxx'
        returnvalue = returnvalue.replace('xxx', '')

        # normalize the string
        returnvalue = unicodedata.normalize('NFKC', returnvalue)
    return returnvalue


def clean(df: pd.DataFrame) -> pd.DataFrame:
    for column in df.columns:  
        df[column] = df[column].apply(_clean_string)
    return df