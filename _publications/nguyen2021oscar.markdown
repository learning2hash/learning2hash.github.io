---
layout: publication
title: 'Oscar-net: Object-centric Scene Graph Attention For Image Attribution'
authors: Eric Nguyen, Tu Bui, Vishy Swaminathan, John Collomosse
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: nguyen2021oscar
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.03541'}]
tags: ["ICCV"]
short_authors: Nguyen et al.
---
Images tell powerful stories but cannot always be trusted. Matching images
back to trusted sources (attribution) enables users to make a more informed
judgment of the images they encounter online. We propose a robust image hashing
algorithm to perform such matching. Our hash is sensitive to manipulation of
subtle, salient visual details that can substantially change the story told by
an image. Yet the hash is invariant to benign transformations (changes in
quality, codecs, sizes, shapes, etc.) experienced by images during online
redistribution. Our key contribution is OSCAR-Net (Object-centric Scene Graph
Attention for Image Attribution Network); a robust image hashing model inspired
by recent successes of Transformers in the visual domain. OSCAR-Net constructs
a scene graph representation that attends to fine-grained changes of every
object's visual appearance and their spatial relationships. The network is
trained via contrastive learning on a dataset of original and manipulated
images yielding a state of the art image hash for content fingerprinting that
scales to millions of images.