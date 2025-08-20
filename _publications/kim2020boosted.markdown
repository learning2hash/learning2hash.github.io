---
layout: publication
title: 'Boosted Locality Sensitive Hashing: Discriminative Binary Codes For Source
  Separation'
authors: Sunwoo Kim, Haici Yang, Minje Kim
conference: ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2020
bibkey: kim2020boosted
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.06239'}]
tags: [Neural Hashing, ICASSP, Hashing Methods, Locality Sensitive Hashing, Compact
    Codes, Evaluation]
short_authors: Sunwoo Kim, Haici Yang, Minje Kim
---
Speech enhancement tasks have seen significant improvements with the advance
of deep learning technology, but with the cost of increased computational
complexity. In this study, we propose an adaptive boosting approach to learning
locality sensitive hash codes, which represent audio spectra efficiently. We
use the learned hash codes for single-channel speech denoising tasks as an
alternative to a complex machine learning model, particularly to address the
resource-constrained environments. Our adaptive boosting algorithm learns
simple logistic regressors as the weak learners. Once trained, their binary
classification results transform each spectrum of test noisy speech into a bit
string. Simple bitwise operations calculate Hamming distance to find the
K-nearest matching frames in the dictionary of training noisy speech spectra,
whose associated ideal binary masks are averaged to estimate the denoising mask
for that test mixture. Our proposed learning algorithm differs from AdaBoost in
the sense that the projections are trained to minimize the distances between
the self-similarity matrix of the hash codes and that of the original spectra,
rather than the misclassification rate. We evaluate our discriminative hash
codes on the TIMIT corpus with various noise types, and show comparative
performance to deep learning methods in terms of denoising performance and
complexity.