def predict_sentiment(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    features = {word: (word in words) for word in word_features}
    vector = vectorizer.transform([' '.join(features.keys())])
    prediction = model.predict(vector)
    return prediction[0]

# Test with a new review
new_review = "This movie was fantastic! I loved it."
print(f'Prediction: {predict_sentiment(new_review)}')
