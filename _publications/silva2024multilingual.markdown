---
layout: publication
title: Multilingual Vision-language Pre-training For The Remote Sensing Domain
authors: "Jo\xE3o Daniel Silva, Joao Magalhaes, Devis Tuia, Bruno Martins"
conference: Proceedings of the 32nd ACM International Conference on Advances in Geographic
  Information Systems
year: 2024
bibkey: silva2024multilingual
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.23370'}]
tags: [Evaluation, Supervised, Few-shot & Zero-shot, Self-Supervised, Datasets, Multimodal
    Retrieval, Text Retrieval]
short_authors: Silva et al.
---
Methods based on Contrastive Language-Image Pre-training (CLIP) are nowadays
extensively used in support of vision-and-language tasks involving remote
sensing data, such as cross-modal retrieval. The adaptation of CLIP to this
specific domain has relied on model fine-tuning with the standard contrastive
objective, using existing human-labeled image-caption datasets, or using
synthetic data corresponding to image-caption pairs derived from other
annotations over remote sensing images (e.g., object classes). The use of
different pre-training mechanisms has received less attention, and only a few
exceptions have considered multilingual inputs. This work proposes a novel
vision-and-language model for the remote sensing domain, exploring the
fine-tuning of a multilingual CLIP model and testing the use of a
self-supervised method based on aligning local and global representations from
individual input images, together with the standard CLIP objective. Model
training relied on assembling pre-existing datasets of remote sensing images
paired with English captions, followed by the use of automated machine
translation into nine additional languages. We show that translated data is
indeed helpful, e.g. improving performance also on English. Our resulting
model, which we named Remote Sensing Multilingual CLIP (RS-M-CLIP), obtains
state-of-the-art results in a variety of vision-and-language tasks, including
cross-modal and multilingual image-text retrieval, or zero-shot image
classification.