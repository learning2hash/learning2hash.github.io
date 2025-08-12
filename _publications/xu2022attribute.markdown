---
layout: publication
title: Attribute Prototype Network For Any-shot Learning
authors: Wenjia Xu, Yongqin Xian, Jiuniu Wang, Bernt Schiele, Zeynep Akata
conference: International Journal of Computer Vision
year: 2022
bibkey: xu2022attribute
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.01208'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Xu et al.
---
Any-shot image classification allows to recognize novel classes with only a
few or even zero samples. For the task of zero-shot learning, visual attributes
have been shown to play an important role, while in the few-shot regime, the
effect of attributes is under-explored. To better transfer attribute-based
knowledge from seen to unseen classes, we argue that an image representation
with integrated attribute localization ability would be beneficial for
any-shot, i.e. zero-shot and few-shot, image classification tasks. To this end,
we propose a novel representation learning framework that jointly learns
discriminative global and local features using only class-level attributes.
While a visual-semantic embedding layer learns global features, local features
are learned through an attribute prototype network that simultaneously
regresses and decorrelates attributes from intermediate features. Furthermore,
we introduce a zoom-in module that localizes and crops the informative regions
to encourage the network to learn informative features explicitly. We show that
our locality augmented image representations achieve a new state-of-the-art on
challenging benchmarks, i.e. CUB, AWA2, and SUN. As an additional benefit, our
model points to the visual evidence of the attributes in an image, confirming
the improved attribute localization ability of our image representation. The
attribute localization is evaluated quantitatively with ground truth part
annotations, qualitatively with visualizations, and through well-designed user
studies.