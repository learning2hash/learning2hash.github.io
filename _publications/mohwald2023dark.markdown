---
layout: publication
title: 'Dark Side Augmentation: Generating Diverse Night Examples For Metric Learning'
authors: "Albert Mohwald, Tomas Jenicek, Ond\u0159ej Chum"
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: mohwald2023dark
citations: 5
additional_links: [{name: Code, url: 'https://github.com/mohwald/gandtr'}, {name: Paper,
    url: 'https://arxiv.org/abs/2309.16351'}]
tags: ["Distance Metric Learning", "ICCV", "Image Retrieval"]
short_authors: "Albert Mohwald, Tomas Jenicek, Ond\u0159ej Chum"
---
Image retrieval methods based on CNN descriptors rely on metric learning from
a large number of diverse examples of positive and negative image pairs.
Domains, such as night-time images, with limited availability and variability
of training data suffer from poor retrieval performance even with methods
performing well on standard benchmarks. We propose to train a GAN-based
synthetic-image generator, translating available day-time image examples into
night images. Such a generator is used in metric learning as a form of
augmentation, supplying training data to the scarce domain. Various types of
generators are evaluated and analyzed. We contribute with a novel light-weight
GAN architecture that enforces the consistency between the original and
translated image through edge consistency. The proposed architecture also
allows a simultaneous training of an edge detector that operates on both night
and day images. To further increase the variability in the training examples
and to maximize the generalization of the trained model, we propose a novel
method of diverse anchor mining.
  The proposed method improves over the state-of-the-art results on a standard
Tokyo 24/7 day-night retrieval benchmark while preserving the performance on
Oxford and Paris datasets. This is achieved without the need of training image
pairs of matching day and night images. The source code is available at
https://github.com/mohwald/gandtr .