---
layout: publication
title: Appearance Invariance In Convolutional Networks With Neighborhood Similarity
authors: Tolga Tasdizen, Mehdi Sajjadi, Mehran Javanmardi, Nisha Ramesh
conference: Arxiv
year: 2017
bibkey: tasdizen2017appearance
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.00755'}]
tags: []
short_authors: Tasdizen et al.
---
We present a neighborhood similarity layer (NSL) which induces appearance
invariance in a network when used in conjunction with convolutional layers. We
are motivated by the observation that, even though convolutional networks have
low generalization error, their generalization capability does not extend to
samples which are not represented by the training data. For instance, while
novel appearances of learned concepts pose no problem for the human visual
system, feedforward convolutional networks are generally not successful in such
situations. Motivated by the Gestalt principle of grouping with respect to
similarity, the proposed NSL transforms its input feature map using the feature
vectors at each pixel as a frame of reference, i.e. center of attention, for
its surrounding neighborhood. This transformation is spatially varying, hence
not a convolution. It is differentiable; therefore, networks including the
proposed layer can be trained in an end-to-end manner. We analyze the
invariance of NSL to significant changes in appearance that are not represented
in the training data. We also demonstrate its advantages for digit recognition,
semantic labeling and cell detection problems.