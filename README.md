# ML_Docker-Power_Consumption
A simple Machine Learning model deploy with Docker. In this example, the model predicts the PJM East Region (USA) Hourly Power Consumption based on a standard Year, Month, Day and Hour inputs.

The model is based on [Hourly Energy Consumption](https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption) dataset from kaggle and my study on the database and ML model is available at my [Energy_Consumption-Time_Series_Forecasting_Study](https://github.com/diegokurashima/Energy_Consumption-Time_Series_Forecasting_Study) repository.

## Container Running
Request
```
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     172.17.0.1:34328 - "POST /predict?year=2026&month=5&day=12&hour=8 HTTP/1.1" 200 OK
```

Response Body
```
{
  "prediction": 30922.98828125
}
```

Prediction from tests.ipynb
```python
{'prediction': 30922.98828125}
```