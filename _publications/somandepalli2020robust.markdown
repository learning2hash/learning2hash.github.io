---
layout: publication
title: 'Robust Character Labeling In Movie Videos: Data Resources And Self-supervised
  Feature Adaptation'
authors: Krishna Somandepalli, Rajat Hebbar, Shrikanth Narayanan
conference: IEEE Transactions on Multimedia
year: 2021
bibkey: somandepalli2020robust
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.11289'}]
tags: ["Datasets", "Self-Supervised"]
short_authors: Krishna Somandepalli, Rajat Hebbar, Shrikanth Narayanan
---
Robust face clustering is a vital step in enabling computational
understanding of visual character portrayal in media. Face clustering for
long-form content is challenging because of variations in appearance and lack
of supporting large-scale labeled data. Our work in this paper focuses on two
key aspects of this problem: the lack of domain-specific training or benchmark
datasets, and adapting face embeddings learned on web images to long-form
content, specifically movies. First, we present a dataset of over 169,000 face
tracks curated from 240 Hollywood movies with weak labels on whether a pair of
face tracks belong to the same or a different character. We propose an offline
algorithm based on nearest-neighbor search in the embedding space to mine
hard-examples from these tracks. We then investigate triplet-loss and multiview
correlation-based methods for adapting face embeddings to hard-examples. Our
experimental results highlight the usefulness of weakly labeled data for
domain-specific feature adaptation. Overall, we find that multiview
correlation-based adaptation yields more discriminative and robust face
embeddings. Its performance on downstream face verification and clustering
tasks is comparable to that of the state-of-the-art results in this domain. We
also present the SAIL-Movie Character Benchmark corpus developed to augment
existing benchmarks. It consists of racially diverse actors and provides
face-quality labels for subsequent error analysis. We hope that the large-scale
datasets developed in this work can further advance automatic character
labeling in videos. All resources are available freely at
https://sail.usc.edu/~ccmi/multiface.