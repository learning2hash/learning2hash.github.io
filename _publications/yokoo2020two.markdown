---
layout: publication
title: Two-stage Discriminative Re-ranking for Large-scale Landmark Retrieval
authors: Yokoo et al.
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2020
bibkey: yokoo2020two
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.11211'}]
tags: ["Hybrid ANN Methods", "CVPR", "Scalability", "Re RANKING"]
---
We propose an efficient pipeline for large-scale landmark image retrieval
that addresses the diversity of the dataset through two-stage discriminative
re-ranking. Our approach is based on embedding the images in a feature-space
using a convolutional neural network trained with a cosine softmax loss. Due to
the variance of the images, which include extreme viewpoint changes such as
having to retrieve images of the exterior of a landmark from images of the
interior, this is very challenging for approaches based exclusively on visual
similarity. Our proposed re-ranking approach improves the results in two steps:
in the sort-step, \\(k\\)-nearest neighbor search with soft-voting to sort the
retrieved results based on their label similarity to the query images, and in
the insert-step, we add additional samples from the dataset that were not
retrieved by image-similarity. This approach allows overcoming the low visual
diversity in retrieved images. In-depth experimental results show that the
proposed approach significantly outperforms existing approaches on the
challenging Google Landmarks Datasets. Using our methods, we achieved 1st place
in the Google Landmark Retrieval 2019 challenge and 3rd place in the Google
Landmark Recognition 2019 challenge on Kaggle. Our code is publicly available
here: https://github.com/lyakaap/Landmark2019-1st-and-3rd-Place-Solution