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
# x << y (bitwise left shift) is the same as multiplying x by 2 ** y.
# This is a bitwise operation that effectively gives us the powers of 2.

# Create an array where each entry is a power of 2, starting from 2^(n_vectors-1) down to 2^0
# 'n_vectors' represents the number of dimensions (or bits) in the binary hash codes.
# This array is used to convert binary numbers (hash codes) into decimal (integer) values.
powers_of_two = 1 << np.arange(n_vectors - 1, -1, step=-1)  
# Example: If n_vectors is 16, this creates an array like [32768, 16384, 8192, ..., 2, 1], corresponding to powers of 2.
print(powers_of_two)  # Print the array of powers of 2

# Sample output:
# [32768 16384  8192  4096  2048  1024   512   256   128    64    32    16    8     4     2     1]

# Convert binary hash codes into decimal (bin indices)
# 'bin_indices_bits' contains the binary hash codes as arrays of 1s and 0s (or True/False).
# By doing a dot product between 'bin_indices_bits' and 'powers_of_two', we convert each binary number into a unique integer.
# Each binary code is interpreted as a binary number, and 'powers_of_two' acts as the weights for each bit.
bin_indices = bin_indices_bits.dot(powers_of_two)

# Example: If bin_indices_bits contains a binary code like [1, 0, 1, 1], this will convert it into its decimal equivalent (e.g., 21560).
print(bin_indices)  # Print the resulting bin index (the integer representation of the binary hash code)

# Sample output:
# 21560  # This represents the decimal equivalent of a specific binary hash code.
```

We’ve now hashed the image into bucket 21560. Now let’s extend this process to the entire dataset.

```python
# Step 3: Hash the entire dataset

# Compute binary hash codes for the dataset using random hyperplanes
# For each data point in 'data', compute the dot product with 'random_vectors' (random hyperplanes).
# If the dot product is >= 0, assign a binary value of 1, otherwise 0 (True/False).
bin_indices_bits = data.dot(random_vectors) >= 0  # This generates a binary code (True/False) for each data point.

# Print the shape of 'bin_indices_bits' to verify the dimensions of the binary hash codes
print(bin_indices_bits.shape)  # Should print something like (60000, n_vectors) where '60000' is the number of data points.

# Convert the binary hash codes into bin indices (integer values)
# The binary hash code is converted into an integer using 'powers_of_two'.
# This process maps each binary code to a unique bin index.
bin_indices = bin_indices_bits.dot(powers_of_two)  # Each binary code is converted into a unique integer (bin index).

# The expected output shape of 'bin_indices' should be (60000,), meaning there are 60,000 bin indices,
# one for each data point in the dataset.
bin_indices.shape  # Check the shape of the resulting bin indices array.

```
At this point, every image in the CIFAR-10 dataset has been hashed. Now, we will create a hashtable to group images that land in the same bucket and check for duplicates.

```python
from collections import defaultdict  # Import defaultdict to create a hash table where each bin index stores a list of image indices

# Step 4: Insert the images into a hash table based on their bin indices
table = defaultdict(list)  # Initialize a hash table where each bin (key) stores a list of image indices (values)
for idx, bin_index in enumerate(bin_indices):
    # For each image, append its index to the corresponding bin in the hash table
    table[bin_index].append(idx)  # 'bin_index' is the key (bin), 'idx' is the image index being stored

# Step 5: Inspect the buckets (bins) that have at least two colliding images
for bucket, images in table.items():
    if len(images) > 1:  # If a bucket contains more than one image (collision)
        print(images)  # Print the list of image indices that collide (i.e., are hashed to the same bin)

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
# Step 1: Split the dataset into query, training, and database sets for nearest neighbor search

from sklearn.model_selection import train_test_split  # Import train_test_split to split the dataset
np.random.seed(0)  # Set a seed for reproducibility

# First split: Separate out a small portion of the data to serve as the query set
# 'data' contains the entire dataset, and 'classes[0, :]' contains the corresponding labels
# We split off 0.2% of the data for queries (test_size=0.002)
data_temp, data_query, labels_temp, labels_query = train_test_split(
    data, classes[0, :], test_size=0.002, random_state=42
)

# Second split: From the remaining data, split into the database set and the training set
# We split off 2% of the remaining data for training, leaving the rest for the database
data_database, data_train, labels_database, labels_train = train_test_split(
    data_temp, labels_temp[:], test_size=0.02, random_state=42
)

