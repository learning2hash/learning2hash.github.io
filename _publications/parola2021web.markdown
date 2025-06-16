---
layout: publication
title: Web Image Search Engine Based On LSH Index And CNN Resnet50
authors: Marco Parola, Alice Nannini, Stefano Poleggi
conference: Arxiv
year: 2021
citations: 3
bibkey: parola2021web
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.13301'}]
tags: [Applications, ANN Search, Efficient Learning, Evaluation Metrics, Hashing Methods]
---
To implement a good Content Based Image Retrieval (CBIR) system, it is
essential to adopt efficient search methods. One way to achieve this results is
by exploiting approximate search techniques. In fact, when we deal with very
large collections of data, using an exact search method makes the system very
slow. In this project, we adopt the Locality Sensitive Hashing (LSH) index to
implement a CBIR system that allows us to perform fast similarity search on
deep features. Specifically, we exploit transfer learning techniques to extract
deep features from images; this phase is done using two famous Convolutional
Neural Networks (CNNs) as features extractors: Resnet50 and Resnet50v2, both
pre-trained on ImageNet. Then we try out several fully connected deep neural
networks, built on top of both of the previously mentioned CNNs in order to
fine-tuned them on our dataset. In both of previous cases, we index the
features within our LSH index implementation and within a sequential scan, to
better understand how much the introduction of the index affects the results.
Finally, we carry out a performance analysis: we evaluate the relevance of the
result set, computing the mAP (mean Average Precision) value obtained during
the different experiments with respect to the number of done comparison and
varying the hyper-parameter values of the LSH index.