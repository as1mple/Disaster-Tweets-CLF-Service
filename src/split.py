import yaml

from sklearn.model_selection import train_test_split
import pandas as pd

if __name__ == "__main__":
    with open("./params.yaml", "r") as fd:
        params = yaml.safe_load(fd)["split"]

    data = pd.read_csv("resources/train.csv")
    train, test = train_test_split(
        data,
        stratify=data.target.values,
        test_size=params["test_size"],
        random_state=params["seed"],
        shuffle=params["shuffle"],
    )

    train.to_csv("resources/train_data.csv", index=False)
    test.to_csv("resources/test_data.csv", index=False)
