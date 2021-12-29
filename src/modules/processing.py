import re
import string

import unidecode
import nltk
from nltk.corpus import stopwords


def preprocessing(text: str):
    text = text.lower()
    text = unidecode.unidecode(text)

    text = re.sub('\[.*?\]', '', text)

    text_without_url = re.sub('https?://\S+|www\.\S+', '', text)

    text_without_tag = re.sub('<.*?>+', '', text_without_url)

    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text_without_tag)

    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)

    return text


def remove_stopwords(text) -> list:
    return [w for w in text if w not in stopwords.words('english')]


def array_to_str(text) -> str:
    return ' '.join(text)


def piepline_preprocess(text: list) -> list:
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')

    process = [preprocessing, tokenizer.tokenize, remove_stopwords, array_to_str]

    for proc in process:
        text = list(map(proc, text))

    return text
