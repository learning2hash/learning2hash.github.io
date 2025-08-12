---
layout: publication
title: Improving Few-shot Learning With Weakly-supervised Object Localization
authors: Inyong Koo, Minki Jeong, Changick Kim
conference: Arxiv
year: 2021
bibkey: koo2021improving
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.11715'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Inyong Koo, Minki Jeong, Changick Kim
---
Few-shot learning often involves metric learning-based classifiers, which
predict the image label by comparing the distance between the extracted feature
vector and class representations. However, applying global pooling in the
backend of the feature extractor may not produce an embedding that correctly
focuses on the class object. In this work, we propose a novel framework that
generates class representations by extracting features from class-relevant
regions of the images. Given only a few exemplary images with image-level
labels, our framework first localizes the class objects by spatially
decomposing the similarity between the images and their class prototypes. Then,
enhanced class representations are achieved from the localization results. We
also propose a loss function to enhance distinctions of the refined features.
Our method outperforms the baseline few-shot model in miniImageNet and
tieredImageNet benchmarks.