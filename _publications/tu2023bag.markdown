---
layout: publication
title: A Bag-of-prototypes Representation For Dataset-level Applications
authors: Weijie Tu, Weijian Deng, Tom Gedeon, Liang Zheng
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: tu2023bag
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.13251'}]
tags: ["CVPR", "Datasets"]
short_authors: Tu et al.
---
This work investigates dataset vectorization for two dataset-level tasks:
assessing training set suitability and test set difficulty. The former measures
how suitable a training set is for a target domain, while the latter studies
how challenging a test set is for a learned model. Central to the two tasks is
measuring the underlying relationship between datasets. This needs a desirable
dataset vectorization scheme, which should preserve as much discriminative
dataset information as possible so that the distance between the resulting
dataset vectors can reflect dataset-to-dataset similarity. To this end, we
propose a bag-of-prototypes (BoP) dataset representation that extends the
image-level bag consisting of patch descriptors to dataset-level bag consisting
of semantic prototypes. Specifically, we develop a codebook consisting of K
prototypes clustered from a reference dataset. Given a dataset to be encoded,
we quantize each of its image features to a certain prototype in the codebook
and obtain a K-dimensional histogram. Without assuming access to dataset
labels, the BoP representation provides a rich characterization of the dataset
semantic distribution. Furthermore, BoP representations cooperate well with
Jensen-Shannon divergence for measuring dataset-to-dataset similarity. Although
very simple, BoP consistently shows its advantage over existing representations
on a series of benchmarks for two dataset-level tasks.