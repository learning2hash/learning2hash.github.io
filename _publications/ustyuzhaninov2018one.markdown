---
layout: publication
title: One-shot Texture Segmentation
authors: Ivan Ustyuzhaninov, Claudio Michaelis, Wieland Brendel, Matthias Bethge
conference: Arxiv
year: 2018
bibkey: ustyuzhaninov2018one
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.02654'}]
tags: []
short_authors: Ustyuzhaninov et al.
---
We introduce one-shot texture segmentation: the task of segmenting an input
image containing multiple textures given a patch of a reference texture. This
task is designed to turn the problem of texture-based perceptual grouping into
an objective benchmark. We show that it is straight-forward to generate large
synthetic data sets for this task from a relatively small number of natural
textures. In particular, this task can be cast as a self-supervised problem
thereby alleviating the need for massive amounts of manually annotated data
necessary for traditional segmentation tasks. In this paper we introduce and
study two concrete data sets: a dense collage of textures (CollTex) and a
cluttered texturized Omniglot data set. We show that a baseline model trained
on these synthesized data is able to generalize to natural images and videos
without further fine-tuning, suggesting that the learned image representations
are useful for higher-level vision tasks.