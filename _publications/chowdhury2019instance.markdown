---
layout: publication
title: Instance-based Inductive Deep Transfer Learning by Cross-Dataset Querying with
  Locality Sensitive Hashing
authors: Chowdhury Somnath Basu Roy, Annervaz K M, Dukkipati Ambedkar
conference: Proceedings of the 2nd Workshop on Deep Learning Approaches for Low-Resource
  NLP (DeepLo 2019)
year: 2019
bibkey: chowdhury2019instance
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.05934'}]
tags: [Locality Sensitive Hashing, Datasets, Hashing Methods]
---
Supervised learning models are typically trained on a single dataset and the
performance of these models rely heavily on the size of the dataset, i.e.,
amount of data available with the ground truth. Learning algorithms try to
generalize solely based on the data that is presented with during the training.
In this work, we propose an inductive transfer learning method that can augment
learning models by infusing similar instances from different learning tasks in
the Natural Language Processing (NLP) domain. We propose to use instance
representations from a source dataset, \textit\{without inheriting anything\}
from the source learning model. Representations of the instances of
\textit\{source\} \& \textit\{target\} datasets are learned, retrieval of relevant
source instances is performed using soft-attention mechanism and
\textit\{locality sensitive hashing\}, and then, augmented into the model during
training on the target dataset. Our approach simultaneously exploits the local
\textit\{instance level information\} as well as the macro statistical viewpoint
of the dataset. Using this approach we have shown significant improvements for
three major news classification datasets over the baseline. Experimental
evaluations also show that the proposed approach reduces dependency on labeled
data by a significant margin for comparable performance. With our proposed
cross dataset learning procedure we show that one can achieve
competitive/better performance than learning from a single dataset.