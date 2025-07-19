---
layout: publication
title: The General Pair-based Weighting Loss for Deep Metric Learning
authors: Liu et al.
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: liu2019general
citations: 550
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.12837'}]
tags: [CVPR, Distance Metric Learning]
---
Deep metric learning aims at learning the distance metric between pair of
samples, through the deep neural networks to extract the semantic feature
embeddings where similar samples are close to each other while dissimilar
samples are farther apart. A large amount of loss functions based on pair
distances have been presented in the literature for guiding the training of
deep metric learning. In this paper, we unify them in a general pair-based
weighting loss function, where the minimizing objective loss is just the
distances weighting of informative pairs. The general pair-based weighting loss
includes two main aspects, (1) samples mining and (2) pairs weighting. Samples
mining aims at selecting the informative positive and negative pair sets to
exploit the structured relationship of samples in a mini-batch and also reduce
the number of non-trivial pairs. Pair weighting aims at assigning different
weights for different pairs according to the pair distances for
discriminatively training the network. We detailedly review those existing
pair-based losses inline with our general loss function, and explore some
possible methods from the perspective of samples mining and pairs weighting.
Finally, extensive experiments on three image retrieval datasets show that our
general pair-based weighting loss obtains new state-of-the-art performance,
demonstrating the effectiveness of the pair-based samples mining and pairs
weighting for deep metric learning.