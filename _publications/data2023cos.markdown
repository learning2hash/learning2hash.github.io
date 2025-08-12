---
layout: publication
title: Cos R-CNN For Online Few-shot Object Detection
authors: Gratianus Wesley Putra Data, Henry Howard-Jenkins, David Murray, Victor Prisacariu
conference: Arxiv
year: 2023
bibkey: data2023cos
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.13485'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Data et al.
---
We propose Cos R-CNN, a simple exemplar-based R-CNN formulation that is
designed for online few-shot object detection. That is, it is able to localise
and classify novel object categories in images with few examples without
fine-tuning. Cos R-CNN frames detection as a learning-to-compare task: unseen
classes are represented as exemplar images, and objects are detected based on
their similarity to these exemplars. The cosine-based classification head
allows for dynamic adaptation of classification parameters to the exemplar
embedding, and encourages the clustering of similar classes in embedding space
without the need for manual tuning of distance-metric hyperparameters. This
simple formulation achieves best results on the recently proposed 5-way
ImageNet few-shot detection benchmark, beating the online 1/5/10-shot scenarios
by more than 8/3/1%, as well as performing up to 20% better in online 20-way
few-shot VOC across all shots on novel classes.