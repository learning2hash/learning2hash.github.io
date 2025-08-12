---
layout: publication
title: Attribute-centered Loss For Soft-biometrics Guided Face Sketch-photo Recognition
authors: Hadi Kazemi, Sobhan Soleymani, Ali Dabouei, Mehdi Iranmanesh, Nasser M. Nasrabadi
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2018
bibkey: kazemi2018attribute
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.03082'}]
tags: ["CVPR"]
short_authors: Kazemi et al.
---
Face sketches are able to capture the spatial topology of a face while
lacking some facial attributes such as race, skin, or hair color. Existing
sketch-photo recognition approaches have mostly ignored the importance of
facial attributes. In this paper, we propose a new loss function, called
attribute-centered loss, to train a Deep Coupled Convolutional Neural Network
(DCCNN) for the facial attribute guided sketch to photo matching. Specifically,
an attribute-centered loss is proposed which learns several distinct centers,
in a shared embedding space, for photos and sketches with different
combinations of attributes. The DCCNN simultaneously is trained to map photos
and pairs of testified attributes and corresponding forensic sketches around
their associated centers, while preserving the spatial topology information.
Importantly, the centers learn to keep a relative distance from each other,
related to their number of contradictory attributes. Extensive experiments are
performed on composite (E-PRIP) and semi-forensic (IIIT-D Semi-forensic)
databases. The proposed method significantly outperforms the state-of-the-art.