---
layout: publication
title: Fast Distance-based Anomaly Detection In Images Using An Inception-like Autoencoder
authors: Natasa Sarafijanovic-Djukic, Jesse Davis
conference: Lecture Notes in Computer Science
year: 2019
bibkey: sarafijanovicdjukic2019fast
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.08731'}]
tags: ["Datasets", "Evaluation", "Quantization"]
short_authors: Natasa Sarafijanovic-Djukic, Jesse Davis
---
The goal of anomaly detection is to identify examples that deviate from
normal or expected behavior. We tackle this problem for images. We consider a
two-phase approach. First, using normal examples, a convolutional autoencoder
(CAE) is trained to extract a low-dimensional representation of the images.
Here, we propose a novel architectural choice when designing the CAE, an
Inception-like CAE. It combines convolutional filters of different kernel sizes
and it uses a Global Average Pooling (GAP) operation to extract the
representations from the CAE's bottleneck layer. Second, we employ a
distanced-based anomaly detector in the low-dimensional space of the learned
representation for the images. However, instead of computing the exact
distance, we compute an approximate distance using product quantization. This
alleviates the high memory and prediction time costs of distance-based anomaly
detectors. We compare our proposed approach to a number of baselines and
state-of-the-art methods on four image datasets, and we find that our approach
resulted in improved predictive performance.