import pickle
import fastapi
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

app = fastapi.FastAPI()

# Allow frontend requests from any origin (for testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReviewInput(BaseModel):
    text: str

@app.post('/predict')
def predict_sentiment(review: ReviewInput):
    prediction = model.predict([review.text])[0]
    return {'Sentiment': prediction}

@app.get('/', response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sentiment Analysis</title>
        <script>
            async function getSentiment() {
                let text = document.getElementById("review").value;
                let response = await fetch('/predict', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({text: text})
                });
                let data = await response.json();
                document.getElementById("result").innerText = "Sentiment: " + data.Sentiment;
            }
        </script>
    </head>
    <body>
        <h2>Sentiment Analysis</h2>
        <input type="text" id="review" placeholder="Enter a review">
        <button onclick="getSentiment()">Predict</button>
        <p id="result"></p>
    </body>
    </html>
    """