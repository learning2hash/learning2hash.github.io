---
layout: publication
title: Presence-only Geographical Priors For Fine-grained Image Classification
authors: Oisin Mac Aodha, Elijah Cole, Pietro Perona
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: macaodha2019presence
citations: 108
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.05272'}]
tags: ["ICCV"]
short_authors: Oisin Mac Aodha, Elijah Cole, Pietro Perona
---
Appearance information alone is often not sufficient to accurately
differentiate between fine-grained visual categories. Human experts make use of
additional cues such as where, and when, a given image was taken in order to
inform their final decision. This contextual information is readily available
in many online image collections but has been underutilized by existing image
classifiers that focus solely on making predictions based on the image
contents.
  We propose an efficient spatio-temporal prior, that when conditioned on a
geographical location and time, estimates the probability that a given object
category occurs at that location. Our prior is trained from presence-only
observation data and jointly models object categories, their spatio-temporal
distributions, and photographer biases. Experiments performed on multiple
challenging image classification datasets show that combining our prior with
the predictions from image classifiers results in a large improvement in final
classification performance.