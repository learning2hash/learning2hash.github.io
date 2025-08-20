---
layout: publication
title: Unsupervised Representation Learning With Minimax Distance Measures
authors: Morteza Haghir Chehreghani
conference: Machine Learning
year: 2020
bibkey: chehreghani2020unsupervised
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.13223'}]
tags: [Tools & Libraries, ICML, Unsupervised, Distance Metric Learning]
short_authors: Morteza Haghir Chehreghani
---
We investigate the use of Minimax distances to extract in a nonparametric way
the features that capture the unknown underlying patterns and structures in the
data. We develop a general-purpose and computationally efficient framework to
employ Minimax distances with many machine learning methods that perform on
numerical data. We study both computing the pairwise Minimax distances for all
pairs of objects and as well as computing the Minimax distances of all the
objects to/from a fixed (test) object. We first efficiently compute the
pairwise Minimax distances between the objects, using the equivalence of
Minimax distances over a graph and over a minimum spanning tree constructed on
that. Then, we perform an embedding of the pairwise Minimax distances into a
new vector space, such that their squared Euclidean distances in the new space
equal to the pairwise Minimax distances in the original space. We also study
the case of having multiple pairwise Minimax matrices, instead of a single one.
Thereby, we propose an embedding via first summing up the centered matrices and
then performing an eigenvalue decomposition to obtain the relevant features. In
the following, we study computing Minimax distances from a fixed (test) object
which can be used for instance in K-nearest neighbor search. Similar to the
case of all-pair pairwise Minimax distances, we develop an efficient and
general-purpose algorithm that is applicable with any arbitrary base distance
measure. Moreover, we investigate in detail the edges selected by the Minimax
distances and thereby explore the ability of Minimax distances in detecting
outlier objects. Finally, for each setting, we perform several experiments to
demonstrate the effectiveness of our framework.