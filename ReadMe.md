# 🧠 Handwritten Digit Classification using Artificial Neural Network (ANN)

A beginner-friendly Deep Learning project that classifies handwritten digits (0–9) using an Artificial Neural Network (ANN) built with TensorFlow and Keras.

This project uses the MNIST handwritten digit dataset and demonstrates the complete deep learning workflow, from loading data to training, evaluating, saving, and using a trained model for prediction.

---

## 📌 Project Overview

This project covers the fundamental concepts of deep learning by building an ANN capable of recognizing handwritten digits.

The workflow includes:

- Loading the MNIST dataset
- Data preprocessing
- Building an Artificial Neural Network
- Training the model
- Evaluating model performance
- Saving the trained model
- Loading the saved model
- Predicting handwritten digits
- Measuring prediction confidence

---

## 📂 Project Structure

```
handwritten-digit-classification-ann/
│
├── train.py              # Train the ANN model
├── predict.py            # Load model and make predictions
├── mnist_ann.keras       # Saved trained model
├── README.md
```

---

## 🛠 Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib

---

## 🧠 Neural Network Architecture

```
Input Image (28×28)
        │
        ▼
Flatten Layer
(28×28 → 784)
        │
        ▼
Dense Layer (128 neurons)
Activation: ReLU
        │
        ▼
Output Layer (10 neurons)
Activation: Softmax
```

---

## 📊 Dataset

Dataset used:

**MNIST Handwritten Digits**

- 60,000 training images
- 10,000 testing images
- Image size: 28 × 28 pixels
- Classes: Digits 0–9

---

## ⚙️ Training Configuration

- Optimizer: Adam
- Loss Function: Sparse Categorical Crossentropy
- Metric: Accuracy
- Epochs: 10

---

## 📈 Model Performance

Test Accuracy:

```
97.65%
```

Test Loss:

```
0.0885
```

*(Results may vary slightly between runs.)*

---

## 🚀 Features

✅ Load MNIST dataset

✅ Normalize image data

✅ Build ANN using TensorFlow/Keras

✅ Train neural network

✅ Evaluate model performance

✅ Save trained model

✅ Load saved model

✅ Predict handwritten digits

✅ Display prediction confidence

---

## 📚 Concepts Learned

During this project I learned:

- Artificial Neural Networks (ANN)
- Forward Propagation
- Backpropagation
- Gradient Descent
- Activation Functions
- ReLU
- Softmax
- Loss Functions
- Optimizers (Adam)
- Model Training
- Model Evaluation
- Model Saving & Loading
- Deep Learning Inference

---

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/madebyRohitjha/Deep-learning-project-01.git
```

### Install dependencies

```bash
pip install tensorflow matplotlib numpy
```

### Train the model

```bash
python train.py
```

### Predict handwritten digits

```bash
python predict.py
```

---

## 🎯 Future Improvements

- Add training accuracy and loss graphs
- Predict custom handwritten digits
- Build a simple GUI
- Deploy using Streamlit
- Improve model architecture
- Compare ANN with CNN

---

## 👨‍💻 Author

**Rohit Jha**

AI & Machine Learning Student

GitHub: https://github.com/madebyRohitjha

Currently learning:
- Machine Learning
- Deep Learning
- Computer Vision
- Large Language Models (LLMs)

---

## ⭐ If you found this project helpful, consider giving it a star!