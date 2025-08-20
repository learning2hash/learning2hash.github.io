---
layout: publication
title: Triplet-aware Scene Graph Embeddings
authors: Brigit Schroeder, Subarna Tripathi, Hanlin Tang
conference: 2019 IEEE/CVF International Conference on Computer Vision Workshop (ICCVW)
year: 2019
bibkey: schroeder2019triplet
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.09256'}]
tags: [Evaluation, Image Retrieval, ICCV]
short_authors: Brigit Schroeder, Subarna Tripathi, Hanlin Tang
---
Scene graphs have become an important form of structured knowledge for tasks
such as for image generation, visual relation detection, visual question
answering, and image retrieval. While visualizing and interpreting word
embeddings is well understood, scene graph embeddings have not been fully
explored. In this work, we train scene graph embeddings in a layout generation
task with different forms of supervision, specifically introducing triplet
super-vision and data augmentation. We see a significant performance increase
in both metrics that measure the goodness of layout prediction, mean
intersection-over-union (mIoU)(52.3% vs. 49.2%) and relation score (61.7% vs.
54.1%),after the addition of triplet supervision and data augmentation. To
understand how these different methods affect the scene graph representation,
we apply several new visualization and evaluation methods to explore the
evolution of the scene graph embedding. We find that triplet supervision
significantly improves the embedding separability, which is highly correlated
with the performance of the layout prediction model.