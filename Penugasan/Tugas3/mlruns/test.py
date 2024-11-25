# from sklearn.datasets import load_boston
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
# import mlflow
# import mlflow.sklearn

# # Load dataset
# data = load_boston()
# X = data.data
# y = data.target

# # Split data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# def train_model(alpha):
#     # Set our tracking server uri for logging
#     mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")
#     # Create a new MLflow Experiment
#     mlflow.set_experiment("MLflow Quickstart")
#     with mlflow.start_run():
#         model = LinearRegression()
#         model.fit(X_train, y_train)
#         predictions = model.predict(X_test)
#         mse = mean_squared_error(y_test, predictions)

#         # Logging parameter, metrics, and model to MLflow
#         mlflow.log_param("alpha", alpha)
#         mlflow.log_metric("mse", mse)
#         mlflow.sklearn.log_model(model, "model")

#         print(f"Model with alpha={alpha}, MSE={mse}")

# # Train model with default alpha value
# train_model(alpha=0.1)


from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn

# Load dataset
data = fetch_california_housing()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(alpha):
    # Set our tracking server uri for logging
    mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")
    mlflow.autolog()    # Create a new MLflow Experiment
    mlflow.set_experiment("MLflow Quickstart")
    with mlflow.start_run():
        model = LinearRegression()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)

        # Logging parameter, metrics, and model to MLflow
        mlflow.log_param("alpha", alpha)
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(model, "model")

        print(f"Model with alpha={alpha}, MSE={mse}")

# Train model with default alpha value
train_model(alpha=0.1)
