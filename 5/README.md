# Assignment CA5: Text Clustering & Unsupervised Learning (Using K-Means Clustering, DBSCAN, Hierarchical Clustering)

## Overview
This assignment implements **unsupervised learning techniques** for text clustering on a news article dataset. The goal is to group similar news articles into meaningful clusters using three different clustering algorithms: K-Means, DBSCAN, and Hierarchical Clustering. The project demonstrates the complete pipeline from text preprocessing to feature extraction, clustering, and evaluation.

## Learning Objectives
- Apply **unsupervised learning** algorithms for text classification
- Implement **text preprocessing** techniques (stemming, lemmatization, stopword removal)
- Extract meaningful features using **Sentence Transformers** (all-MiniLM-L6-v2)
- Compare and evaluate clustering algorithms using **silhouette scores** and **homogeneity scores**
- Visualize high-dimensional clusters using **PCA** dimensionality reduction
- Understand the strengths and weaknesses of different clustering approaches

## Key Concepts & Algorithms

### Clustering Algorithms Implemented
1. **K-Means Clustering**
   - Partition-based algorithm
   - Optimal K determined via **Elbow Method**
   - Tested with K values ranging from 3 to 8

2. **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**
   - Density-based clustering
   - Can identify arbitrary-shaped clusters
   - Handles noise points effectively
   - Parameter tuning: eps (0.5 - 3.0) and min_samples (5 - 34)

3. **Agglomerative Hierarchical Clustering**
   - Bottom-up hierarchical approach
   - Creates a hierarchy of clusters
   - Tested with K values from 3 to 8

### Feature Extraction
- **Sentence Transformers** (all-MiniLM-L6-v2)
- **TF-IDF Vectorization** (alternative approach)

### Dimensionality Reduction
- **PCA (Principal Component Analysis)** for 2D visualization

### Evaluation Metrics
- **Silhouette Score**: Measures cluster cohesion and separation (-1 to +1)
- **Homogeneity Score**: Compares clustering results with ground truth labels (when available)

## Dataset
- **Source**: Daily news articles in English from multiple newsgroups
- **Format**: CSV file with document texts
- **Content**: News articles from various categories
- **Size**: Multi-document dataset (exact size depends on dataset.csv)

## Implementation Details

### Tech Stack
- **Language**: Python 3.11
- **Libraries**:
  - `pandas` - Data manipulation
  - `numpy` - Numerical operations
  - `scikit-learn` - Clustering, PCA, metrics
  - `sentence-transformers` - Feature extraction
  - `nltk` - Text preprocessing (stopwords, stemming, lemmatization)
  - `matplotlib` - Visualization
- **Environment**: Jupyter Notebook / Google Colab

### Preprocessing Pipeline
1. Lowercasing text
2. Removing punctuation and special characters (`\n`, `\r`)
3. Stopword removal using NLTK's English stopword list
4. Stemming (Porter Stemmer)
5. Lemmatization (WordNet Lemmatizer)

### Feature Extraction Workflow
Raw Text → Preprocessing → Sentence Embeddings (384-dim) → PCA Reduction (2D) → Clustering


## Results & Evaluation

### Silhouette Scores Comparison
| Method | Silhouette Score | Observations |
|--------|------------------|--------------|
| K-Means | 0.091 | Best with K = 4 |
| DBSCAN | 0.041 | Sensitive to eps/min_samples |
| Hierarchical | 0.085 | Consistent performance |

### Cluster Quality Analysis
- Extracted 3 sample documents from each cluster for qualitative evaluation
- Visualized clusters in 2D space using PCA
- Compared cluster distributions across algorithms


### Prerequisites
pip install pandas numpy scikit-learn sentence-transformers nltk matplotlib

## **Challenges & Learnings**
1. Choosing optimal hyperparameters for DBSCAN (eps and min_samples)

2. Determining the right K for K-Means despite clear elbow

3. Handling noise points in DBSCAN clusters

## Key Takeaways
- K-Means: Works best for well-separated, spherical clusters

- DBSCAN: Excels at finding arbitrary-shaped clusters and handling noise

- Hierarchical: Provides insight into data structure but can be computationally expensive

- Feature quality (Sentence Embeddings) significantly impacts clustering performance

- PCA visualization helps intuit cluster quality but loses some information
