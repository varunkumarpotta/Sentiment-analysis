
positive_words = ['happy', 'good', 'great', 'fantastic', 'excellent', 'amazing', 'positive', 'fortunate', 'correct', 'superior']
negative_words = ['sad', 'bad', 'terrible', 'awful', 'horrible', 'negative', 'unfortunate', 'wrong', 'inferior', 'poor','worst']

def analyze_sentiment(text):
    text = text.lower()
    positive_score = sum(word in text for word in positive_words)
    negative_score = sum(word in text for word in negative_words)
    
    if positive_score > negative_score:
        return 'Positive'
    elif negative_score > positive_score:
        return 'Negative'
    else:
        return 'Neutral'

# Example usage
if __name__ == '__main__':
    text = input("Enter a text: ")
    result = analyze_sentiment(text)
    print(f'Sentiment: {result}')
