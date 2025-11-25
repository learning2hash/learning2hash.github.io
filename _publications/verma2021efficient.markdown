---
layout: publication
title: Efficient Binary Embedding Of Categorical Data Using Binsketch
authors: Bhisham Dev Verma, Rameshwar Pratap, Debajyoti Bera
conference: Arxiv
year: 2021
bibkey: verma2021efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.07163'}]
tags: ["Datasets", "Efficiency", "Hashing Methods"]
short_authors: Bhisham Dev Verma, Rameshwar Pratap, Debajyoti Bera
---
In this work, we present a dimensionality reduction algorithm, aka.
sketching, for categorical datasets. Our proposed sketching algorithm Cabin
constructs low-dimensional binary sketches from high-dimensional categorical
vectors, and our distance estimation algorithm Cham computes a close
approximation of the Hamming distance between any two original vectors only
from their sketches. The minimum dimension of the sketches required by Cham to
ensure a good estimation theoretically depends only on the sparsity of the data
points - making it useful for many real-life scenarios involving sparse
datasets. We present a rigorous theoretical analysis of our approach and
supplement it with extensive experiments on several high-dimensional real-world
data sets, including one with over a million dimensions. We show that the Cabin
and Cham duo is a significantly fast and accurate approach for tasks such as
RMSE, all-pairs similarity, and clustering when compared to working with the
full dataset and other dimensionality reduction techniques.