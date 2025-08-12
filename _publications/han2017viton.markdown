---
layout: publication
title: 'VITON: An Image-based Virtual Try-on Network'
authors: Xintong Han, Zuxuan Wu, Zhe Wu, Ruichi Yu, Larry S. Davis
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: han2017viton
citations: 527
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.08447'}]
tags: ["CVPR"]
short_authors: Han et al.
---
We present an image-based VIirtual Try-On Network (VITON) without using 3D
information in any form, which seamlessly transfers a desired clothing item
onto the corresponding region of a person using a coarse-to-fine strategy.
Conditioned upon a new clothing-agnostic yet descriptive person representation,
our framework first generates a coarse synthesized image with the target
clothing item overlaid on that same person in the same pose. We further enhance
the initial blurry clothing area with a refinement network. The network is
trained to learn how much detail to utilize from the target clothing item, and
where to apply to the person in order to synthesize a photo-realistic image in
which the target item deforms naturally with clear visual patterns. Experiments
on our newly collected Zalando dataset demonstrate its promise in the
image-based virtual try-on task over state-of-the-art generative models.