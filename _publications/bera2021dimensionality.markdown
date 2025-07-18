---
layout: publication
title: Dimensionality Reduction For Categorical Data
authors: Bera Debajyoti, Pratap Rameshwar, Verma Bhisham Dev
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2021
bibkey: bera2021dimensionality
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.00362'}]
tags: [Compact Codes, DATASETS, Evaluation]
---
Categorical attributes are those that can take a discrete set of values,
e.g., colours. This work is about compressing vectors over categorical
attributes to low-dimension discrete vectors. The current hash-based methods
compressing vectors over categorical attributes to low-dimension discrete
vectors do not provide any guarantee on the Hamming distances between the
compressed representations. Here we present FSketch to create sketches for
sparse categorical data and an estimator to estimate the pairwise Hamming
distances among the uncompressed data only from their sketches. We claim that
these sketches can be used in the usual data mining tasks in place of the
original data without compromising the quality of the task. For that, we ensure
that the sketches also are categorical, sparse, and the Hamming distance
estimates are reasonably precise. Both the sketch construction and the Hamming
distance estimation algorithms require just a single-pass; furthermore, changes
to a data point can be incorporated into its sketch in an efficient manner. The
compressibility depends upon how sparse the data is and is independent of the
original dimension -- making our algorithm attractive for many real-life
scenarios. Our claims are backed by rigorous theoretical analysis of the
properties of FSketch and supplemented by extensive comparative evaluations
with related algorithms on some real-world datasets. We show that FSketch is
significantly faster, and the accuracy obtained by using its sketches are among
the top for the standard unsupervised tasks of RMSE, clustering and similarity
search.