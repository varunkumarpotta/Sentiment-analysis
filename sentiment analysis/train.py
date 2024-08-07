# Train the model
model = MultinomialNB()
model.fit(train_vectors, train_labels)

# Evaluate the model
predictions = model.predict(test_vectors)
accuracy = accuracy_score(test_labels, predictions)
print(f'Accuracy: {accuracy:.2f}')
print(classification_report(test_labels, predictions))
