---
layout: publication
title: Calibrated neighborhood aware confidence measure for deep metric learning
authors: Karpusha Maryna, Yun Sunghee, Fehervari Istvan
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: karpusha2020calibrated
citations: 102
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.04935'}]
tags: ["CVPR"]
---
Deep metric learning has gained promising improvement in recent years
following the success of deep learning. It has been successfully applied to
problems in few-shot learning, image retrieval, and open-set classifications.
However, measuring the confidence of a deep metric learning model and
identifying unreliable predictions is still an open challenge. This paper
focuses on defining a calibrated and interpretable confidence metric that
closely reflects its classification accuracy. While performing similarity
comparison directly in the latent space using the learned distance metric, our
approach approximates the distribution of data points for each class using a
Gaussian kernel smoothing function. The post-processing calibration algorithm
with proposed confidence metric on the held-out validation dataset improves
generalization and robustness of state-of-the-art deep metric learning models
while provides an interpretable estimation of the confidence. Extensive tests
on four popular benchmark datasets (Caltech-UCSD Birds, Stanford Online
Product, Stanford Car-196, and In-shop Clothes Retrieval) show consistent
improvements even at the presence of distribution shifts in test data related
to additional noise or adversarial examples.