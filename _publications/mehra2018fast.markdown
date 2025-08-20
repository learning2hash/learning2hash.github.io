---
layout: publication
title: Fast Interactive Image Retrieval Using Large-scale Unlabeled Data
authors: Akshay Mehra, Jihun Hamm, Mikhail Belkin
conference: Arxiv
year: 2018
bibkey: mehra2018fast
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.04204'}]
tags: [Image Retrieval, Datasets, Supervised, Graph-based ANN, Scalability, Neural
    Hashing]
short_authors: Akshay Mehra, Jihun Hamm, Mikhail Belkin
---
An interactive image retrieval system learns which images in the database
belong to a user's query concept, by analyzing the example images and feedback
provided by the user. The challenge is to retrieve the relevant images with
minimal user interaction. In this work, we propose to solve this problem by
posing it as a binary classification task of classifying all images in the
database as being relevant or irrelevant to the user's query concept. Our
method combines active learning with graph-based semi-supervised learning
(GSSL) to tackle this problem. Active learning reduces the number of user
interactions by querying the labels of the most informative points and GSSL
allows to use abundant unlabeled data along with the limited labeled data
provided by the user. To efficiently find the most informative point, we use an
uncertainty sampling based method that queries the label of the point nearest
to the decision boundary of the classifier. We estimate this decision boundary
using our heuristic of adaptive threshold. To utilize huge volumes of unlabeled
data we use an efficient approximation based method that reduces the complexity
of GSSL from \(O(n^3)\) to \(O(n)\), making GSSL scalable. We make the classifier
robust to the diversity and noisy labels associated with images in large
databases by incorporating information from multiple modalities such as visual
information extracted from deep learning based models and semantic information
extracted from the WordNet. High F1 scores within few relevance feedback rounds
in our experiments with concepts defined on AnimalWithAttributes and Imagenet
(1.2 million images) datasets indicate the effectiveness and scalability of our
approach.