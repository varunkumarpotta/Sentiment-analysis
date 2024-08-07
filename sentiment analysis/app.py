# List of positive and negative words
positive_words = ["good", "happy", "joy", "excellent", "great", "positive", "fortunate", "correct", "superior","wonderful"]
negative_words = ["bad", "sad", "pain", "terrible", "awful", "negative", "unfortunate", "wrong", "inferior","worst"]

# Function to preprocess the text
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    for char in ['.', ',', '!', '?', ';', ':', '(', ')', '[', ']', '{', '}', '"', "'"]:
        text = text.replace(char, "")  # Remove punctuation
    words = text.split()  # Split into words
    return words

# Function to analyze sentiment
def analyze_sentiment(text):
    words = preprocess_text(text)
    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)
    
    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"

# Example usage
text = "I am very happy with the excellent service!"
sentiment = analyze_sentiment(text)
print(f"The sentiment of the text is: {sentiment}")
