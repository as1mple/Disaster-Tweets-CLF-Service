import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pandas as pd
import nltk

from modules.processing import preprocessing, remove_stopwords, array_to_str

if __name__ == "__main__":
    train_data = pd.read_csv('resources/train_data.csv')
    y = train_data.target.values

    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')

    train_data.text = train_data.text.apply(preprocessing)
    train_data.text = train_data.text.apply(tokenizer.tokenize)
    train_data.text = train_data.text.apply(remove_stopwords)
    train_data.text = train_data.text.apply(array_to_str)

    x = train_data.text.values

    prep_features = Pipeline(steps=[
        ('tfidf', TfidfVectorizer(min_df=2, max_df=0.5, ngram_range=(1, 2))),
    ])
    model = LogisticRegression(C=1.0)
    clf = Pipeline(steps=[('preprocessor', prep_features),
                          ('model', model)
                          ])

    clf.fit(x, y)

    pickle.dump(clf, open('resources/model.pkl', 'wb'))
