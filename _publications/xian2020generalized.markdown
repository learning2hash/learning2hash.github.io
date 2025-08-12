---
layout: publication
title: Generalized Few-shot Video Classification With Video Retrieval And Feature
  Generation
authors: Yongqin Xian, Bruno Korbar, Matthijs Douze, Lorenzo Torresani, Bernt Schiele,
  Zeynep Akata
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2021
bibkey: xian2020generalized
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.04755'}]
tags: ["Few Shot & Zero Shot", "Video Retrieval"]
short_authors: Xian et al.
---
Few-shot learning aims to recognize novel classes from a few examples.
Although significant progress has been made in the image domain, few-shot video
classification is relatively unexplored. We argue that previous methods
underestimate the importance of video feature learning and propose to learn
spatiotemporal features using a 3D CNN. Proposing a two-stage approach that
learns video features on base classes followed by fine-tuning the classifiers
on novel classes, we show that this simple baseline approach outperforms prior
few-shot video classification methods by over 20 points on existing benchmarks.
To circumvent the need of labeled examples, we present two novel approaches
that yield further improvement. First, we leverage tag-labeled videos from a
large dataset using tag retrieval followed by selecting the best clips with
visual similarities. Second, we learn generative adversarial networks that
generate video features of novel classes from their semantic embeddings.
Moreover, we find existing benchmarks are limited because they only focus on 5
novel classes in each testing episode and introduce more realistic benchmarks
by involving more novel classes, i.e. few-shot learning, as well as a mixture
of novel and base classes, i.e. generalized few-shot learning. The experimental
results show that our retrieval and feature generation approach significantly
outperform the baseline approach on the new benchmarks.