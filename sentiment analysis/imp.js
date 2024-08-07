function analyzeSentiment() {
    const text = document.getElementById("input-text").value;

    // List of positive and negative words
    const positiveWords = ["good", "happy", "joy", "excellent", "great", "positive", "fortunate", "correct", "superior"];
    const negativeWords = ["bad", "sad", "pain", "terrible", "awful", "negative", "unfortunate", "wrong", "inferior"];

    // Preprocess the text
    const words = text.toLowerCase().replace(/[.,!?;:(){}\[\]"]/g, "").split(/\s+/);

    // Count positive and negative words
    let positiveCount = 0;
    let negativeCount = 0;

    words.forEach(word => {
        if (positiveWords.includes(word)) {
            positiveCount++;
        } else if (negativeWords.includes(word)) {
            negativeCount++;
        }
    });

    // Determine sentiment
    let sentiment = "Neutral";
    if (positiveCount > negativeCount) {
        sentiment = "Positive";
    } else if (negativeCount > positiveCount) {
        sentiment = "Negative";
    }

    // Display result
    document.getElementById("result").textContent = `The sentiment of the text is: ${sentiment}`;
}
