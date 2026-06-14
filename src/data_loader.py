import pandas as pd
from sklearn.model_selection import train_test_split

def get_train_test_data():
    df = pd.read_csv("../data/train.csv")

    X = df.drop("Activity", axis=1)
    y = df["Activity"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test
