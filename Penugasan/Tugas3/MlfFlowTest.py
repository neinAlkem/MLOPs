from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
import mlflow 
import mlflow.sklearn

mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")
mlflow.set_experiment("MLflow Quickstart")

data = load_diabetes
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

def train_model(alpha):
    with mlflow.start_run():
        model = LinearRegression()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test,predictions)
        
        mlflow.log_param("alpha", alpha)
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(model, "model")
        
        print(f"Model with alpha={alpha}, MSE={mse}")

train_model(alpha=0.5)
train_model(alpha=1.0)

model_uri = "runs:/<run-id/model"
model = mlflow.sklearn.load_model(model_uri)
new_predictions = model.predict(X_test)

