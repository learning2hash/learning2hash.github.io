import scipy.io
import os
import requests

url='https://www.dropbox.com/s/875u1rkva9iffpj/Gist512CIFAR10.mat?dl=1'
response = requests.get(url)
with open(os.path.join("./", "Gist512CIFAR10.mat"), 'wb') as f:
    f.write(response.content)

mat = scipy.io.loadmat('./Gist512CIFAR10.mat')

from sklearn.preprocessing import Normalizer
data = mat['X']
data = Normalizer(norm='l2').fit_transform(data)
data= data- data.mean(axis=0)
classes = mat['X_class']

num_classes = 10
n_vectors = 16
dim = 512

import numpy as np

np.random.seed(0)
random_vectors = np.random.randn(dim, n_vectors)
print(random_vectors)

print('dimension:', data[0,:].shape)

# https://wiki.python.org/moin/BitwiseOperators
# x << y is the same as multiplying x by 2 ** y
powers_of_two = 1 << np.arange(n_vectors - 1, -1, step=-1)

# we can do it for the entire corpus
bin_indices_bits = data.dot(random_vectors) >= 0
bin_indices = bin_indices_bits.dot(powers_of_two)
bin_indices.shape

from collections import defaultdict

table = defaultdict(list)
for idx, bin_index in enumerate(bin_indices):
    table[bin_index].append(idx)

from sklearn.model_selection import train_test_split

np.random.seed(0)
data_temp, data_query, labels_temp, labels_query = train_test_split(data, classes[0,:], test_size=0.002, random_state=42)
data_database, data_train, labels_database, labels_train = train_test_split(data_temp, labels_temp[:], test_size=0.02, random_state=42)

from sklearn.svm import SVC
svclassifier = SVC(kernel='linear') #class_weight='balanced')

adjacency_matrix=np.equal.outer(labels_train, labels_train).astype(float)
row_sums = adjacency_matrix.sum(axis=1)
adjacency_matrix = adjacency_matrix / row_sums[:, np.newaxis]

n_iter=2

for i in range(0,n_iter):

    print(i)
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
            print("here")
        else:
            hyperplane=svclassifier.fit(data_train, bin_indices_bits[:,j]).coef_
            hyperplane=np.array(hyperplane)
            grh_hyperplanes[:,j]=hyperplane

    random_vectors = grh_hyperplanes.copy()

# we can do it for the entire corpus
bin_indices_bits = data_database.dot(random_vectors) >= 0
print(bin_indices_bits.shape)
bin_indices = bin_indices_bits.dot(powers_of_two)
bin_indices.shape

from collections import defaultdict

table = defaultdict(list)
for idx, bin_index in enumerate(bin_indices):
    table[bin_index].append(idx)

from itertools import combinations
from sklearn.metrics.pairwise import pairwise_distances
import pandas as pd

max_search_radius=10
topn=10
precision_history = {i: [] for i in range(max_search_radius+1)}
time_history = {i: [] for i in range(max_search_radius+1)}

import time

for query_image, query_label in zip(data_query,labels_query):

    bin_index_bits = np.ravel(query_image.dot(random_vectors) >= 0)
    candidate_set = set()

    for search_radius in range(max_search_radius + 1):

        start = time.time()

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
        time_history[search_radius].append(elapsed_time)

mean_time = [np.mean(time_history[i]) for i in range(len(time_history))]
print(mean_time)
print(precision_history)
mean_precision = [np.mean(precision_history[i]) for i in range(len(precision_history))]

print(mean_precision)
