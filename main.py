import pickle
import fastapi
from pydantic import BaseModel

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

app = fastapi.FastAPI()

class ReviewInput(BaseModel):
    text : str


@app.post('/predict')

def predict_sentiment(review: ReviewInput):
    prediction = model.predict('review.text')[0]
    return {'Sentiment': prediction}


@app.get('/')
def home():
    return {'message': 'Welcome to the sentiment analysis API'}
