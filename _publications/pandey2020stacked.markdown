---
layout: publication
title: Stacked Adversarial Network For Zero-shot Sketch Based Image Retrieval
authors: Anubha Pandey, Ashish Mishra, Vinay Kumar Verma, Anurag Mittal, Hema A. Murthy
conference: 2020 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2020
bibkey: pandey2020stacked
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.06657'}]
tags: ["Distance Metric Learning", "Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Pandey et al.
---
Conventional approaches to Sketch-Based Image Retrieval (SBIR) assume that
the data of all the classes are available during training. The assumption may
not always be practical since the data of a few classes may be unavailable, or
the classes may not appear at the time of training. Zero-Shot Sketch-Based
Image Retrieval (ZS-SBIR) relaxes this constraint and allows the algorithm to
handle previously unseen classes during the test. This paper proposes a
generative approach based on the Stacked Adversarial Network (SAN) and the
advantage of Siamese Network (SN) for ZS-SBIR. While SAN generates a
high-quality sample, SN learns a better distance metric compared to that of the
nearest neighbor search. The capability of the generative model to synthesize
image features based on the sketch reduces the SBIR problem to that of an
image-to-image retrieval problem. We evaluate the efficacy of our proposed
approach on TU-Berlin, and Sketchy database in both standard ZSL and
generalized ZSL setting. The proposed method yields a significant improvement
in standard ZSL as well as in a more challenging generalized ZSL setting (GZSL)
for SBIR.