import nl_core_news_lg
nlp = nl_core_news_lg.load()

def filter(string: str) -> str:
    doc = nlp(string)
    token_str = [token.text for token in doc if token.pos_ == 'NOUN' and token.has_vector and len(token.text) > 1]
    returnvalue = ' '.join(token_str)
    return returnvalue