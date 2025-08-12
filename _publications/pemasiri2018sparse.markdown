---
layout: publication
title: Sparse Over-complete Patch Matching
authors: Akila Pemasiri, Kien Nguyen, Sridha Sridharan, Clinton Fookes
conference: Pattern Recognition Letters
year: 2019
bibkey: pemasiri2018sparse
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.03556'}]
tags: []
short_authors: Pemasiri et al.
---
Image patch matching, which is the process of identifying corresponding
patches across images, has been used as a subroutine for many computer vision
and image processing tasks. State -of-the-art patch matching techniques take
image patches as input to a convolutional neural network to extract the patch
features and evaluate their similarity. Our aim in this paper is to improve on
the state of the art patch matching techniques by observing the fact that a
sparse-overcomplete representation of an image posses statistical properties of
natural visual scenes which can be exploited for patch matching. We propose a
new paradigm which encodes image patch details by encoding the patch and
subsequently using this sparse representation as input to a neural network to
compare the patches. As sparse coding is based on a generative model of natural
image patches, it can represent the patch in terms of the fundamental visual
components from which it has been composed of, leading to similar sparse codes
for patches which are built from similar components. Once the sparse coded
features are extracted, we employ a fully-connected neural network, which
captures the non-linear relationships between features, for comparison. We have
evaluated our approach using the Liberty and Notredame subsets of the popular
UBC patch dataset and set a new benchmark outperforming all state-of-the-art
patch matching techniques for these datasets.