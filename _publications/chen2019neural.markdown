---
layout: publication
title: 'Neural Storyboard Artist: Visualizing Stories With Coherent Image Sequences'
authors: Shizhe Chen, Bei Liu, Jianlong Fu, Ruihua Song, Qin Jin, Pingping Lin, Xiaoyu
  Qi, Chunting Wang, Jin Zhou
conference: Arxiv
year: 2019
bibkey: chen2019neural
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.10460'}]
tags: ["Tools & Libraries"]
short_authors: Chen et al.
---
A storyboard is a sequence of images to illustrate a story containing
multiple sentences, which has been a key process to create different story
products. In this paper, we tackle a new multimedia task of automatic
storyboard creation to facilitate this process and inspire human artists.
Inspired by the fact that our understanding of languages is based on our past
experience, we propose a novel inspire-and-create framework with a
story-to-image retriever that selects relevant cinematic images for inspiration
and a storyboard creator that further refines and renders images to improve the
relevancy and visual consistency. The proposed retriever dynamically employs
contextual information in the story with hierarchical attentions and applies
dense visual-semantic matching to accurately retrieve and ground images. The
creator then employs three rendering steps to increase the flexibility of
retrieved images, which include erasing irrelevant regions, unifying styles of
images and substituting consistent characters. We carry out extensive
experiments on both in-domain and out-of-domain visual story datasets. The
proposed model achieves better quantitative performance than the
state-of-the-art baselines for storyboard creation. Qualitative visualizations
and user studies further verify that our approach can create high-quality
storyboards even for stories in the wild.