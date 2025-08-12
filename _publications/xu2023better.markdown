---
layout: publication
title: Better Sampling Of Negatives For Distantly Supervised Named Entity Recognition
authors: Lu Xu, Lidong Bing, Wei Lu
conference: Arxiv
year: 2023
bibkey: xu2023better
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.13142'}]
tags: ["Datasets", "Supervised"]
short_authors: Lu Xu, Lidong Bing, Wei Lu
---
Distantly supervised named entity recognition (DS-NER) has been proposed to
exploit the automatically labeled training data instead of human annotations.
The distantly annotated datasets are often noisy and contain a considerable
number of false negatives. The recent approach uses a weighted sampling
approach to select a subset of negative samples for training. However, it
requires a good classifier to assign weights to the negative samples. In this
paper, we propose a simple and straightforward approach for selecting the top
negative samples that have high similarities with all the positive samples for
training. Our method achieves consistent performance improvements on four
distantly supervised NER datasets. Our analysis also shows that it is critical
to differentiate the true negatives from the false negatives.