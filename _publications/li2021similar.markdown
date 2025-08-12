---
layout: publication
title: 'Similar Scenes Arouse Similar Emotions: Parallel Data Augmentation For Stylized
  Image Captioning'
authors: Guodun Li, Yuchen Zhai, Zehao Lin, Yin Zhang
conference: Arxiv
year: 2021
bibkey: li2021similar
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.11912'}]
tags: []
short_authors: Li et al.
---
Stylized image captioning systems aim to generate a caption not only
semantically related to a given image but also consistent with a given style
description. One of the biggest challenges with this task is the lack of
sufficient paired stylized data. Many studies focus on unsupervised approaches,
without considering from the perspective of data augmentation. We begin with
the observation that people may recall similar emotions when they are in
similar scenes, and often express similar emotions with similar style phrases,
which underpins our data augmentation idea. In this paper, we propose a novel
Extract-Retrieve-Generate data augmentation framework to extract style phrases
from small-scale stylized sentences and graft them to large-scale factual
captions. First, we design the emotional signal extractor to extract style
phrases from small-scale stylized sentences. Second, we construct the plugable
multi-modal scene retriever to retrieve scenes represented with pairs of an
image and its stylized caption, which are similar to the query image or caption
in the large-scale factual data. In the end, based on the style phrases of
similar scenes and the factual description of the current scene, we build the
emotion-aware caption generator to generate fluent and diversified stylized
captions for the current scene. Extensive experimental results show that our
framework can alleviate the data scarcity problem effectively. It also
significantly boosts the performance of several existing image captioning
models in both supervised and unsupervised settings, which outperforms the
state-of-the-art stylized image captioning methods in terms of both sentence
relevance and stylishness by a substantial margin.