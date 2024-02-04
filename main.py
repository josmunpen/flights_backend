from fastapi import FastAPI, Request
import numpy as np
import joblib
import logging
import time
import pandas as pd

from schemas.flights import InputFlight

app = FastAPI(debug=True)

# Set logging config
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logger.addHandler(handler)

last_model = "./models/dtr.pkl"

# Load model from disk
loaded_model = joblib.load(last_model)
logger.info('Model loaded succesfully')

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def root():
    return {"message": "Everything look's ok"}


@app.post("/inference_price")
async def predict(
    input_flight: InputFlight,

):
    input = input_flight.__dict__
    input = pd.json_normalize(input)


    start = time.time()
    res = loaded_model.predict(input)[0]
    logger.info(f'Inference generated - {time.time() - start}s')

    return res

