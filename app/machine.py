import joblib
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier


class Machine:

    def __init__(self, df: DataFrame):
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)

    def __call__(self, feature_basis: DataFrame):
        prediction, *_ = self.model.predict(feature_basis)
        confidence = self.model.predict_proba(feature_basis).max()
        return prediction, confidence

    def save(self, filepath):
        joblib.dump(self.model, filepath)

    @staticmethod
    def open(filepath):
        model = joblib.load(filename=filepath)
        return model

    def info(self, df):
        return f"Model Used: {self.name} " \
               f"Timestamp: {df['Timestamp'][0]}"
