---
layout: publication
title: 'Onionnet: Sharing Features In Cascaded Deep Classifiers'
authors: Martin Simonovsky, Nikos Komodakis
conference: Procedings of the British Machine Vision Conference 2016
year: 2016
bibkey: simonovsky2016onionnet
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1608.02728'}]
tags: []
short_authors: Martin Simonovsky, Nikos Komodakis
---
The focus of our work is speeding up evaluation of deep neural networks in
retrieval scenarios, where conventional architectures may spend too much time
on negative examples. We propose to replace a monolithic network with our novel
cascade of feature-sharing deep classifiers, called OnionNet, where subsequent
stages may add both new layers as well as new feature channels to the previous
ones. Importantly, intermediate feature maps are shared among classifiers,
preventing them from the necessity of being recomputed. To accomplish this, the
model is trained end-to-end in a principled way under a joint loss. We validate
our approach in theory and on a synthetic benchmark. As a result demonstrated
in three applications (patch matching, object detection, and image retrieval),
our cascade can operate significantly faster than both monolithic networks and
traditional cascades without sharing at the cost of marginal decrease in
precision.