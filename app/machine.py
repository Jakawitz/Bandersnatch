import re

import joblib
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier


class Machine:

    def __init__(self, df: DataFrame):
        self.name = "Random Forest"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)

    def __call__(self, feature_basis: DataFrame):
        prediction, *_ = self.model.predict(feature_basis)
        return prediction

    def save(self, filepath):
        joblib.dump(self.model, filepath)

    @staticmethod
    def open(filepath):
        joblib.load(filename=filepath)

    def info(self):
        return f"Model Used: {self.name}\n Timestamp {self.df['Timestamp']}"
