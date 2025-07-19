---
layout: publication
title: Deep Variational And Structural Hashing
authors: Liong et al.
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2018
bibkey: liong2018deep
citations: 56
additional_links: [{name: Paper, url: 'http://ieeexplore.ieee.org/document/4031381/'}]
tags: [Hashing Methods]
---
In this paper, we propose a deep variational and structural hashing (DVStH) method to learn compact binary codes for multimedia retrieval. Unlike most existing deep hashing methods which use a series of convolution and fully-connected layers to learn binary features, we develop a probabilistic framework to infer latent feature representation inside the network. Then, we design a struct layer rather than a bottleneck hash layer, to obtain binary codes through a simple encoding procedure. By doing these, we are able to obtain binary codes discriminatively and generatively. To make it applicable to cross-modal scalable multimedia retrieval, we extend our method to a cross-modal deep variational and structural hashing (CM-DVStH). We design a deep fusion network with a struct layer to maximize the correlation between image-text input pairs during the training stage so that a unified binary vector can be obtained. We then design modality-specific hashing networks to handle the out-of-sample extension scenario. Specifically, we train a network for each modality which outputs a latent representation that is as close as possible to the binary codes which are inferred from the fusion network. Experimental results on five benchmark datasets are presented to show the efficacy of the proposed approach.