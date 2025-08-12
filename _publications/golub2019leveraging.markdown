---
layout: publication
title: Leveraging Pretrained Image Classifiers For Language-based Segmentation
authors: "David Golub, Ahmed El-kishky, Roberto Mart\xEDn-mart\xEDn"
conference: 2020 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2020
bibkey: golub2019leveraging
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.00830'}]
tags: []
short_authors: "David Golub, Ahmed El-kishky, Roberto Mart\xEDn-mart\xEDn"
---
Current semantic segmentation models cannot easily generalize to new object
classes unseen during train time: they require additional annotated images and
retraining. We propose a novel segmentation model that injects visual priors
into semantic segmentation architectures, allowing them to segment out new
target labels without retraining. As visual priors, we use the activations of
pretrained image classifiers, which provide noisy indications of the spatial
location of both the target object and distractor objects in the scene. We
leverage language semantics to obtain these activations for a target label
unseen by the classifier. Further experiments show that the visual priors
obtained via language semantics for both relevant and distracting objects are
key to our performance.