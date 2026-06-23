# AI Course Project 4: Building Deep Neural Networks from Scratch

## Overview

This project focuses on implementing the fundamental building blocks of deep neural networks from scratch and understanding how modern deep learning systems operate internally.

Rather than relying on high-level deep learning frameworks, core neural network layers, activation functions, loss functions, and optimization algorithms were manually implemented using Python and NumPy. The completed framework was then used to train and evaluate models on image classification and regression tasks.

The project concludes with convolutional neural network training using the VGG16 architecture on a real-world image dataset.

---

## Objectives

* Understand the mathematical foundations of deep learning.
* Implement neural network layers from scratch.
* Develop forward and backward propagation algorithms.
* Verify gradients using numerical gradient checking.
* Build a fully connected deep neural network.
* Train models using gradient-based optimization.
* Apply neural networks to classification and regression problems.
* Explore convolutional neural networks for image recognition.

---

## Core Components Implemented

### Fully Connected Layer

Implemented:

* Forward propagation
* Backward propagation
* Weight and bias gradient computation

This layer serves as the fundamental building block of dense neural networks.

---

### Activation Functions

#### ReLU (Rectified Linear Unit)

Implemented:

* Forward pass
* Backward pass

Used to introduce non-linearity and improve training efficiency.

#### Sigmoid

Implemented:

* Forward pass
* Backward pass

Used for probabilistic outputs and binary decision boundaries.

---

### Composite Neural Network Layers

Implemented a combined:

* Fully Connected Layer
* ReLU Activation Layer

This modular design simplifies network construction and training.

---

### Loss Functions

#### Softmax Cross-Entropy Loss

Used for multi-class classification problems.

Implemented:

* Loss computation
* Gradient computation

#### Mean Squared Error (MSE)

Used for regression tasks.

Implemented:

* Loss computation
* Gradient computation

---

## Gradient Verification

To ensure correctness of all implementations:

* Analytical gradients from backpropagation were compared with numerical gradients.
* Gradient checking was performed for all major components.
* Differences were verified to be negligible.

This validation process confirmed the correctness of the implementation.

---

## Neural Network Architecture

After implementing individual layers, they were combined into a complete deep neural network framework.

The network supports:

* Multiple hidden layers
* Flexible architecture design
* Forward propagation
* Backpropagation
* Parameter updates
* Modular layer construction

---

## Optimization Algorithms

### Stochastic Gradient Descent (SGD)

Implemented SGD to update model parameters using mini-batch gradients.

### Momentum Optimization

Implemented Momentum-based updates to:

* Accelerate convergence
* Reduce oscillations
* Improve optimization stability

---

## Dataset 1: MNIST Handwritten Digit Classification

The custom neural network was trained and evaluated on the MNIST dataset.

### Task

Classify grayscale images of handwritten digits (0–9).

### Workflow

1. Data preprocessing
2. Neural network construction
3. Training using SGD with Momentum
4. Validation and performance evaluation
5. Hyperparameter tuning

---

## Dataset 2: California Housing Price Prediction

The implemented framework was also applied to a regression task using the California Housing dataset.

### Task

Predict housing prices based on multiple numerical features.

### Objective

Demonstrate the flexibility of the neural network framework for both:

* Classification
* Regression

problems.

---

## Convolutional Neural Networks

The final phase of the project introduces deep convolutional neural networks.

### VGG16 Architecture

A VGG16-based model was trained on the CIFAR-10 dataset.

### CIFAR-10 Classes

* Airplane
* Automobile
* Bird
* Cat
* Deer
* Dog
* Frog
* Horse
* Ship
* Truck

---

## CNN Concepts Explored

### Convolutional Layers

Used to automatically learn:

* Edges
* Textures
* Shapes
* High-level visual features

from images.

### Fully Connected Layers

Used after feature extraction to perform final classification.

### Feature Hierarchies

The network progressively learns:

1. Low-level features
2. Mid-level patterns
3. Semantic object representations

---

## Technologies Used

* Python
* NumPy
* Matplotlib
* Scikit-Learn
* Jupyter Notebook
* PyTorch
* Torchvision

---

## Key AI Concepts

* Deep Learning
* Artificial Neural Networks
* Backpropagation
* Gradient Descent
* Numerical Gradient Checking
* Activation Functions
* Loss Functions
* Optimization Algorithms
* Convolutional Neural Networks
* Image Classification
* Regression
* Feature Learning

---

## Results

The project successfully demonstrates how modern neural networks can be constructed from first principles.

By implementing each component manually, it provides a deeper understanding of:

* Forward propagation
* Backpropagation
* Optimization
* Representation learning

The VGG16 experiment further illustrates the effectiveness of deep convolutional architectures for image recognition tasks.

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

* Building neural networks from scratch
* Deriving and implementing backpropagation
* Gradient verification techniques
* Training deep learning models
* Optimization strategies
* Image classification pipelines
* Convolutional neural network architectures
* Practical deep learning workflows

---

## Future Improvements

* Implement additional activation functions
* Add Batch Normalization support
* Introduce Dropout regularization
* Experiment with Adam optimization
* Build custom CNN architectures
* Explore transfer learning techniques

---

Part of the Artificial Intelligence Course Projects Series.
