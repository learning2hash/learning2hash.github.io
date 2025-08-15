---
layout: publication
title: 'Condl: Detector-free Dense Image Matching'
authors: Monika Kwiatkowski, Simon Matern, Olaf Hellwich
conference: Arxiv
year: 2024
bibkey: kwiatkowski2024condl
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.02766'}]
tags: ["Self-Supervised"]
short_authors: Monika Kwiatkowski, Simon Matern, Olaf Hellwich
---
In this work, we introduce a deep-learning framework designed for estimating
dense image correspondences. Our fully convolutional model generates dense
feature maps for images, where each pixel is associated with a descriptor that
can be matched across multiple images. Unlike previous methods, our model is
trained on synthetic data that includes significant distortions, such as
perspective changes, illumination variations, shadows, and specular highlights.
Utilizing contrastive learning, our feature maps achieve greater invariance to
these distortions, enabling robust matching. Notably, our method eliminates the
need for a keypoint detector, setting it apart from many existing
image-matching techniques.