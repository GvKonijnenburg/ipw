from ..text.words_per_label import words_per_label
from .wordcloud import wordcloud

def model_wordclouds(df, model, run, h = 3, w = 3):
    label_dicts = words_per_label(df, model, run)

    n = max(label_dicts.keys())

    for label in range(n + 1):
        wordcloud(label_dicts[label], title = f'Cluster {label}', h = h, w = w)