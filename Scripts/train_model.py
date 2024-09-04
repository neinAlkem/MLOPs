import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

def train_model():
    X_train = pd.read_csv('C:/Users/Bagas/OneDrive/Documents/GitHub/MLOPs/Penugasan/Tugas2/data/X_train.csv')
    y_train = pd.read_csv('C:/Users/Bagas/OneDrive/Documents/GitHub/MLOPs/Penugasan/Tugas2/data/y_train.csv')

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train.values.ravel())
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/logistic_regression_model.pkl')

if __name__ == "__main__":
    train_model()
