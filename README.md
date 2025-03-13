# Sentiment Analysis API

## Overview
This project is a **Sentiment Analysis API** built with **FastAPI**, designed to classify customer reviews as **positive, negative, or neutral**. The API takes textual input, processes it using a pre-trained **Machine Learning model**, and returns the predicted sentiment. It is designed for **real-time predictions** and can be deployed on **Render** for free hosting.

## Features
- **FastAPI Backend:** A high-performance, asynchronous web framework.
- **Machine Learning Model:** Uses **scikit-learn** for sentiment classification.
- **Real-time Predictions:** API endpoints to process customer reviews.
- **Deployment on Render:** Configured to run on cloud infrastructure.
- **Docker Support:** Ensures consistency across different environments.
- **GitHub Codespaces Integration:** Enables cloud-based development.

## Tech Stack
- **Backend:** FastAPI
- **Machine Learning:** Scikit-learn, Pandas
- **Deployment:** Render, Docker (optional)
- **Package Management:** Pip, Virtual Environment

## Project Structure
```
📂 sentiment-analysis-api
│── data/
│   ├── customer-review.csv  # Dataset (optional)
│── myenv/                    # Virtual environment
│── model.pkl                 # Trained ML model
│── main.py                    # FastAPI application
│── modelling.py               # ML training script
│── requirements.txt           # Python dependencies
│── README.md                  # Project documentation
│── Dockerfile                 # (Optional) Containerization setup
```

## Setup and Installation
### 1. Clone the repository
```sh
$ git clone https://github.com/your-username/sentiment-analysis-api.git
$ cd sentiment-analysis-api
```

### 2. Create a Virtual Environment
```sh
$ python -m venv myenv
$ source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 3. Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4. Run the FastAPI Server
```sh
$ uvicorn main:app --host 0.0.0.0 --port 8000
```
The API will be available at: [http://localhost:8000](http://localhost:8000)

### 5. Test the API
Open your browser and go to:
```sh
http://localhost:8000/docs
```
This will open the **Swagger UI**, where you can test the API endpoints.

## API Endpoints
| Method | Endpoint       | Description |
|--------|---------------|-------------|
| POST   | /predict      | Predict sentiment from a text input |
| GET    | /             | Health check endpoint |

### Example Request
```sh
POST /predict
{
    "text": "The product is amazing! I love it."
}
```
### Example Response
```json
{
    "sentiment": "positive"
}
```

## Deployment
### Option 1: Deploy to Render
1. Push your code to GitHub.
2. Connect the repository to Render.
3. Set the **start command**:
   ```sh
   gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
   ```
4. Deploy!

### Option 2: Run with Docker
1. Build the Docker image:
   ```sh
   docker build -t sentiment-api .
   ```
2. Run the container:
   ```sh
   docker run -p 8000:8000 sentiment-api
   ```

## Contributing
Feel free to contribute! Fork the repo, create a feature branch, and submit a pull request.

## License
This project is an open-source and anyone is free to use it.

## Contact
For inquiries, reach out via GitHub Issues or email: **v.jha85@gmail.com**


