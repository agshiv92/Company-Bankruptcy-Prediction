from azureml.core.model import Model
import numpy as np
import pandas as pd
import joblib
import json
import pickle
import os

def init():
    global model
    model_path = Model.get_model_path("automl_model")
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = json.loads(raw_data)['data']
        data = pd.DataFrame.from_dict(data)
        result = model.predict(data)
        return result.tolist()
    
    except Exception as ex:
        error = str(ex)
        return error
