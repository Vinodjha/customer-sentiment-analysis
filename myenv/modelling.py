import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer

nltk.download('stopwords')
nltk.download('punkt')

#Cleaning the data before putting it into a dataframe. I had to remove the several quotes in the data before it could parse correctly

# File path (update with actual file path)
file_path = "/workspaces/customer-sentiment-analysis/data/customer-review.csv"

# Read file, remove all quotes, and overwrite the file
with open(file_path, "r", encoding="utf-8") as f:
    data = f.read().replace('"', '')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(data)

data  = pd.read_csv(file_path)
print(data.head())

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalnum() and word not in stopwords.words("english")]
    return " ".join(tokens)

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB

X = data['Text'].apply(preprocess_text)
X_train, X_test, y_train, y_test = train_test_split(X, data['Sentiment'], test_size=0.2, random_state=42)

model = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB())
])

model.fit(X_train, y_train)

