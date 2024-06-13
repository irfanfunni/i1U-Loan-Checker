import pandas as pd
import joblib

model = joblib.load('best_model_pipeline_random.pkl')

def predict_inputs(user_inputs):
    # convert to df
    df = pd.DataFrame(user_inputs)
    # Run predictions
    return float(model.predict_proba(df)[:, 1])