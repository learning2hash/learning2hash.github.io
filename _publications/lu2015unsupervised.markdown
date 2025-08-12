---
layout: publication
title: 'Unsupervised Learning On Neural Network Outputs: With Application In Zero-shot
  Learning'
authors: Yao Lu
conference: Arxiv
year: 2016
bibkey: lu2015unsupervised
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1506.00990'}]
tags: ["Few Shot & Zero Shot", "Unsupervised"]
short_authors: Yao Lu
---
The outputs of a trained neural network contain much richer information than
just an one-hot classifier. For example, a neural network might give an image
of a dog the probability of one in a million of being a cat but it is still
much larger than the probability of being a car. To reveal the hidden structure
in them, we apply two unsupervised learning algorithms, PCA and ICA, to the
outputs of a deep Convolutional Neural Network trained on the ImageNet of 1000
classes. The PCA/ICA embedding of the object classes reveals their visual
similarity and the PCA/ICA components can be interpreted as common visual
features shared by similar object classes. For an application, we proposed a
new zero-shot learning method, in which the visual features learned by PCA/ICA
are employed. Our zero-shot learning method achieves the state-of-the-art
results on the ImageNet of over 20000 classes.