---
layout: default
title: Tutorial
comments: true
---
# Learning to Hash: A Step-by-Step Tutorial

### Overview

In this tutorial, we’ll explore a powerful learning-to-hash model and its application in image retrieval. Specifically, we will compare **Graph Regularized Hashing (GRH)**, a supervised hashing method, to **Locality Sensitive Hashing (LSH)** for image retrieval tasks.

We'll walk through the implementation of GRH, study its performance on the CIFAR-10 dataset, and benchmark it against LSH. GRH, initially introduced by Moran and Lavrenko, has since been extended to cross-modal hashing, which we'll touch on later.

### What You'll Learn

- Implementation of LSH and GRH in Python
- Performance comparison using the CIFAR-10 dataset
- Evaluation using precision at 10 and semantic nearest neighbor metrics

### Getting Started

#### Step 1: Set Up Your Environment

First, let's create a Python virtual environment for this project. This will keep your dependencies organized and isolated:

```bash
python3 -m venv ./hashing_tutorial
source hashing_tutorial/bin/activate
pip3 install -r requirements.txt
```

#### Step 2: Retrieve and Pre-process the Dataset

We'll use the **CIFAR-10 dataset** for our hashing experiments, but instead of raw images, we’ll use the GIST features to represent the images.

```python
import scipy.io
import os
import requests

url = 'https://www.dropbox.com/s/875u1rkva9iffpj/Gist512CIFAR10.mat?dl=1'
response = requests.get(url)
with open(os.path.join("./", "Gist512CIFAR10.mat"), 'wb') as f:
    f.write(response.content)

mat = scipy.io.loadmat('./Gist512CIFAR10.mat')
data = mat['X']
data = Normalizer(norm='l2').fit_transform(data)
data = data - data.mean(axis=0)
classes = mat['X_class']
```

This code downloads the CIFAR-10 dataset and pre-processes it into GIST features. Normalization and mean centering are critical steps before indexing.

If you want to skip the implementation steps, you can directly run the full code [here](./tutorial/hashing_tutorial.py):

```bash
python3 hashing_tutorial.py
```

### Locality Sensitive Hashing (LSH) Implementation

#### Step 3: Generate Hashcodes Using LSH

In LSH, we generate random hyperplanes to project images into hashcodes. Let’s start by projecting an image from the dataset:

```python
import numpy as np

num_classes = 10
n_vectors = 32
dim = 512

np.random.seed(0)
random_vectors = np.random.randn(dim, n_vectors)

bin_indices_bits = data[0, :].dot(random_vectors) >= 0
print(bin_indices_bits)
```

This will print out the boolean hashcode for the first image. Similar hashcodes will be assigned to images that are semantically similar, i.e., from the same class.

#### Step 4: Convert Boolean Hashcode to Integer Representation

We now convert the boolean representation of the hashcode into an integer:

```python
powers_of_two = 1 << np.arange(n_vectors - 1, -1, step=-1)
bin_indices = bin_indices_bits.dot(powers_of_two)
print(bin_indices)
```

This assigns an integer bin index for the image, which will determine its bucket in the hash table.

#### Step 5: Hash the Entire Dataset

Now, let’s hash the entire dataset using matrix operations:

```python
bin_indices_bits = data.dot(random_vectors) >= 0
bin_indices = bin_indices_bits.dot(powers_of_two)
```

This generates hashcodes for all 60,000 images in the CIFAR-10 dataset.

#### Step 6: Inspect the Hash Buckets

We can now create a hash table and inspect the buckets with more than one image:

```python
from collections import defaultdict

table = defaultdict(list)
for idx, bin_index in enumerate(bin_indices):
    table[bin_index].append(idx)

for bucket, images in table.items():
    if len(images) > 1:
        print(images)
```

This will print out the buckets that contain more than one image, allowing us to inspect collisions.

### Evaluating LSH

#### Step 7: Precision Evaluation with Hamming Radius Search

To evaluate the performance, we’ll use precision at 10 as our metric. This measures how many of the 10 nearest neighbors retrieved are semantically similar to the query image:

```python
from sklearn.model_selection import train_test_split

data_temp, data_query, labels_temp, labels_query = train_test_split(
    data, classes[0, :], test_size=0.002, random_state=42)
data_database, data_train, labels_database, labels_train = train_test_split(
    data_temp, labels_temp[:], test_size=0.02, random_state=42)
```

Here, we split the dataset into queries, training, and database sets.

Using Hamming radius-based search, we vary the radius to find more candidate neighbors:

```python
from itertools import combinations

max_search_radius = 10
precision_history = {i: [] for i in range(max_search_radius + 1)}

for query_image, query_label in zip(data_query, labels_query):
    bin_index_bits = np.ravel(query_image.dot(random_vectors) >= 0)
    candidate_set = set()

    for search_radius in range(max_search_radius + 1):
        n_vectors = bin_index_bits.shape[0]
        for different_bits in combinations(range(n_vectors), search_radius):
            alternate_bits = bin_index_bits.copy()
            alternate_bits[list(different_bits)] = np.logical_not(alternate_bits[list(different_bits)])
            nearby_bin = alternate_bits.dot(powers_of_two)
            if nearby_bin in table:
                candidate_set.update(table[nearby_bin])
```

This approach helps us retrieve images even from nearby hash bins, thus improving precision.

### Introducing Graph Regularized Hashing (GRH)

#### Step 8: Implement GRH

While LSH relies on random projections, **GRH** aims to learn the projections by utilizing label information. The key is constructing an adjacency matrix to serve as the supervisory signal:

```python
adjacency_matrix = np.equal.outer(labels_train, labels_train).astype(int)
row_sums = adjacency_matrix.sum(axis=1)
adjacency_matrix = adjacency_matrix / row_sums[:, np.newaxis]
```

In GRH, the hashcodes are refined iteratively through graph regularization and hyperplane updates, improving retrieval performance.

```python
n_iter = 2
for i in range(n_iter):
    bin_indices_bits = (data_train.dot(random_vectors) >= 0).astype(int)
    bin_indices_bits[bin_indices_bits == 0] = -1
    bin_indices_bits_refined = np.matmul(adjacency_matrix, bin_indices_bits.astype(float))
    bin_indices_bits_refined = (bin_indices_bits_refined >= 0).astype(int)
    bin_indices_bits_refined[bin_indices_bits_refined <= 0] = -1
```

This process adjusts hashcodes based on label similarity, improving semantic retrieval.

### GRH vs LSH: Performance Comparison

By learning the hash hyperplanes, GRH significantly improves retrieval performance over LSH, especially in low Hamming radius scenarios. As we increase the radius, GRH consistently outperforms LSH in terms of precision:

- **Precision@10 with GRH:** 0.25 at Hamming radius 0
- **Precision@10 with LSH:** 0.1 at Hamming radius 0

![LSH vs GRH Precision](./tutorial/lsh_precision10.png)

### Conclusion

In this tutorial, we demonstrated the differences between LSH and GRH for image retrieval. While LSH provides a fast, unsupervised hashing method, GRH offers higher retrieval accuracy by leveraging supervised learning.

Feel free to explore the full code [here](./tutorial/hashing_tutorial.py) and experiment with different datasets or hashing techniques!

**Feedback:** I’d love to hear your thoughts. Feel free to reach out [here](https://sjmoran.github.io/).
