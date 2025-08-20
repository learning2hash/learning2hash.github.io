---
layout: publication
title: Learning An Ensemble Of Deep Fingerprint Representations
authors: Akash Godbole, Karthik Nandakumar, Anil K. Jain
conference: Arxiv
year: 2022
bibkey: godbole2022learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.02425'}]
tags: [Uncategorized]
short_authors: Akash Godbole, Karthik Nandakumar, Anil K. Jain
---
Deep neural networks (DNNs) have shown incredible promise in learning
fixed-length representations from fingerprints. Since the representation
learning is often focused on capturing specific prior knowledge (e.g.,
minutiae), there is no universal representation that comprehensively
encapsulates all the discriminatory information available in a fingerprint.
While learning an ensemble of representations can mitigate this problem, two
critical challenges need to be addressed: (i) How to extract multiple diverse
representations from the same fingerprint image? and (ii) How to optimally
exploit these representations during the matching process? In this work, we
train multiple instances of DeepPrint (a state-of-the-art DNN-based fingerprint
encoder) on different transformations of the input image to generate an
ensemble of fingerprint embeddings. We also propose a feature fusion technique
that distills these multiple representations into a single embedding, which
faithfully captures the diversity present in the ensemble without increasing
the computational complexity. The proposed approach has been comprehensively
evaluated on five databases containing rolled, plain, and latent fingerprints
(NIST SD4, NIST SD14, NIST SD27, NIST SD302, and FVC2004 DB2A) and
statistically significant improvements in accuracy have been consistently
demonstrated across a range of verification as well as closed- and open-set
identification settings. The proposed approach serves as a wrapper capable of
improving the accuracy of any DNN-based recognition system.