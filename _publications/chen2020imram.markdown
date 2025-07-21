---
layout: publication
title: 'IMRAM: Iterative Matching With Recurrent Attention Memory For Cross-modal
  Image-text Retrieval'
authors: Chen et al.
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: chen2020imram
citations: 337
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.03772'}]
tags: ["Text-Retrieval", "CVPR"]
---
Enabling bi-directional retrieval of images and texts is important for
understanding the correspondence between vision and language. Existing methods
leverage the attention mechanism to explore such correspondence in a
fine-grained manner. However, most of them consider all semantics equally and
thus align them uniformly, regardless of their diverse complexities. In fact,
semantics are diverse (i.e. involving different kinds of semantic concepts),
and humans usually follow a latent structure to combine them into
understandable languages. It may be difficult to optimally capture such
sophisticated correspondences in existing methods. In this paper, to address
such a deficiency, we propose an Iterative Matching with Recurrent Attention
Memory (IMRAM) method, in which correspondences between images and texts are
captured with multiple steps of alignments. Specifically, we introduce an
iterative matching scheme to explore such fine-grained correspondence
progressively. A memory distillation unit is used to refine alignment knowledge
from early steps to later ones. Experiment results on three benchmark datasets,
i.e. Flickr8K, Flickr30K, and MS COCO, show that our IMRAM achieves
state-of-the-art performance, well demonstrating its effectiveness. Experiments
on a practical business advertisement dataset, named \Ads\{\}, further validates
the applicability of our method in practical scenarios.