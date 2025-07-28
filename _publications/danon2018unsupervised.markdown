---
layout: publication
title: Unsupervised Natural Image Patch Learning
authors: Dov Danon, Hadar Averbuch-elor, Ohad Fried, Daniel Cohen-or
conference: Computational Visual Media
year: 2019
bibkey: danon2018unsupervised
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.03130'}]
tags: ["Unsupervised"]
short_authors: Danon et al.
---
Learning a metric of natural image patches is an important tool for analyzing
images. An efficient means is to train a deep network to map an image patch to
a vector space, in which the Euclidean distance reflects patch similarity.
Previous attempts learned such an embedding in a supervised manner, requiring
the availability of many annotated images. In this paper, we present an
unsupervised embedding of natural image patches, avoiding the need for
annotated images. The key idea is that the similarity of two patches can be
learned from the prevalence of their spatial proximity in natural images.
Clearly, relying on this simple principle, many spatially nearby pairs are
outliers, however, as we show, the outliers do not harm the convergence of the
metric learning. We show that our unsupervised embedding approach is more
effective than a supervised one or one that uses deep patch representations.
Moreover, we show that it naturally leads itself to an efficient
self-supervised domain adaptation technique onto a target domain that contains
a common foreground object.