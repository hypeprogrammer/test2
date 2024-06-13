# app/repositories/iris_repository.py
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

class IrisRepository:
    def __init__(self):
        self.model = None
        self._load_data()
        self._train_model()

    def _load_data(self):
        iris = load_iris()
        self.X = iris.data
        self.y = iris.target

    def _train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        joblib.dump(self.model, 'iris_model.pkl')

    def load_model(self):
        if not self.model:
            self.model = joblib.load('iris_model.pkl')
        return self.model