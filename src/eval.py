import json
import pickle

import pandas as pd

from modules.processing import piepline_preprocess
from sklearn.metrics import f1_score

if __name__ == "__main__":

    test_data = pd.read_csv("resources/test_data.csv")
    clf = pickle.load(open("resources/model.pkl", "rb"))

    x_test = test_data.text.values
    y_test = test_data.target.values

    x_test = piepline_preprocess(x_test)
    predict = clf.predict(x_test)
    score = f1_score(y_test, predict)

    with open("metrics.json", "w") as f:
        json.dump(
            {
                "test": {
                    "f1_score": score,
                }
            },
            f,
            indent=4,
        )
