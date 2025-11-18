---
layout: publication
title: A New Similarity Space Tailored For Supervised Deep Metric Learning
authors: Pedro H. Barros, Fabiane Queiroz, Flavio Figueredo, Jefersson A. Dos Santos,
  Heitor S. Ramos
conference: ACM Transactions on Intelligent Systems and Technology
year: 2020
bibkey: barros2020a
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.08325'}]
tags: ["Datasets", "Distance Metric Learning", "Supervised"]
short_authors: Barros et al.
---
We propose a novel deep metric learning method. Differently from many works
on this area, we defined a novel latent space obtained through an autoencoder.
The new space, namely S-space, is divided into different regions that describe
the positions where pairs of objects are similar/dissimilar. We locate makers
to identify these regions. We estimate the similarities between objects through
a kernel-based t-student distribution to measure the markers' distance and the
new data representation. In our approach, we simultaneously estimate the
markers' position in the S-space and represent the objects in the same space.
Moreover, we propose a new regularization function to avoid similar markers to
collapse altogether. We present evidences that our proposal can represent
complex spaces, for instance, when groups of similar objects are located in
disjoint regions. We compare our proposal to 9 different distance metric
learning approaches (four of them are based on deep-learning) on 28 real-world
heterogeneous datasets. According to the four quantitative metrics used, our
method overcomes all the nine strategies from the literature.