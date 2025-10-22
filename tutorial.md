---
layout: default
title: Tutorial
comments: true
---
# Needles, Haystacks and Hashing: Smarter Search with AI

🔗 [Read on Medium](https://medium.com/@sean.j.moran/learning-to-hash-finding-the-needle-in-the-haystack-with-ai-24a15f85de0e)

## **How to find What You’re Looking For — Fast**

This article offers a hands-on introduction to machine learning approaches for nearest neighbour search, a field often called *Learning to Hash* or *Semantic Hashing*.

You’ll learn about:

* Why nearest neighbour search matters in computer science
* Approximate methods that dramatically speed up search
* Locality Sensitive Hashing (LSH), a widely used algorithm
* How machine learning can make neighbour search even more effective

👉 A fully annotated notebook with the experiments can be found on [**Google Colab**](https://colab.research.google.com/drive/1l-2wt1rozorVZLpxSQQks10CVC3iiBxS?usp=sharing).

<figure>
  <img src="https://miro.medium.com/v2/resize:fit:1024/1*JzcGGbGxBLwn7FuNeiQy7g.png" alt="" width="700">
</figure>

[Nearest neighbour search](https://en.wikipedia.org/wiki/Nearest_neighbor_search) is the core computer science task of finding the most similar data points to a query within a database. It’s a fundamental matching operation with wide applications across fields like bioinformatics, natural language processing (NLP), and computer vision.

It also powers today’s vector databases, the backbone of Retrieval-Augmented Generation (RAG) with large language models (LLMs).

Here are just a few places where nearest neighbour search and hashing shine:

* [**Code Search**:](https://arxiv.org/abs/2111.04473) Scalable source code search engines (e.g. using MinHash) for large repositories.
* [**Efficient Transformers**:](https://openreview.net/pdf?id=rkgNKkHtvB) Speeding up NLP models by applying LSH inside Transformer architectures.
* [**Social Media Monitoring**:](https://www.aclweb.org/anthology/P14-5007) Real-time event detection and tracking.
* [**Seismic Analysis**:](https://dawnd9.sites.stanford.edu/news/earthquake-hunting-efficient-time-series-similarity-search) Detecting earthquakes via time-series similarity search.
* [**Fraud Detection**:](https://www.uber.com/en-GB/blog/lsh/) Uber applies LSH to spot suspiciously similar rides.
* [**Audio Fingerprinting**:](https://santhoshhari.github.io/Locality-Sensitive-Hashing/) Matching snippets of audio to massive song databases (think *Shazam!*).
* [**Genomics**:](https://pubmed.ncbi.nlm.nih.gov/26006009/) Assembling genomes and matching gene expressions across large datasets.
* [**Image Retrieval**:](https://research.google/pubs/visualrank-applying-pagerank-to-large-scale-image-search/) Google combines LSH with PageRank to index billions of images.
* [**Malware Detection**:](https://media.kaspersky.com/en/enterprise-security/Kaspersky-Lab-Whitepaper-Machine-Learning.pdf) Anti-virus tools hash suspicious code snippets to flag known malware.

And the list goes on.

In this article, we’ll show how approximate nearest neighbour (ANN) methods make search dramatically faster. By using hashing, ANN achieves sub-linear retrieval times, meaning search grows much more slowly than dataset size. To see why this matters, compare linear vs. sub-linear growth: as your dataset scales, sub-linear time stays manageable, while linear time quickly becomes impractical.

The entire process is illustrated in the diagram below:

In this article, we explore a published *Learning to Hash* model and compare its image-retrieval performance to Locality Sensitive Hashing (LSH). In particular, we focus on [Graph Regularised Hashing (GRH)](https://learning2hash.github.io/publications/moran2015graph/) — a simple yet effective supervised hashing approach — later extended to [cross-modal hashing](https://dl.acm.org/doi/abs/10.1145/2766462.2767816) for retrieving across both images and text.

## **Learning to Hash — Optimising Retrieval Effectiveness with AI**

There are many ways to generate hash codes. Some methods are data-independent, relying on random functions with special properties, while more recent approaches learn the codes directly from data.

The best-known data-independent approach is Locality Sensitive Hashing (LSH), which has been widely written about. In this article, however, we focus on learning hash functions with AI — often called *Semantic Hashing* or *Learning to Hash*.

Our case study is Graph Regularised Hashing (GRH), an intuitive supervised hashing model that strikes a good balance between simplicity and effectiveness. We compare GRH against LSH on the benchmark task of image retrieval. GRH has also been extended to cross-modal hashing, enabling retrieval across both images and text.

There are many open-source Learning to Hash models available. I have chosen GRH because it clearly illustrates the core learning principles without requiring heavy mathematical detail. Other influential models include Supervised Hashing with Kernels and Deep Hashing. For a broader overview, see this excellent recent survey.

### Loading The Data

We’ll build our hashing model in Python 3, training it on the publicly available CIFAR-10 dataset. As a benchmark, we’ll compare retrieval effectiveness against Locality Sensitive Hashing (LSH) with Gaussian sign random projections, using two common evaluation measures: precision@10 and semantic nearest neighbour accuracy.

As with any project, the first step is to set up a Python virtual environment to hold the code and dependencies (a sample [requirements.txt](https://learning2hash.github.io/tutorial/requirements.txt) is provided here).

Let’s start by creating a clean Python environment for the tutorial. Run the following commands in your terminal:

```
# 1. Create a new virtual environment called 'hashing\_tutorial'  
python3 -m venv ./hashing\_tutorial  
  
# 2. Activate the environment  
source hashing\_tutorial/bin/activate  
  
# 3. Install the required packages  
pip3 install -r requirements.txt
```
💡 *Tip: If you ever want to leave the environment, just type deactivate.*

For this tutorial, we’ll use a pre-computed GIST descriptor version of CIFAR-10, stored in a .mat file. A .mat file is a MATLAB format commonly used to share pre-computed datasets in machine learning research. Don’t worry — we can easily load it in Python using scipy.io.

```
import os  
import requests  
import scipy.io  
from sklearn.preprocessing import Normalizer  
  
# 1. Download the dataset (stored as a .mat file)  
url = "https://www.dropbox.com/s/875u1rkva9iffpj/Gist512CIFAR10.mat?dl=1"  
response = requests.get(url)  
  
# Save the file locally  
with open("Gist512CIFAR10.mat", "wb") as f:  
 f.write(response.content)  
  
# 2. Load the .mat file  
mat = scipy.io.loadmat("Gist512CIFAR10.mat")  
  
# 3. Extract features (X) and classes (labels)  
data = mat["X"]  
classes = mat["X_class"]  
  
# 4. Pre-process the features  
# - L2 normalisation  
# - Zero-centering (subtracting mean)  
data = Normalizer(norm="l2").fit_transform(data)  
data = data - data.mean(axis=0)
```
At this point, we have:

* **data** → a normalised feature matrix (one row per CIFAR-10 image)
* **classes** → the corresponding class labels

These are now ready to use for training and evaluating our hashing model.

The code above downloads the CIFAR-10 dataset (pre-processed into GIST features) and saves it to your working directory. To make sure similarity comparisons are meaningful, we L2-normalise and mean-centre the data before indexing.

👉 If you’d like to skip the step-by-step walkthrough, you can run the entire pipeline in one go:

```
python3 hashing_tutorial.py
```
This script will:

1. Download and prepare the CIFAR-10 dataset
2. Train the Graph Regularised Hashing (GRH) model
3. Evaluate retrieval effectiveness on the CIFAR-10 images

👉 A full notebook with the experiments can also be found on [Google Colab](https://colab.research.google.com/drive/1l-2wt1rozorVZLpxSQQks10CVC3iiBxS?usp=sharing).

## Implementation — Locality Sensitive Hashing (LSH)

We’ll start with Gaussian sign random projections: project each vector onto random hyperplanes and take the sign to get a binary hash (1 bit per hyperplane). With 16 hyperplanes, we get a 16-bit hash.

```
import numpy as np  
from collections import defaultdict  
  
# --- Config ---  
n_bits = 16 # 16 hyperplanes → 16-bit hash  
dim = data.shape[1] # should be 512 for GIST512  
rng = np.random.default_rng(0) # reproducibility  
  
# --- Random hyperplanes (Gaussian) ---  
random_vectors = rng.standard_normal((dim, n_bits)) # shape: (512, 16)  
  
# --- Hash a single image (example) ---  
x0 = data[0] # one CIFAR-10 image vector  
bits0 = (x0 @ random_vectors) >= 0 # boolean hash bits  
print("hash bits (bool):", bits0)  
print("hash bits (0/1):", bits0.astype(int))  
# e.g. [False True False True ...]The last line of code prints out the hashcode assigned to this image. Images with the exact same hashcode will collide in the same hashtable bucket. We would like these colliding images to be semantically similar, that is, to have the same class label.
```
Convert the boolean bits to a single bucket id (an integer) so we can index a hash table:

```
# Bits → integer bucket id (big-endian)  
powers_of_two = (1 << np.arange(n_bits - 1, -1, -1, dtype=np.uint64))  
bucket0 = int(bits0.dot(powers_of_two))  
print("bucket id:", bucket0)
```
Now hash the entire dataset and build the hash table:

```
# --- Hash all images ---  
bit_matrix = (data @ random_vectors) >= 0 # shape: (N, 16)  
bucket_ids = bit_matrix.dot(powers_of_two).astype(np.uint64) # shape: (N,)  
  
# --- Build hash table: bucket_id -> list of indices ---  
table = defaultdict(list)  
for idx, b in enumerate(bucket_ids):  
 table[int(b)].append(idx)  
  
# Quick stats  
N = data.shape[0]  
bucket_sizes = np.array([len(v) for v in table.values()])  
print(f"N images: {N}, unique buckets: {len(table)}")  
print(f"Avg bucket size: {bucket_sizes.mean():.2f}, max collisions in a bucket: {bucket_sizes.max()}")
```
Inspect a colliding bucket to see label consistency (good hashing ⇒ many items share the same class):

```
labels = classes.ravel() # flatten to shape (N,)  
  
# Pick the first bucket with >= 2 items  
example_bucket, example_idxs = next((b, idxs) for b, idxs in table.items() if len(idxs) >= 2)  
print("example bucket:", example_bucket)  
print("indices:", example_idxs)  
print("labels:", labels[example_idxs])  
  
from collections import Counter  
print("label counts:", Counter(labels[example_idxs]))
```
**What to expect:**

* Some buckets will be “clean” (mostly one class) — great!
* Others will be mixed (several classes) — that’s the approximation trade-off with basic LSH.

```
example bucket: 21560  
indices: [39378, 39502, 41761, 42070, 50364]  
labels: [7 8 8 4 9]  
label counts: Counter({8: 2, 7: 1, 4: 1, 9: 1})
```
Here we see that this bucket is mixed: only two images (label 8, *ship*) are semantically related, while the rest are from other classes.

```
indices: [42030, 42486, 43090, 47535, 50134, 50503]  
labels: [4 4 4 1 1 4]  
label counts: Counter({4: 4, 1: 2})
```
This time, LSH does much better: most of the colliding images belong to the same class (4 = *deer*), with just a couple of outliers (1 = *automobile*).

Next, we’ll move from spot-checks to a quantitative evaluation (e.g., *precision@10*) so we can compare LSH to a learned hashing model like Graph Regularised Hashing (GRH).

### Evaluation — Locality Sensitive Hashing (LSH)

To measure how well LSH works, we’ll use the precision@10 metric while varying the number of hash bits. Precision@10 tells us: *of the top 10 retrieved neighbours for a query, how many share the same class label?*

First, we split CIFAR-10 into three parts:

* **Queries** — used for retrieval
* **Training set** — to learn parameters (if needed)
* **Database** — the collection we search over

```
from sklearn.model_selection import train_test_split  
  
np.random.seed(0)  
  
# Split into queries and the rest  
data_temp, data_query, labels_temp, labels_query = train_test_split(  
 data, classes[0, :], test_size=0.002, random_state=42  
)  
  
# Split the remainder into database and training  
data_database, data_train, labels_database, labels_train = train_test_split(  
 data_temp, labels_temp, test_size=0.02, random_state=42  
)
```
This gives us:

* **120 queries** for testing retrieval
* **58,682 images** in the database
* **1,198 images** for training

Next, we index the database with LSH, building the hash table:

```
# Step 1: Generate binary hash codes for each image in the database  
bin_indices_bits = data_database.dot(random_vectors) >= 0 # shape: (N, n_bits)  
  
# Step 2: Convert each binary code into an integer bucket ID  
bin_indices = bin_indices_bits.dot(powers_of_two)  
  
# Step 3: Build the hash table (bucket_id -> list of image indices)  
from collections import defaultdict  
table = defaultdict(list)  
for idx, bucket_id in enumerate(bin_indices):  
 table[bucket_id].append(idx)
```
**What this does:**

* Each image in the database is assigned a binary hash code (bin_indices_bits).
* That binary code is converted into a unique integer ID (bin_indices) so it can be used as a hash bucket key.
* We then build a hash table (table) that groups together all images with the same bucket ID.

Now, similar images should “collide” in the same bucket — making nearest neighbour search much faster

With the index in place, we can now search for nearest neighbours using a Hamming radius search:

In simple terms, the idea is:

* Start with the query’s hash bin.
* Also check nearby bins whose hash codes differ by up to *r* bits.
* The maximum radius *r* controls how far we search.

In Python, we can use itertools.combinations to enumerate all possible bit flips. For example, with a maximum radius of 10, we explore bins that differ from the query’s bin by 1, 2, …, up to 10 bits.

This way, we return not only the neighbours in the same bin, but also those in nearby bins, improving recall.

```
from itertools import combinations  
from collections import defaultdict  
from typing import Dict, Iterable, List, Tuple  
  
import numpy as np  
import pandas as pd  
from sklearn.metrics.pairwise import pairwise\_distances  
import time  
  
  
def evaluate_multiprobe_lsh(  
 data_query: np.ndarray,  
 labels_query: np.ndarray,  
 data_database: np.ndarray,  
 labels_database: np.ndarray,  
 random_vectors: np.ndarray,  
 powers_of_two: np.ndarray,  
 buckets: Dict[int, List[int]],  
 *,  
 max_search_radius: int = 10,  
 topk: int = 10,  
 metric: str = "cosine",  
) -> Tuple[pd.DataFrame, pd.DataFrame]:  
 """  
 Evaluate multi-probe LSH by sweeping Hamming search radius (0..max_search_radius).  
  
 Args:  
 data_query: (Q, D) query vectors.  
 labels_query: (Q,) labels for queries.  
 data_database: (N, D) database vectors.  
 labels_database: (N,) labels for database items (same order as data_database).  
 random_vectors: (D, B) projection matrix for hashing to B bits.  
 powers_of_two: (B,) array mapping bit-vectors -> integer bucket ids via dot product.  
 buckets: dict mapping bucket_id -> list of database indices in that bucket.  
 max_search_radius: maximum Hamming radius to probe.  
 topk: precision@k cutoff.  
 metric: distance metric used for re-ranking (e.g., "cosine").  
  
 Returns:  
 (mean_time_df, mean_precision_df)  
 mean_time_df: columns: ["radius", "mean_time_seconds"]  
 mean_precision_df: columns: ["radius", "mean_precision_at_k"]  
 """  
 # History accumulators  
 time_history: Dict[int, List[float]] = defaultdict(list)  
 precision_history: Dict[int, List[float]] = defaultdict(list)  
  
 # Precompute once: number of hash bits  
 # We generate the query hash as a boolean vector (True = 1, False = 0).  
 B = random_vectors.shape[1]  
  
 for q_vec, q_label in zip(data_query, labels_query):  
 # Compute binary hash bits for the query  
 # bin_bits: shape (B,), dtype=bool  
 bin_bits = np.ravel((q_vec @ random_vectors) >= 0)  
  
 # Candidate set grows monotonically with radius (multi-probe)  
 candidate_set: set = set()  
  
 for radius in range(max_search_radius + 1):  
 start = time.time()  
  
 # Probe all buckets within Hamming distance == radius  
 # Note: combinations(range(B), radius) can be large for big B and radius.  
 # Keep max_search_radius modest or add a cap if needed.  
 for flip_idx in combinations(range(B), radius):  
 alt_bits = bin_bits.copy()  
 alt_bits[list(flip_idx)] = ~alt_bits[list(flip_idx)]  
 bucket_id = int(alt_bits.dot(powers_of_two))  
 if bucket_id in buckets:  
 candidate_set.update(buckets[bucket_id])  
  
 # Re-rank candidates by true distance and compute precision@k  
 if candidate_set:  
 cand_idx = list(candidate_set)  
 cand_vecs = data_database[cand_idx]  
 cand_labels = labels_database[cand_idx]  
  
 # Distance to the single query vector (reshape to (1, D))  
 dists = pairwise_distances(  
 cand_vecs, q_vec.reshape(1, -1), metric=metric  
 ).ravel()  
  
 # Build a small dataframe for readability   
 nearest = (  
 pd.DataFrame(  
 {"id": cand_idx, "label": cand_labels, "distance": dists}  
 )  
 .sort_values("distance", ascending=True)  
 .reset_index(drop=True)  
 )  
  
 top_labels = nearest["label"].head(topk).tolist()  
 precision_at_k = top_labels.count(q_label) / float(topk)  
 precision_history[radius].append(precision_at_k)  
 else:  
 # No candidates yet at this radius  
 precision_history[radius].append(0.0)  
  
 elapsed = time.time() - start  
 time_history[radius].append(elapsed)  
  
 # Aggregate across queries  
 mean_time = pd.DataFrame(  
 {"radius": list(range(max_search_radius + 1)),  
 "mean_time_seconds": [np.mean(time_history[r]) for r in range(max_search_radius + 1)]}  
 )  
  
 mean_precision = pd.DataFrame(  
 {"radius": list(range(max_search_radius + 1)),  
 "mean_precision_at_k": [np.mean(precision_history[r]) for r in range(max_search_radius + 1)]}  
 )  
  
 return mean_time, mean_precision
```
With a Hamming radius of 0, the above code yields a mean precision@10 of around 0.08. In practice, this means that out of the 10 retrieved images, fewer than 1 on average is relevant to the query.

As we increase the Hamming radius, retrieval quality improves — but at the cost of searching through many more candidate neighbours.

## Implementation — Graph Regularised Hashing (GRH)

We now move from random hyperplanes (LSH) to learned hyperplanes. This is the essence of *Learning to Hash*: by training the hyperplanes, we can achieve much higher retrieval effectiveness. Our focus will be on the Graph Regularised Hashing (GRH) model, a supervised learning-to-hash approach.

To make the workings of GRH concrete, we’ll walk through a small running example throughout this section.

The figure above shows a toy dataset of cars and tigers. Each image is represented as a node in the graph, and edges connect semantic nearest neighbours (e.g. cars are linked to other cars, tigers to other tigers). The binary codes shown beside each image are the starting point, produced by Locality Sensitive Hashing (LSH). At this stage the codes are still noisy and random, but GRH will refine them over iterations so that similar images cluster together in hash space.

GRH learns from a supervisory signal: an adjacency matrix that encodes which images are semantically related. If two images share the same class label, we set adjacency_matrix[i, j] = 1; otherwise, it’s 0. Normalising by row ensures each row sums to 1.

```
# Construct adjacency matrix from training labels  
adjacency_matrix = np.equal.outer(labels_train, labels_train).astype(int)  
row_sums = adjacency_matrix.sum(axis=1)  
adjacency_matrix = adjacency_matrix / row_sums[:, np.newaxis]
```
### **Learning the hash functions**

The GRH model (Moran & Lavrenko) is reminiscent of the Expectation-Maximisation (EM) algorithm:

* **Step 1:** Estimate hash codes given the current hyperplanes
* **Step 2:** Update the hyperplanes to better preserve semantic similarity

Slides from the original GRH talk (linked [here](https://www.slideshare.net/slideshow/graph-regularised-hashing-ecir15-talk/46413512)) walk through the details of this iterative process.

**Step A: Graph Regularisation**

GRH encourages similar points in the data graph to stay close in the hash space:

* **S** is the similarity graph
* **D** is the degree matrix
* ɑ balances between the previous codes (**Lₘ**) and the initial embedding (**L₀**)

The first step in GRH uses the similarity graph of the data to refine the hash codes. Concretely, it multiplies the adjacency matrix (which captures which images are similar) by the current hash codes of the training images.

After the first round of graph regularisation, the hash codes are updated to **L₁.** This is done by multiplying the adjacency-weighted structure of the graph with the initial codes **L₀:**

In the second step, GRH turns the refined hash codes into actual decision boundaries in the data space. For each hash bit k = 1 … K, it learns a **linear classifier** (think of a Support Vector Machine, SVM) that splits the data into two halves:

Once the hash codes have been refined in Step A, GRH improves the way data is split in hash space. For each hash bit, it trains a Support Vector Machine (SVM), using the bit values as the training labels. Instead of sticking with the random hyperplanes from Locality Sensitive Hashing (LSH), GRH starts with them as an initial guess and then iteratively sharpens these hyperplanes. Over time, the boundaries become better at separating semantically similar images (which should end up in the same bucket) from dissimilar ones (which should be pushed apart).

Each hyperplane corresponds to one hash bit. As shown in the figure below, this hyperplane for bit position 1 divides the data into two regions: the negative half-space (-1) above the line and the positive half-space (+1) below it. Every image receives its bit assignment based on which side of the hyperplane it falls.

1. **Graph Regularisation** — refine the binary codes by encouraging similar points in the graph to stay close in hash space.
2. **Data-Space Partitioning** — update the hyperplanes by training an SVM for each hash bit.

These steps alternate for a fixed number of iterations, starting from random hyperplanes (as in LSH) and gradually improving them into semantically meaningful hash functions.

Here’s the full iterative process:

```
from sklearn.svm import LinearSVC  
  
n_iter = 2 # number of GRH iterations  
alpha = 0.5 # weighting for supervision vs. original codes  
  
for i in range(n_iter):  
 # --- Step 1: Generate initial binary codes with current hyperplanes ---  
 bin_indices_bits = (data_train.dot(random_vectors) >= 0).astype(int)  
 bin_indices_bits[bin_indices_bits == 0] = -1 # use -1/1 convention  
  
 # --- Step 2: Refine codes using the adjacency matrix (supervision) ---  
 refined_bits = adjacency_matrix @ bin_indices_bits.astype(float)  
 refined_bits = np.where(refined_bits >= 0, 1, -1)  
  
 # Blend original codes with refined ones (alpha controls weighting)  
 bin_indices_bits = (alpha * refined_bits + (1 - alpha) * bin_indices_bits).astype(float)  
 bin_indices_bits = np.where(bin_indices_bits >= 0, 1, -1)  
  
 # --- Step 3: Update hyperplanes with SVMs ---  
 grh_hyperplanes = random_vectors.copy()  
 for j in range(n_vectors):  
 # Edge case: if all bits are identical, reset hyperplane randomly  
 if abs(bin_indices_bits[:, j].sum()) == data_train.shape[0]:  
 grh_hyperplanes[:, j] = np.random.randn(dim)  
 else:  
 svm = LinearSVC(C=1.0, max_iter=1000)  
 svm.fit(data_train, bin_indices\_bits[:, j])  
 grh_hyperplanes[:, j] = svm.coef_.ravel()  
  
 # Update random_vectors for the next iteration  
 random_vectors = grh_hyperplanes.copy()
```
In this implementation, I’ve set GRH with *n_iter = 2* and *alpha = 0.25*.

Iterations (*n_iter*) control how many times we repeat the two GRH steps:

1. Refine hash codes with the adjacency matrix
2. Update hyperplanes using those refined codes

After two iterations, the *random_vectors* matrix contains refined hyperplanes — tuned to preserve semantic similarity from the training data (via the adjacency matrix). These hyperplanes can now be used in the same way as before (with a hash table and Hamming radius search) to evaluate retrieval performance.

### Evaluation — Graph Regularised Hashing (GRH)

With a solid grasp of how GRH works, we can now evaluate its hash codes using the same methodology as LSH.

The results show a clear improvement in retrieval effectiveness, especially at lower Hamming radii, where GRH is able to capture semantic similarity much better than random hyperplanes.

* At radius 0, GRH achieves ~0.25 mean precision@10, compared to only ~0.1 for LSH.
* Importantly, query times remain similar for both methods (~0.5 seconds at low radii).

The curve below shows GRH query times as the Hamming radius increases. In some cases, we pay a small cost in speed for the significant boost in retrieval effectiveness — a worthwhile trade-off in practice.

In this tutorial, we implemented a data-independent approach for hashing-based nearest neighbour search — Locality Sensitive Hashing (LSH) — and evaluated its quality and speed.

To improve retrieval effectiveness, we introduced *Learning to Hash*, where machine learning is used to train better hyperplanes. Using Graph Regularised Hashing (GRH), we demonstrated clear improvements on an image retrieval task.

GRH learns its hyperplanes with Support Vector Machines (SVMs), but is not tied to any specific learner. In practice, this means you could swap in a deep neural network for more accurate partitions, or a lightweight passive-aggressive classifier for fast, online adaptation in streaming scenarios.

In this article, we focused on a single-hashtable implementation of LSH and GRH, and boosted retrieval further with multi-probing (searching nearby buckets). An alternative 

*Disclaimer: The views and opinions expressed in this article are my own and do not represent those of my employer or any affiliated organizations. The content is based on personal experience and reflection, and should not be taken as professional or academic advice.*

## 📚 Further Learning

If you’d like to dive deeper into the theory and practice of hashing for similarity search and large-scale learning, here are some foundational and advanced resources:

* [**Moses Charikar — Similarity Estimation Techniques from Rounding Algorithms:**](https://www.cs.princeton.edu/courses/archive/spr04/cos598B/bib/CharikarEstim.pdf) The seminal paper that introduced SimHash, a cornerstone in locality-sensitive hashing and similarity search.
* [**Anand Rajaraman & Jeffrey Ullman — Mining of Massive Datasets:**](http://www.mmds.org) A freely available textbook covering large-scale data mining techniques, including LSH and approximate nearest neighbour search.
* [**Sean Moran & Victor Lavrenko — Graph Regularised Hashing:**](https://link.springer.com/chapter/10.1007/978-3-319-16354-3_15) A method that incorporates graph structure into the hashing process, improving similarity preservation for information retrieval tasks.
* [**Wei Liu, Jun Wang, Rongrong Ji, Yu-Gang Jiang & Shih-Fu Chang — Supervised Hashing with Kernels:**](https://ieeexplore.ieee.org/abstract/document/6247912/footnotes#footnotes) A supervised approach that leverages kernel methods to generate compact binary codes for efficient retrieval.
* [**Wu-Jun Li, Sheng Wang & Wang-Cheng Kang — Feature Learning Based Deep Supervised Hashing with Pairwise Labels:**](https://arxiv.org/abs/1511.03855)Early work that combines feature learning with supervised hashing, paving the way for deep learning methods in similarity search.
* [**Xiao Luo, Haixin Wang, Daqing Wu, Chong Chen, Minghua Deng, Jianqiang Huang & Xian-Sheng Hua — A Survey on Deep Hashing Methods:**](https://arxiv.org/abs/2003.03369) A comprehensive survey that reviews advances in deep hashing, providing an overview of key architectures, methods, and applications.
* [**Awesome Learning to Hash:**](https://learning2hash.github.io) For readers eager to explore Learning to Hash in more depth, *Awesome Learning to Hash* is a curated, and regularly updated resource. Access to over 3,000 key papers, all organised by topic, method, and application domain

👉 These readings will give you a solid path from the theoretical underpinnings of hashing, through classical supervised methods, and into the modern era of deep hashing research and applications.
