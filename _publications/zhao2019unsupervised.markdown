---
layout: publication
title: Unsupervised Adversarial Attacks On Deep Feature-based Retrieval With GAN
authors: Guoping Zhao, Mingyu Zhang, Jiajun Liu, Ji-Rong Wen
conference: Arxiv
year: 2019
bibkey: zhao2019unsupervised
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.05793'}]
tags: ["Image Retrieval", "Robustness", "Unsupervised"]
short_authors: Zhao et al.
---
Studies show that Deep Neural Network (DNN)-based image classification models
are vulnerable to maliciously constructed adversarial examples. However, little
effort has been made to investigate how DNN-based image retrieval models are
affected by such attacks. In this paper, we introduce Unsupervised Adversarial
Attacks with Generative Adversarial Networks (UAA-GAN) to attack deep
feature-based image retrieval systems. UAA-GAN is an unsupervised learning
model that requires only a small amount of unlabeled data for training. Once
trained, it produces query-specific perturbations for query images to form
adversarial queries. The core idea is to ensure that the attached perturbation
is barely perceptible to human yet effective in pushing the query away from its
original position in the deep feature space. UAA-GAN works with various
application scenarios that are based on deep features, including image
retrieval, person Re-ID and face search. Empirical results show that UAA-GAN
cripples retrieval performance without significant visual changes in the query
images. UAA-GAN generated adversarial examples are less distinguishable because
they tend to incorporate subtle perturbations in textured or salient areas of
the images, such as key body parts of human, dominant structural
patterns/textures or edges, rather than in visually insignificant areas (e.g.,
background and sky). Such tendency indicates that the model indeed learned how
to toy with both image retrieval systems and human eyes.