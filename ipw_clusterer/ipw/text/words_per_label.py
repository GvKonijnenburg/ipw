from itertools import count
from .add_word_count_to_dict import add_word_count_to_dict
from ..enums.model import Model

def words_per_label(df, model, run):
    label_column = model.col(run)

    returnvalue = {}

    for i in df.index:
        label = df.loc[i, label_column]
        words = df.loc[i, 'text']
        
        if label in returnvalue:
            returnvalue[label] = add_word_count_to_dict(words, returnvalue[label], count_all = False)
        else:
            returnvalue[label] = add_word_count_to_dict(words, {}, count_all = False)

    return returnvalue