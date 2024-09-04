import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import joblib
import json

def evaluate_model():
    X_test = pd.read_csv('C:/Users/Bagas/OneDrive/Documents/GitHub/MLOPs/Penugasan/Tugas2/data/X_test.csv')
    y_test = pd.read_csv('C:/Users/Bagas/OneDrive/Documents/Github/MLOps/Penugasan/Tugas2/data/y_test.csv')
    model = joblib.load('models/logistic_regression_model.pkl')

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    with open('result/evaluation_report.json', 'w') as f:
        json.dump(report, f, indent=4)

    with open('result/accuracy.txt', 'w') as f:
        f.write(f'Accuracy: {accuracy}\n')

if __name__ == "__main__":
    evaluate_model()
