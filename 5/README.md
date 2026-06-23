# AI Course Project 5: News Article Clustering and Analysis(Using K-Means Clustering, DBSCAN, Hierarchical Clustering)

## Overview

This project explores unsupervised learning techniques for clustering news articles into meaningful groups based on their semantic content. The objective is to automatically discover hidden structures within textual data and evaluate the effectiveness of different clustering algorithms on a real-world news dataset.

The project combines modern Natural Language Processing (NLP) techniques with classical clustering algorithms to transform raw text into meaningful vector representations and organize documents into coherent clusters.

---

## Objectives

* Preprocess and clean textual news data.
* Generate semantic embeddings using Sentence Transformers.
* Apply multiple clustering algorithms to group similar articles.
* Compare clustering performance using quantitative evaluation metrics.
* Visualize high-dimensional text embeddings through dimensionality reduction techniques.
* Analyze the strengths and weaknesses of different clustering approaches.

---

## Dataset

The dataset consists of English-language news articles collected from multiple news categories.

Each document contains textual content and an associated news category used for evaluation purposes.

---

## Text Preprocessing

Several preprocessing techniques were explored to improve text quality before feature extraction:

* Stopword removal
* Removal of special characters and unnecessary whitespace
* Text normalization
* Stemming experiments
* Lemmatization experiments

The impact of different preprocessing strategies was analyzed and compared.

---

## Feature Extraction

Instead of relying on traditional bag-of-words representations, semantic embeddings were generated using:

* Sentence Transformers
* Model: `all-MiniLM-L6-v2`

This transformer-based model converts each news article into a dense vector representation that captures semantic meaning and contextual relationships between words and sentences.

---

## Clustering Algorithms

Three clustering methods were implemented and evaluated:

### 1. K-Means Clustering

* Partition-based clustering algorithm
* Number of clusters determined using the Elbow Method
* Fast and efficient for large datasets

### 2. DBSCAN

* Density-based clustering algorithm
* Capable of detecting outliers
* Does not require specifying the number of clusters beforehand

### 3. Hierarchical Clustering

* Builds nested clusters using a tree-like structure
* Provides insight into relationships between clusters
* Useful for exploratory data analysis

---

## Dimensionality Reduction

Because transformer embeddings have high dimensionality, Principal Component Analysis (PCA) was applied to reduce dimensions before visualization.

PCA enabled:

* Visualization of clusters in two-dimensional space
* Better understanding of cluster separation
* Comparison of clustering quality across algorithms

---

## Evaluation Metrics

The clustering results were evaluated using:

### Silhouette Score

Measures how similar a sample is to its own cluster compared to other clusters.

Higher values indicate better cluster separation.

### Homogeneity Score

Measures whether each cluster contains data points belonging primarily to a single true class.

Higher values indicate purer clusters.

---

## Experimental Workflow

1. Load and preprocess news articles.
2. Generate semantic embeddings using Sentence Transformers.
3. Apply K-Means clustering.
4. Apply DBSCAN clustering.
5. Apply Hierarchical Clustering.
6. Reduce embedding dimensions using PCA.
7. Visualize clustering results.
8. Compute evaluation metrics.
9. Compare clustering performance.
10. Analyze representative samples from each cluster.

---

## Technologies Used

* Python
* NumPy
* Pandas
* Scikit-Learn
* Sentence Transformers
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Key AI Concepts

* Unsupervised Learning
* Text Representation Learning
* Semantic Embeddings
* Clustering
* Density-Based Learning
* Hierarchical Learning
* Dimensionality Reduction
* Natural Language Processing (NLP)

---

## Results

The project demonstrates how modern transformer-based embeddings significantly improve text clustering quality compared to traditional keyword-based approaches.

Comparative analysis of K-Means, DBSCAN, and Hierarchical Clustering highlights the trade-offs between cluster quality, scalability, and robustness to noise.

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Natural Language Processing pipelines
* Sentence Transformer embeddings
* Unsupervised machine learning
* Clustering evaluation techniques
* Dimensionality reduction and visualization
* Comparative analysis of machine learning algorithms

---

## Future Improvements

* Experiment with larger transformer models
* Apply UMAP or t-SNE for visualization
* Explore topic modeling approaches
* Fine-tune embeddings for domain-specific datasets
* Investigate advanced clustering methods such as HDBSCAN

---

Part of the Artificial Intelligence Course Projects Series.