```

This code will give 120 random queries that we will use alongside the LSH search index to find nearest neighbours. The database consists of 58682 images, and the training dataset contains 1198 images. 

![Dataset](./tutorial/lsh_dataset.png)

To prevent overfitting we maintain a held-out _database_ that we perform retrieval against using the set of 120 queries. The training dataset is used to learn any parameters and hyperparameters required by the models.

We now index the database portion with LSH creating our hashtable:

```python
# Step 1: Compute binary hash codes for the entire database
# Project the data points onto the random hyperplanes (random_vectors) and convert to binary hash codes
# If the dot product of a data point and a hyperplane is >= 0, assign a value of 1, else 0
bin_indices_bits = data_database.dot(random_vectors) >= 0  # Each data point gets a binary code (True/False)

# Step 2: Convert binary hash codes to bin indices (integer representation)
# The binary code is treated as bits and converted to an integer using powers_of_two
bin_indices = bin_indices_bits.dot(powers_of_two)  # Each binary code is converted into an integer index

# Step 3: Build the hash table
table = defaultdict(list)  # Initialize the hash table as a defaultdict of lists

# Step 4: Populate the hash table with data points
for idx, bin_index in enumerate(bin_indices):
    table[bin_index].append(idx)  # For each data point, add its index to the corresponding bin in the hash table
```

To search for nearest neighbours we apply a _Hamming radius based search_:

![Dataset](./tutorial/lsh_evaluation.png)

Hamming radius based search for a radius of zero is shown in Figure (b) in the above diagram (taken from the PhD thesis of [Sean Moran](https://era.ed.ac.uk/handle/1842/20390)). 

In a nutshell this search methodology works by also looking in the collding bin and nearby bins that different from the current bin by a certain number of bits, up to a specific maximum radius. We can use the _itertools combinations_ function to enumerate all the bins that differ from the current bin with respect to a certain number of bits, up to a maximum radius of 10 bits. As well as returning neighbours in the same bin, we also return neighbours from the nearby bins.

```python
from itertools import combinations  # Used to generate combinations of bit positions for Hamming radius search
from sklearn.metrics.pairwise import pairwise_distances  # Used to compute distances between query and candidates
import pandas as pd  # Pandas for managing candidate neighbors and their labels/distances
import time  # For measuring the time spent on each search radius

# Hamming radius-based search for nearest neighbors
max_search_radius = 10  # Maximum Hamming radius to consider in the search
topn = 10  # We will evaluate precision@10 (how many correct results are in the top 10 nearest neighbors)
precision_history = {i: [] for i in range(max_search_radius + 1)}  # Dictionary to track precision at each radius
time_history = {i: [] for i in range(max_search_radius + 1)}  # Dictionary to track time taken for each radius

# Iterate over each query image and its corresponding label
for query_image, query_label in zip(data_query, labels_query):
    
    # Step 1: Compute binary hash code for the query image using random hyperplanes
    bin_index_bits = np.ravel(query_image.dot(random_vectors) >= 0)  # Convert query image to binary hash code
    candidate_set = set()  # Set to collect candidate neighbors found within the Hamming radius

    # Step 2: Search over various Hamming radii (from 0 to max_search_radius)
    for search_radius in range(max_search_radius + 1):
        start = time.time()  # Start timer to measure the search time for this radius

        # Search for nearby bins by flipping bits up to 'search_radius' positions
        for different_bits in combinations(range(n_vectors), search_radius):
            alternate_bits = bin_index_bits.copy()  # Copy original binary hash code of the query
            alternate_bits[list(different_bits)] = np.logical_not(alternate_bits[list(different_bits)])  # Flip bits at positions defined by 'different_bits'
            nearby_bin = alternate_bits.dot(powers_of_two)  # Convert binary code to an integer to look up in the hash table
            if nearby_bin in table:  # Check if the altered binary hash corresponds to a bin in the hash table
                candidate_set.update(table[nearby_bin])  # Add the candidates from this bin to the candidate set

        # Step 3: If candidate neighbors are found, rank them by their actual distances (using cosine similarity)
        if candidate_set:
            candidates = data_database[list(candidate_set)]  # Retrieve the actual data points for the candidates
            ground_truth = labels_database[list(candidate_set)]  # Retrieve the true labels for the candidates
            distances = pairwise_distances(candidates, query_image.reshape(1,-1), metric='cosine').flatten()  # Compute cosine distances between candidates and query
            nearest_neighbors = pd.DataFrame({'id': list(candidate_set), 'class': ground_truth, 'distance': distances})  # Store candidates and their distances
            # Sort candidates by their distances and take the top 10 closest
            candidate_set_labels = nearest_neighbors.sort_values('distance').reset_index(drop=True)['class'][:10]
            # Calculate precision@10 (how many of the top 10 closest candidates have the correct label)
            precision = list(candidate_set_labels).count(query_label) / topn
            precision_history[search_radius].append(precision)  # Store the precision for this radius

        time_history[search_radius].append(time.time() - start)  # Store the time taken for this search radius

