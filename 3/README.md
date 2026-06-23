# AI Course Project 3: Hotel Price Classification Using Machine Learning

## Overview

This project focuses on applying machine learning techniques to predict hotel pricing categories based on information collected from an online hotel booking platform.

The project covers the complete machine learning workflow, including exploratory data analysis, feature engineering, data preprocessing, model development, hyperparameter optimization, ensemble learning, and implementation of a boosting algorithm from scratch.

The primary objective is to classify hotels into price categories and compare the performance of multiple machine learning algorithms.

---

## Objectives

* Analyze real-world hotel booking data.
* Perform exploratory data analysis (EDA).
* Clean and preprocess raw data.
* Engineer meaningful features.
* Transform continuous pricing information into classification labels.
* Train and evaluate multiple machine learning models.
* Explore ensemble learning methods.
* Implement the SAMME boosting algorithm from scratch.
* Compare custom and library-based boosting approaches.

---

## Dataset

The dataset contains hotel information collected from an online reservation platform.

Features include:

* Hotel name
* Location
* User rating
* Rating quality category
* Number of reviews
* Room type
* Bed type
* Room size
* Distance from city center
* Number of nights
* Number of adults
* Free cancellation availability
* Hotel price

The target variable was created by converting hotel prices into two categories:

* Budget Hotels (Class 0)
* Premium Hotels (Class 1)

using the median hotel price as the classification threshold.

---

## Exploratory Data Analysis (EDA)

Comprehensive exploratory analysis was performed to better understand the dataset and identify useful patterns.

### Analysis Performed

* Dataset structure inspection
* Statistical summaries
* Missing value analysis
* Unique value distributions
* Correlation analysis
* Scatter plots
* Hexbin visualizations
* Feature-target relationship analysis

### Goals

* Discover hidden patterns
* Identify influential features
* Detect anomalies and outliers
* Guide feature engineering decisions

---

## Data Preprocessing

Several preprocessing techniques were applied to prepare the data for machine learning models.

### Missing Value Handling

Different imputation strategies were explored depending on feature characteristics.

### Feature Cleaning

* Removal of irrelevant attributes
* Extraction of numerical values from textual columns
* Handling inconsistent data formats

### Categorical Encoding

Categorical features were transformed into numerical representations suitable for machine learning algorithms.

### Scaling

Appropriate normalization and standardization techniques were applied where necessary.

---

## Feature Engineering

Additional features were generated to improve predictive performance.

Examples include:

* Derived room-related features
* Reservation-based indicators
* Encoded location information
* User-review statistics

Feature engineering played a significant role in improving model accuracy and robustness.

---

## Machine Learning Models

Several classification algorithms were implemented and compared.

### Naive Bayes

A probabilistic classifier based on Bayes' theorem and conditional independence assumptions.

#### Advantages

* Fast training
* Computationally efficient
* Effective on certain high-dimensional datasets

---

### Decision Tree

A tree-based classification model that recursively partitions data based on feature importance.

#### Techniques Applied

* Hyperparameter tuning
* Tree visualization
* Pruning strategies

#### Advantages

* Easy interpretability
* Transparent decision-making process

---

### Random Forest

An ensemble learning method based on multiple decision trees.

#### Techniques Applied

* RandomizedSearchCV
* Hyperparameter optimization
* Feature importance analysis

#### Advantages

* High accuracy
* Reduced overfitting
* Improved robustness

---

### AdaBoost

A boosting-based ensemble method that combines multiple weak learners.

#### Experiments

* Hyperparameter tuning
* Impact of varying estimator counts
* Performance comparison across configurations

#### Advantages

* Strong predictive performance
* Adaptive learning mechanism

---

### XGBoost

An advanced gradient boosting framework designed for efficiency and accuracy.

#### Hyperparameter Optimization

Grid search was performed over:

* Learning rate
* Number of estimators
* Maximum tree depth
* Minimum samples split
* Minimum samples leaf
* Maximum features

#### Advantages

* High predictive power
* Efficient computation
* Excellent performance on structured data

---

## Boosting From Scratch

One of the key objectives of this project was implementing the SAMME Boosting algorithm from scratch.

### Implementation Features

* Sample weight initialization
* Weighted training process
* Error computation
* Learner weight calculation
* Sample weight updates
* Weighted voting mechanism
* Multi-class support

### Educational Value

This implementation provided a deeper understanding of how boosting algorithms improve predictive performance by combining weak learners into a strong ensemble model.

---

## Custom vs Library Boosting

The custom SAMME implementation was compared against Scikit-Learn's implementation.

The comparison focused on:

* Classification performance
* Prediction behavior
* Training dynamics
* Algorithmic consistency

---

## Model Evaluation

Models were evaluated using multiple classification metrics.

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Macro Average
* Micro Average
* Weighted Average

Using multiple metrics provided a comprehensive view of model performance across different evaluation perspectives.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Key AI Concepts

* Supervised Learning
* Classification
* Data Preprocessing
* Feature Engineering
* Exploratory Data Analysis
* Decision Trees
* Ensemble Learning
* Bagging
* Boosting
* Hyperparameter Optimization
* Gradient Boosting
* Model Evaluation

---

## Results

The project demonstrates how proper preprocessing, feature engineering, and ensemble methods can significantly improve classification performance.

Comparative analysis revealed the strengths and weaknesses of classical machine learning algorithms versus advanced boosting techniques.

The custom SAMME implementation further provided valuable insight into the internal mechanics of ensemble learning.

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Real-world data analysis
* Feature engineering techniques
* Machine learning pipelines
* Ensemble learning methods
* Hyperparameter tuning
* Classification evaluation
* Boosting algorithms
* Implementing machine learning algorithms from scratch

---

## Future Improvements

* Explore stacking and blending ensembles
* Apply advanced feature selection methods
* Investigate deep learning approaches
* Extend boosting implementation with additional variants
* Deploy the best-performing model as a web application

---

Part of the Artificial Intelligence Course Projects Series.
