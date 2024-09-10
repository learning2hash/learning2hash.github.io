---
layout: default
title: Tutorial
comments: true
---

# Learning To Hash Tutorial

### Overview

In this tutorial, we dive into a [published learning to hash model](https://learning2hash.github.io/publications/moran2015agraph/) and compare its image retrieval performance against Locality Sensitive Hashing (LSH).

We will specifically explore the [Graph Regularized Hashing (GRH)](https://learning2hash.github.io/publications/moran2015agraph/) model by Moran and Lavrenko, a simple yet highly effective supervised hashing method for learning to hash. This model was later [extended for cross-modal hashing](https://dl.acm.org/doi/abs/10.1145/2766462.2767816).

### Preliminaries

The original MATLAB code for the GRH model by Moran and Lavrenko is available [here](https://github.com/sjmoran/GRH), but we’ll re-implement it in Python 3. We'll train the model on the CIFAR-10 dataset and evaluate its performance using precision at 10 and semantic nearest neighbor evaluation, comparing it to LSH.

To get started, set up a virtual environment:

```bash
python3 -m venv ./hashing_tutorial
source hashing_tutorial/bin/activate
pip3 install -r requirements.txt
```

Next, we retrieve and preprocess the CIFAR-10 dataset. We'll use pre-processed [GIST](http://people.csail.mit.edu/torralba/code/spatialenvelope/) features for this task.

```python
import scipy.io
import os
import requests

# Step 1: Download and save the pre-processed CIFAR-10 dataset
url='https://www.dropbox.com/s/875u1rkva9iffpj/Gist512CIFAR10.mat?dl=1'
response = requests.get(url)
with open(os.path.join("./", "Gist512CIFAR10.mat"), 'wb') as f:
    f.write(response.content)

# Step 2: Load the dataset
mat = scipy.io.loadmat('./Gist512CIFAR10.mat')

# Extract the data and class labels from the dataset
data = mat['X']
classes = mat['X_class']

# Step 3: Normalize the data to ensure it's ready for indexing
from sklearn.preprocessing import Normalizer
data = Normalizer(norm='l2').fit_transform(data)  # L2 normalization
data = data - data.mean(axis=0)  # Mean centering the data
```
The code above does three things:

1. Downloads the pre-processed CIFAR-10 dataset.
2. Loads the data into memory using scipy.io.loadmat.
3. Normalizes the data using L2 normalization and mean-centers it. This step is crucial to ensure consistent indexing later.

### Quick Start
If you want to skip ahead, you can run the entire tutorial using this command:

```python
python3 hashing_tutorial.py 
```

This will automatically download the dataset, train the GRH model, and evaluate its performance.

### Implementation (LSH)
Now, let's jump into Locality Sensitive Hashing (LSH). We'll generate 16 random hyperplanes (which translates into a 16-bit hashcode), and project the first image onto them to generate its LSH hashcode.

```python
import numpy as np

# Parameters for LSH
n_vectors = 32  # Number of random hyperplanes
dim = 512  # Dimensions in GIST features

# Step 1: Generate random hyperplanes
np.random.seed(0)
random_vectors = np.random.randn(dim, n_vectors)

# Step 2: Project the first image onto these hyperplanes to generate its hashcode
bin_indices_bits = data[0, :].dot(random_vectors) >= 0  # Binary hashcode based on sign

print(bin_indices_bits)
# Output: [False  True False  True False  True False False False False  True  True True False False False]
```

Here’s what’s happening:

We generate random hyperplanes and project the first image onto them. The result is a binary hashcode that represents the image. Any two images with the same hashcode will land in the same bucket in our hashtable.

Next, we’ll convert this binary hashcode into an integer for easier indexing.

```python
# https://wiki.python.org/moin/BitwiseOperators
# x << y is the same as multiplying x by 2 ** y
powers_of_two = 1 << np.arange(n_vectors - 1, -1, step=-1)
print(powers_of_two)
# [32768 16384  8192  4096  2048  1024   512   256   128    64    32    16    8     4     2     1]

bin_indices = bin_indices_bits.dot(powers_of_two)
print(bin_indices)
# 21560
```

We’ve now hashed the image into bucket 21560. Now let’s extend this process to the entire dataset.

```python
# Step 3: Hash the entire dataset
bin_indices_bits = data.dot(random_vectors) >= 0
print(bin_indices_bits.shape)
bin_indices = bin_indices_bits.dot(powers_of_two)  Should show (60000,) indicating 60,000 bin indices
bin_indices.shape
```
At this point, every image in the CIFAR-10 dataset has been hashed. Now, we will create a hashtable to group images that land in the same bucket and check for duplicates.

```python
from collections import defaultdict

# Step 4: Insert the images into a hashtable
table = defaultdict(list)
for idx, bin_index in enumerate(bin_indices):
	table[bin_index].append(idx)

# Step 5: Inspect the buckets with at least two colliding images
for bucket,images in table.items():
	if len(images)>1:
		print(images)
```

This code builds a hashtable where images that share the same hashcode (i.e., collide) are placed in the same bucket. Let's inspect some of these collisions to see how well LSH groups semantically similar images.

```python
# Inspect one of the buckets
# Example bucket: [39378, 39502, 41761, 42070, 50364]
print(classes.shape)
print(classes[:, 39378])  # Output: 7 (horse)
print(classes[:, 39502])  # Output: 8 (ship)
print(classes[:, 41761])  # Output: 8 (ship)
print(classes[:, 42070])  # Output: 4 (deer)
print(classes[:, 50364])  # Output: 9 (truck)
```

In this case, LSH performs poorly, as two different categories (horse, truck) collide in the same bucket. Let's inspect another bucket for better results.

```python
# We take this bucket and inspect the images:
# [42030, 42486, 43090, 47535, 50134, 50503]

print(classes.shape)
print(classes[:,42030])   # 4
print(classes[:,42486])   # 4
print(classes[:,43090])   # 4
print(classes[:,47535])   # 1
print(classes[:,50134])   # 1
print(classes[:,50503])   # 4
```

In this bucket, LSH performs better—grouping similar categories (mostly deer).

### Evaluation (LSH)

Next, let’s evaluate LSH more rigorously using precision at 10, which measures how many of the 10 nearest neighbors for a query share the same class label.

```python
# Step 1: Split the dataset into queries, training, and database sets
from sklearn.model_selection import train_test_split
np.random.seed(0)
data_temp, data_query, labels_temp, labels_query = train_test_split(data, classes[0,:], test_size=0.002, random_state=42)
data_database, data_train, labels_database, labels_train = train_test_split(data_temp, labels_temp[:], test_size=0.02, random_state=42)
```

This code will give 120 random queries that we will use alongside the LSH search index to find nearest neighbours. The database consists of 58682 images, and the training dataset contains 1198 images. 

![Dataset](./tutorial/lsh_dataset.png)

To prevent overfitting we maintain a held-out _database_ that we perform retrieval against using the set of 120 queries. The training dataset is used to learn any parameters and hyperparameters required by the models.

We now index the database portion with LSH creating our hashtable:

```python
bin_indices_bits = data_database.dot(random_vectors) >= 0
bin_indices = bin_indices_bits.dot(powers_of_two)

table = defaultdict(list)
for idx, bin_index in enumerate(bin_indices):
    table[bin_index].append(idx)
```

To search for nearest neighbours we apply a _Hamming radius based search_:

![Dataset](./tutorial/lsh_evaluation.png)

Hamming radius based search for a radius of zero is shown in Figure (b) in the above diagram (taken from the PhD thesis of [Sean Moran](https://era.ed.ac.uk/handle/1842/20390)). 

In a nutshell this search methodology works by also looking in the collding bin and nearby bins that different from the current bin by a certain number of bits, up to a specific maximum radius. We can use the _itertools combinations_ function to enumerate all the bins that differ from the current bin with respect to a certain number of bits, up to a maximum radius of 10 bits. As well as returning neighbours in the same bin, we also return neighbours from the nearby bins.

```python
from itertools import combinations
from sklearn.metrics.pairwise import pairwise_distances
import pandas as pd
import time

max_search_radius=10
topn=10
precision_history = {i: [] for i in range(max_search_radius+1)}
time_history = {i: [] for i in range(max_search_radius+1)}

for query_image, query_label in zip(data_query,labels_query):

    bin_index_bits = np.ravel(query_image.dot(random_vectors) >= 0)
    candidate_set = set()

    for search_radius in range(max_search_radius + 1):

        start = time.time()

        # Augment the candidate set with images from bins within the search radius
        n_vectors = bin_index_bits.shape[0]
        for different_bits in combinations(range(n_vectors), search_radius):
            index = list(different_bits)
            alternate_bits = bin_index_bits.copy()
            alternate_bits[index] = np.logical_not(alternate_bits[index])
            nearby_bin = alternate_bits.dot(powers_of_two)
            if nearby_bin in table:
                candidate_set.update(table[nearby_bin])

        # sort candidates by their true distances from the query
        candidate_list = list(candidate_set)
        if candidate_list:
            candidates = data_database[candidate_list[:]] 
            ground_truth = labels_database[candidate_list[:]]
            distance = pairwise_distances(candidates, query_image.reshape(1,-1), metric='cosine').flatten()
            distance_col = 'distance'
            nearest_neighbors = pd.DataFrame({'id': candidate_list, 'class': ground_truth, distance_col: distance}).sort_values(distance_col).reset_index(drop=True)
            candidate_set_labels = nearest_neighbors.sort_values(by=['distance'], ascending=True)['class'][:10]
            precision = list(candidate_set_labels).count(query_label) / topn
            precision_history[search_radius].append(precision)
        end = time.time()
        elapsed_time=end - start
        print(elapsed_time)
        time_history[search_radius].append(elapsed_time)

mean_time = [np.mean(time_history[i]) for i in range(len(time_history))]
print(mean_time)
mean_precision = [np.mean(precision_history[i]) for i in range(len(precision_history))]
print(mean_precision)
```	

The above code will produce a mean precision@10 of 0.30 for a radius of 2. As we increase the Hamming radius we increase the quality of the retrieval, at the expense of checking many more candidate nearest neighbours. This means that, on average, given a list of 10 returned images, 30% of those will be relevant to the query when we use a Hamming radius of 2. We will show how this can be boosted to 0.40 mean precision@10 by _learning the hashing hyperplanes_, rather than generating the hyperplanes randomly (as per LSH).

![LSH Precision@10](./tutorial/lsh_precision10.png)

As the Hamming radius increases from 0 to 10 we start retrieving more and more images from the database in our candidate set, and this leads to a corresponding sharp increase in the query time which will approach a standard brute force search time (~53 seconds) when the returned candidate set equals the entire database.

![LSH Time](./tutorial/lsh_time.png)

## Implementation (GRH)

We now investigate how learning the hyperplanes (i.e. learning to hash) can afford a much higher level or retrieval effectiveness. To recap we will be developing the supervised learning to hash model [Graph Regularised Hashing](https://learning2hash.github.io/publications/moran2015agraph/).

Our first step is to use the training dataset to construct an _adjacency matrix_ that GRH will use as its supervisory signal for learning the hashing hyperplanes. If two images share the same class label they have _adjacency_matrix[i,j]=1_ and _adjacency_matrix[i,j]=0_ otherwise. In Python we can construct this adjacency matrix from the class label vector:

```python
adjacency_matrix=np.equal.outer(labels_train, labels_train).astype(int)
row_sums = adjacency_matrix.sum(axis=1)
adjacency_matrix = adjacency_matrix / row_sums[:, np.newaxis]
```

We now implement the two-step [Graph Regularised Hashing (GRH)](https://learning2hash.github.io/publications/moran2015agraph/) model of Moran and Lavrenko, which is reminiscent of the expectation maximisation (EM) algorithm. The following slides are taken from the talk [here](https://www.slideshare.net/sjmoran1/graph-regularised-hashing-ecir15-talk).

![GRH](./tutorial/grh.png)

The first step is _Graph Regularisation_:

![GRH](./tutorial/grh_step1.png)

(The paper by Fernando Diaz - as referenced in the above [slidedeck](https://www.slideshare.net/sjmoran1/graph-regularised-hashing-ecir15-talk) - is very much worth a read and can be found [here](https://fernando.diaz.nyc/LSR-IR.pdf).)

In the first step the adjacency matrix is matrix multiplied by the hashcodes of the training dataset images. This multiplication has the effect of adjusting the hashcodes of the training database images such that semantically similar images have their hashcodes made more similar to each other. 

The second step is _Data Space Partitioning_:

![GRH](./tutorial/grh_step2.png)

In the second step those refined hashcodes are used to update the hyperplanes: to do this an SVM is learnt per hash bit using the bits as targets. GRH takes the LSH hyperplanes in _random_vector_ as an initialisation point and iteratively updates those hyperplanes so as to make them more effective for hashing. The entire GRH model is implemented below:

```python
n_iter=2   # number of iterations of GRH
alpha=0.5  # how much to update the hashcodes based on the supervisory information

for i in range(0,n_iter):

    bin_indices_bits = (data_train.dot(random_vectors) >= 0).astype(int)
    bin_indices_bits[bin_indices_bits==0]=-1
    bin_indices_bits_refined=np.matmul(adjacency_matrix,bin_indices_bits.astype(float))
    bin_indices_bits_refined=(bin_indices_bits_refined >=0).astype(int)
    bin_indices_bits_refined[bin_indices_bits_refined<=0]=-1

    bin_indices_bits = (0.25*bin_indices_bits_refined.astype(float) + 0.75*bin_indices_bits.astype(float))
    bin_indices_bits=(bin_indices_bits >=0).astype(int)
    bin_indices_bits[bin_indices_bits<=0]=-1

    grh_hyperplanes = random_vectors.copy()
    for j in range(0,n_vectors):
        if abs(sum(bin_indices_bits[:,j]))==data_train.shape[0]:
            # In case all bits are the same we generate a new random vector
            random_vector = np.random.randn(dim, 1)
            grh_hyperplanes[:,j]=random_vector[:,0]
        else:
            hyperplane=svclassifier.fit(data_train, bin_indices_bits[:,j]).coef_
            hyperplane=np.array(hyperplane)
            grh_hyperplanes[:,j]=hyperplane
    
    random_vectors = grh_hyperplanes.copy()
```
In the above code, we parametrise GRH with 2 iterations and an alpha of 0.25. The iterations parameter is the number of times we repeat the two steps of GRH i.e. hashcode refinement with the adjacency matrix followed by adjustment of the hyperplanes based on those updated hashcodes. After 2 iterations, the matrix _random_vectors_ contains a set of hyperplanes that have been refined - that is made more effective for hashing-based nearest neighbour search - based on the supervisory information in the training dataset as encapsulated in the adjacency matrix. We can use these hyperplanes as in the code at the start of this tutorial to evaluate their effectiveness via a hashtable bucket-based evaluation at various Hamming radii.

We now illustate how GRH works on a toy image retrieval example. The following diagram illustrates the nearest neighbour relationships on the toy example: denoted by the nodes and edges (edges connect semantic nearest neighbours). The LSH generated hashcodes are show alongside each image.

![GRH](./tutorial/grh_toy1.png)

The diagram below illustrates how the adjacency matrix is used to update the hashcodes, with the first bit of image _C_ flipping to a -1 to be more similar to the images above and to the left of it. In contrast, image _E_ has its second bit flipped to become more similar to the hashcodes from the images below and to the left of it.

![GRH](./tutorial/grh_toy2.png)

A hyperplane is then learnt for the first bit by using the first bit of every image's hashcode as the target. In this toy example (image below) a hyperplane partitions the data space horizontally, assigning images above the line a -1 in their first bit of their hashcode, and images below the line a 1 in their first bit of their hashcode.

![GRH](./tutorial/grh_toy3.png)

### Evaluation (GRH)

Now we have gained an understanding of how the GRH model works we will evaluate the GRH hashcodes using the same methodology as we did for LSH. We find an improved retrieval effectiveness, particularly at low Hamming radii:

![GRH Time](./tutorial/grh_precision10.png)

The benefits of GRH on this dataset an for a hashcode length of 16 bits can mostly be observed in the low Hamming radius regime (<=5). For example, at Hamming radius 0, GRH obtains ~0.25 mean precision@10, whereas LSH obtains ~0.1 mean precision@10. Query time for both methods are approximately similar (~0.5 seconds). The query time curve for GRH at increasing Hamming radii is shown below. As can be observed, for some Hamming radii, we pay at small price in terms of query time for the additional boost in effectiveness.

![GRH Time](./tutorial/grh_time.png)

### Conclusions

In this tutorial we use a Support Vector Machine (SVM) to learn the hyperplanes for GRH. We note that another benefit of GRH, aside from its simplicity and effectiveness, is that it is _agnostic to the learning algorithm_, and we can use a deep network if we wish to learn a more accurate data-space partitioning or a [passive aggressive classifier](https://www.youtube.com/watch?v=uxGDwyPWNkU) if we desire a light-weight learning method that can be adapted online e.g. in a streaming scenario. Lastly, in this tutorial we explored a single hashtable implementation of LSH and GRH and increased the number of relevant items retrieved using multiple buckets via a multi-probing mechanism. Other implementations of LSH would forgo the multi-probing of buckets within the same hashtable, and instead use multiple independent hashtables to find more relevant items.

### Contact & Feedback 

Any comments on this tutorial please contact the author [Sean Moran](https://sjmoran.github.io/). The code for the tutorial can be found [here](./tutorial/hashing_tutorial.py). The dependencies are located in [requirements.txt](./tutorial/requirements.txt) file. Feel free to contact [me](https://sjmoran.github.io/) with questions, suggestions or feedback. Copyright © [Sean Moran](https://sjmoran.github.io/) 2024. All opinions are my own.
