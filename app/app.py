import os
import pandas as pd
import pickle
from fastapi import FastAPI
import datetime

import xgboost as xgb
import sklearn

app = FastAPI()

path_app = os.getcwd()
path_model = os.path.join(path_app, 'model/model.pkl')

with open(path_model, 'rb') as f:
    model = pickle.load(f)

def create_features_Datetime(df_input):
    '''
    Create datetime features for "Datetime" column
    '''
    
    df = df_input.copy()

    # Standard Datetime Features
    df['Year'] = df.index.year
    df['Quarter'] = df.index.quarter
    df['Month'] = df.index.month
    df['Day'] = df.index.day
    df['Hour'] = df.index.hour

    df['Day_of_Year'] = df.index.dayofyear

    df['Weekday'] = df.index.weekday
    df['Is_Weekend'] =  df.index.day_name().isin(['Saturday', 'Sunday'])

    return df

@app.post('/predict')
async def predict(year, month, day, hour):

    dt = datetime.datetime(int(year), int(month), int(day), int(hour))

    # Dataframe
    df = pd.DataFrame({"Datetime": [dt]})
    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df = df.set_index("Datetime")

    data = create_features_Datetime(df)

    cols_train = ['Quarter', 'Month', 'Day', 'Hour', 'Day_of_Year', 'Weekday', 'Is_Weekend']
    data = data[cols_train]
    
    prediction_result = model.predict(data)
    prediction = float(prediction_result[0])
    return {'prediction': prediction}