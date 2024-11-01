from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib

def load_data():
    # Load the wine dataset
    wine = load_wine(as_frame=True)
    data = pd.DataFrame(data=wine.data, columns=wine.feature_names)
    data["target"] = wine.target
    print(data.head())
    return data

def split_data(data, target_column="target"):
    X = data.drop(columns=[target_column])
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test

def save_preprocessed_data(X_train, X_test, y_train, y_test, file_path):
    joblib.dump((X_train, X_test, y_train, y_test), file_path)


data = load_data()
X_train, X_test, y_train, y_test = split_data(data)
save_preprocessed_data(X_train, X_test, y_train, y_test, "preprocessed_data.pkl")


def load_preprocessed_data(file_path):
    return joblib.load(file_path)

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def save_model(model, file_path):
    joblib.dump(model, file_path)


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_preprocessed_data("preprocessed_data.pkl")

    model = train_model(X_train, y_train)
    save_model(model, "model.pkl")