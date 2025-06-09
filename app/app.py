import pickle
from fastapi import FastAPI

app = FastAPI()
model = pickle.load('model/model.pkl')

@app.post('/predict')
def predict(data):
    prediction = model.predict(data)
    return { 'prediction': prediction
            }

if __name__ == '__main__':
    app.run(app, host='0.0.0.0', port=8000)