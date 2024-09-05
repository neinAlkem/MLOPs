import joblib
import os

def deploy_model():
    model = joblib.load('models/random_forest_model.pkl')
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/final_model.pkl')

if __name__ == "__main__":
    deploy_model()
