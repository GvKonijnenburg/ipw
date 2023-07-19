from .add_word_count_to_dict import add_word_count_to_dict

def words_per_label(df, labels):
    n = labels.max() + 1
    returnvalue = {}

    for i, label in enumerate(labels):
        words = df.loc[df.index[i]]['text']

        if label in returnvalue:
            returnvalue[label] = add_word_count_to_dict(words, returnvalue[label])
        else:
            dict = {}
            returnvalue[label] = add_word_count_to_dict(words, dict)

    return returnvalue