---
layout: publication
title: \(k\)-nearest Neighbor Augmented Neural Networks For Text Classification
authors: Zhiguo Wang, Wael Hamza, Linfeng Song
conference: Arxiv
year: 2017
bibkey: wang2017k
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.07863'}]
tags: ["Datasets", "Evaluation", "Supervised"]
short_authors: Zhiguo Wang, Wael Hamza, Linfeng Song
---
In recent years, many deep-learning based models are proposed for text
classification. This kind of models well fits the training set from the
statistical point of view. However, it lacks the capacity of utilizing
instance-level information from individual instances in the training set. In
this work, we propose to enhance neural network models by allowing them to
leverage information from \(k\)-nearest neighbor (kNN) of the input text. Our
model employs a neural network that encodes texts into text embeddings.
Moreover, we also utilize \(k\)-nearest neighbor of the input text as an external
memory, and utilize it to capture instance-level information from the training
set. The final prediction is made based on features from both the neural
network encoder and the kNN memory. Experimental results on several standard
benchmark datasets show that our model outperforms the baseline model on all
the datasets, and it even beats a very deep neural network model (with 29
layers) in several datasets. Our model also shows superior performance when
training instances are scarce, and when the training set is severely
unbalanced. Our model also leverages techniques such as semi-supervised
training and transfer learning quite well.