# Step 4: Calculate average precision and time across all query images for each search radius
mean_time = [np.mean(time_history[i]) for i in range(len(time_history))]  # Compute average time for each search radius
mean_precision = [np.mean(precision_history[i]) for i in range(len(precision_history))]  # Compute average precision for each search radius

# Output the results
print(mean_time)  # Print the average time spent for each search radius
print(mean_precision)  # Print the average precision@10 for each search radius
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
n_iter = 2   # Number of iterations of the Generalized Randomized Hashing (GRH) process
alpha = 0.5  # Weighting factor to update the hashcodes based on supervisory information (supervised learning)

# Loop through each iteration of GRH
for i in range(0, n_iter):
    
    # Step 1: Compute initial binary hash codes based on random hyperplanes
    # Data is projected onto random vectors (hyperplanes) and hashed to binary values (1 or -1)
    bin_indices_bits = (data_train.dot(random_vectors) >= 0).astype(int)  # Binary hash codes (0 or 1)
    bin_indices_bits[bin_indices_bits == 0] = -1  # Convert 0s to -1 to get [-1, 1] binary representation
    
    # Step 2: Refine hash codes using adjacency matrix (leveraging graph-based relationships)
    bin_indices_bits_refined = np.matmul(adjacency_matrix, bin_indices_bits.astype(float))  # Refine codes using neighborhood structure
    bin_indices_bits_refined = (bin_indices_bits_refined >= 0).astype(int)  # Convert to binary
    bin_indices_bits_refined[bin_indices_bits_refined <= 0] = -1  # Ensure the binary codes are in {-1, 1}
    
    # Step 3: Smooth hash codes by combining original and refined codes
    bin_indices_bits = (0.25 * bin_indices_bits_refined.astype(float) + 0.75 * bin_indices_bits.astype(float))  # Smooth out refined hash codes with original codes
    bin_indices_bits = (bin_indices_bits >= 0).astype(int)  # Convert back to binary form
    bin_indices_bits[bin_indices_bits <= 0] = -1  # Ensure binary values are in {-1, 1}
    
    # Step 4: Update hyperplanes based on supervised learning (using SVM)
    grh_hyperplanes = random_vectors.copy()  # Copy the current set of random hyperplanes
    for j in range(0, n_vectors):
        
        # Check if all binary codes for the j-th vector are the same (either all 1 or all -1)
        if abs(sum(bin_indices_bits[:, j])) == data_train.shape[0]:
            # If all bits are the same, generate a new random hyperplane
            random_vector = np.random.randn(dim, 1)
            grh_hyperplanes[:, j] = random_vector[:, 0]  # Replace the j-th hyperplane with a new random vector
        
        else:
            # Otherwise, fit an SVM classifier to the data using the binary codes as labels
            hyperplane = svclassifier.fit(data_train, bin_indices_bits[:, j]).coef_  # Fit SVM to get the hyperplane
            hyperplane = np.array(hyperplane)  # Convert the hyperplane coefficients to a NumPy array
            grh_hyperplanes[:, j] = hyperplane  # Update the j-th hyperplane with the SVM-trained hyperplane
    
    # Step 5: Update the random vectors for the next iteration
    random_vectors = grh_hyperplanes.copy()  # Copy the updated hyperplanes for the next iteration of GRH
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

In this tutorial, we demonstrate how to use a Support Vector Machine (SVM) to learn the hyperplanes for GRH. One of the key advantages of GRH, beyond its simplicity and effectiveness, is its flexibility—it’s agnostic to the learning algorithm. This means you can easily swap in a deep network to achieve more precise data-space partitioning or opt for a [passive aggressive classifier](https://www.youtube.com/watch?v=uxGDwyPWNkU) for a lightweight, online-adaptable method, ideal for streaming scenarios. Additionally, we explored a single hashtable implementation of LSH and GRH, and boosted the retrieval of relevant items by using multiple buckets through a multi-probing mechanism. Other LSH implementations take a different approach, utilizing multiple independent hashtables rather than probing buckets within the same one to increase the number of relevant results.

### Contact & Feedback 

Got thoughts on this tutorial? I'd love to hear them! You can reach out to the author, [Sean Moran](https://sjmoran.github.io/), anytime. Want to dive into the code? Check it out [here](./tutorial/hashing_tutorial.py), and don’t forget to grab the dependencies from the [requirements.txt] 

Copyright © [Sean Moran](https://sjmoran.github.io/) 2024. All opinions are my own.
