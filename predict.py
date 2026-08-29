correct = 0
import random
import tensorflow as tf

from tensorflow.keras.datasets import mnist

model = tf.keras.models.load_model("mnist_ann.keras")

print("Model loaded successfully!")

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_test = X_test / 255.0


image_index = random.randint(0, 9999)

prediction = model.predict(X_test[image_index].reshape(1, 28, 28), verbose=0)

predicted_digit = prediction.argmax()

print("Predicted Digit:", predicted_digit)
print("Actual Digit:", y_test[image_index])

confidence = prediction.max() * 100
print(f"Confidence: {confidence:.2f}%")
for i in range(5):
    image_index = random.randint(0, 9999)

    prediction = model.predict(
        X_test[image_index].reshape(1, 28, 28),
        verbose=0
    )

    predicted_digit = prediction.argmax()
    confidence = prediction.max() * 100

    print(f"\nImage {i+1}")
    print("Prediction:", predicted_digit)
    print("Actual:", y_test[image_index])
    print(f"Confidence: {confidence:.2f}%")

    for i in range(100):
    image_index = random.randint(0, 9999)

    prediction = model.predict(
        X_test[image_index].reshape(1, 28, 28),
        verbose=0
    )

    predicted_digit = prediction.argmax()

    if predicted_digit == y_test[image_index]:
        correct += 1

accuracy = (correct / 100) * 100

print(f"Correct Predictions: {correct}/100")
print(f"Accuracy: {accuracy:.2f}%")