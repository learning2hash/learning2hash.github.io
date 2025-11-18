---
layout: publication
title: Curriculum Learning For Data-efficient Vision-language Alignment
authors: Tejas Srinivasan, Xiang Ren, Jesse Thomason
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2022
bibkey: srinivasan2022curriculum
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.14525'}]
tags: ["CVPR", "Few Shot & Zero Shot", "Image Retrieval", "Self-Supervised"]
short_authors: Tejas Srinivasan, Xiang Ren, Jesse Thomason
---
Aligning image and text encoders from scratch using contrastive learning
requires large amounts of paired image-text data. We alleviate this need by
aligning individually pre-trained language and vision representation models
using a much smaller amount of paired data, augmented with a curriculum
learning algorithm to learn fine-grained vision-language alignments. TOnICS
(Training with Ontology-Informed Contrastive Sampling) initially samples
minibatches whose image-text pairs contain a wide variety of objects to learn
object-level alignment, and progressively samples minibatches where all
image-text pairs contain the same object to learn finer-grained contextual
alignment. Aligning pre-trained BERT and VinVL models to each other using
TOnICS outperforms CLIP on downstream zero-shot image retrieval while using
less than 1% as much training data.