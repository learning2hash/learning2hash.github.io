---
layout: publication
title: Learning Low Bending And Low Distortion Manifold Embeddings
authors: "Juliane Braunsmann, Marko Rajkovi\u0107, Martin Rumpf, Benedikt Wirth"
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2021
bibkey: braunsmann2021learning
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.13189'}]
tags: ["CVPR"]
short_authors: Braunsmann et al.
---
Autoencoders are a widespread tool in machine learning to transform
high-dimensional data into a lowerdimensional representation which still
exhibits the essential characteristics of the input. The encoder provides an
embedding from the input data manifold into a latent space which may then be
used for further processing. For instance, learning interpolation on the
manifold may be simplified via the new manifold representation in latent space.
The efficiency of such further processing heavily depends on the regularity and
structure of the embedding. In this article, the embedding into latent space is
regularized via a loss function that promotes an as isometric and as flat
embedding as possible. The required training data comprises pairs of nearby
points on the input manifold together with their local distance and their local
Frechet average. This regularity loss functional even allows to train the
encoder on its own. The loss functional is computed via a Monte Carlo
integration which is shown to be consistent with a geometric loss functional
defined directly on the embedding map. Numerical tests are performed using
image data that encodes different data manifolds. The results show that smooth
manifold embeddings in latent space are obtained. These embeddings are regular
enough such that interpolation between not too distant points on the manifold
is well approximated by linear interpolation in latent space.