---
layout: publication
title: Zero-shot Image Captioning By Anchor-augmented Vision-language Space Alignment
authors: Junyang Wang, Yi Zhang, Ming Yan, Ji Zhang, Jitao Sang
conference: Arxiv
year: 2022
bibkey: wang2022zero
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.07275'}]
tags: ["Image Retrieval"]
short_authors: Wang et al.
---
CLIP (Contrastive Language-Image Pre-Training) has shown remarkable zero-shot
transfer capabilities in cross-modal correlation tasks such as visual
classification and image retrieval. However, its performance in cross-modal
generation tasks like zero-shot image captioning remains unsatisfied. In this
work, we discuss that directly employing CLIP for zero-shot image captioning
relies more on the textual modality in context and largely ignores the visual
information, which we call *contextual language prior*. To address this,
we propose Cross-modal Language Models (CLMs) to facilitate unsupervised
cross-modal learning. We further propose Anchor Augment to guide the generative
model's attention to the fine-grained information in the representation of
CLIP. Experiments on MS COCO and Flickr 30K validate the promising performance
of proposed approach in both captioning quality and computational efficiency.