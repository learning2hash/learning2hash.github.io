---
layout: publication
title: Fast Zero-shot Image Tagging
authors: Yang Zhang, Boqing Gong, Mubarak Shah
conference: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2016
bibkey: zhang2016fast
citations: 102
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1605.09759'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Yang Zhang, Boqing Gong, Mubarak Shah
---
The well-known word analogy experiments show that the recent word vectors
capture fine-grained linguistic regularities in words by linear vector offsets,
but it is unclear how well the simple vector offsets can encode visual
regularities over words. We study a particular image-word relevance relation in
this paper. Our results show that the word vectors of relevant tags for a given
image rank ahead of the irrelevant tags, along a principal direction in the
word vector space. Inspired by this observation, we propose to solve image
tagging by estimating the principal direction for an image. Particularly, we
exploit linear mappings and nonlinear deep neural networks to approximate the
principal direction from an input image. We arrive at a quite versatile tagging
model. It runs fast given a test image, in constant time w.r.t.\ the training
set size. It not only gives superior performance for the conventional tagging
task on the NUS-WIDE dataset, but also outperforms competitive baselines on
annotating images with previously unseen tags