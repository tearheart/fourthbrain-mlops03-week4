from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

import logging
from logging.config import dictConfig
from src.log_config import log_config # this is your local file

from pydantic import BaseModel

from transformers import pipeline


dictConfig(log_config)
logger = logging.getLogger("week4")

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

sentiment_model = pipeline("sentiment-analysis")

class PredictionRequest(BaseModel):
  query_string: str

@app.get('/')
def read_form():
    return {"message": "Hello World, welcome the sentiment machine!"}

@app.get("/health")
def health():
    logger.info("It worked")
    return {"message": "Hello World"}

@app.post("/sentiment")
def sentiment(request: PredictionRequest):
    sentiment_query_sentence = request.query_string
    sentiment = sentiment_model(sentiment_query_sentence)
    return f"Sentiment test: {sentiment_query_sentence} == {sentiment}"

@app.get("/form")
def form_post(request: Request):
    result = "Type a sentence and I'll return the sentiment!!"
    return templates.TemplateResponse("form.html", {"request": request, "result": result})

@app.post("/form")
def form_post(request: PredictionRequest, sentence: str = Form(...)):
    sentiment = sentiment_model(sentence)
    return templates.TemplateResponse('form.html', {"request": request, "sentiment": sentiment, "sentence": sentence})
