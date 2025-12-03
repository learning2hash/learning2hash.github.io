---
layout: publication
title: Rapid Probabilistic Interest Learning From Domain-specific Pairwise Image Comparisons
authors: Michael Burke, Siyabonga Mbonambi, Purity Molala, Raesetje Sefala
conference: Arxiv
year: 2017
bibkey: burke2017rapid
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.05850'}]
tags: ["Evaluation", "Image Retrieval", "Neural Hashing"]
short_authors: Burke et al.
---
A great deal of work aims to discover large general purpose models of image
interest or memorability for visual search and information retrieval. This
paper argues that image interest is often domain and user specific, and that
efficient mechanisms for learning about this domain-specific image interest as
quickly as possible, while limiting the amount of data-labelling required, are
often more useful to end-users. This work uses pairwise image comparisons to
reduce the labelling burden on these users, and introduces an image interest
estimation approach that performs similarly to recent data hungry deep learning
approaches trained using pairwise ranking losses. Here, we use a Gaussian
process model to interpolate image interest inferred using a Bayesian ranking
approach over image features extracted using a pre-trained convolutional neural
network. Results show that fitting a Gaussian process in high-dimensional image
feature space is not only computationally feasible, but also effective across a
broad range of domains. The proposed probabilistic interest estimation approach
produces image interests paired with uncertainties that can be used to identify
images for which additional labelling is required and measure inference
convergence, allowing for sample efficient active model training. Importantly,
the probabilistic formulation allows for effective visual search and
information retrieval when limited labelling data is available.