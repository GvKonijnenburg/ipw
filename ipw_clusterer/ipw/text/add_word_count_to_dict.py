import re
import nl_core_news_lg
from typing import Dict

nlp = nl_core_news_lg.load()

def add_word_count_to_dict(string:str, returnvalue: Dict[str, int], count_all = True) -> Dict[str, int]:
    words = string.split()
    for word in words:
        key = re.sub(r'[^a-z]', '', word.lower())
        if key in returnvalue:
            if count_all:
                returnvalue[key] += 1
        else:
            returnvalue[key] = 1
    return returnvalue
