import pickle
import yaml

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pandas as pd

from modules.processing import piepline_preprocess

if __name__ == "__main__":
    with open("params.yaml", "r") as fd:
        params = yaml.safe_load(fd)["train"]

    train_data = pd.read_csv("resources/train_data.csv")

    x = train_data.text.values
    y = train_data.target.values

    x = piepline_preprocess(x)

    prep_features = Pipeline(
        steps=[
            ("tfidf", TfidfVectorizer(min_df=2, max_df=0.5, ngram_range=(1, 2))),
        ]
    )
    model = LogisticRegression(
        C=params["C"],
        random_state=params["random_state"],
        solver=params["solver"],
        l1_ratio=params["l1_ratio"],
        penalty=params["penalty"],
    )
    clf = Pipeline(steps=[("preprocessor", prep_features), ("model", model)])

    clf.fit(x, y)

    pickle.dump(clf, open("resources/model.pkl", "wb"))