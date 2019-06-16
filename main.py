### Musoc 2019
### Machine Learning Model for Classification of toxic comments

### @author: Pratyush Kerhalkar

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

print ("imported libraries")

print ("loading data...")
train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")
sub = pd.read_csv("sample_submission.csv")
test_labels = pd.read_csv("test_labels.csv")
print ("data loaded")

test_classes = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]

train_text = train_data["comment_text"]
test_text = test_data["comment_text"]

text = pd.concat([train_text, test_text])

print ("creating tfidf vectorizer for input dataset")
word_vectorizer = TfidfVectorizer(
    min_df = 1,
    stop_words= 'english')

word_vectorizer.fit(text)

train_features = word_vectorizer.transform(train_text)
test_features = word_vectorizer.transform(test_text)


print ("Creating model")
# Sample Logistic Regression model for "toxic" comment feature
model = LogisticRegression(C = 0.1, solver='sag')
model.fit(train_features, train_data["toxic"])
predicted_value = model.predict(train_features)
print ("Model created")

# Accuracy Calculation for sample logistic regression model
true_value = train_data["toxic"]
true_value_numpy = true_value.to_numpy()
total = len(true_value_numpy)
count = 0

for i in range(len(true_value_numpy)):
    if true_value_numpy[i] == predicted_value[i]:
        count += 1

accuracy = float(count/total)*100
print ("Model accuracy obtained: ", accuracy)
# Accuracy obtained: 93.52%


# Logistic regression model creation
output_logistic_regression = pd.DataFrame.from_dict({'id': test_data['id']})

for feature in test_classes:
    model = LogisticRegression(C=0.1, solver='sag')
    model.fit(train_features, train_data[feature])
    output_logistic_regression[feature] = model.predict_proba(test_features)[:,1]
    
    