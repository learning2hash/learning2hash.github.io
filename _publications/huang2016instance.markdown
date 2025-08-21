---
layout: publication
title: Instance-aware Image And Sentence Matching With Selective Multimodal LSTM
authors: Yan Huang, Wei Wang, Liang Wang
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: huang2016instance
citations: 242
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.05588'}]
tags: ["CVPR", "Datasets", "Evaluation"]
short_authors: Yan Huang, Wei Wang, Liang Wang
---
Effective image and sentence matching depends on how to well measure their
global visual-semantic similarity. Based on the observation that such a global
similarity arises from a complex aggregation of multiple local similarities
between pairwise instances of image (objects) and sentence (words), we propose
a selective multimodal Long Short-Term Memory network (sm-LSTM) for
instance-aware image and sentence matching. The sm-LSTM includes a multimodal
context-modulated attention scheme at each timestep that can selectively attend
to a pair of instances of image and sentence, by predicting pairwise
instance-aware saliency maps for image and sentence. For selected pairwise
instances, their representations are obtained based on the predicted saliency
maps, and then compared to measure their local similarity. By similarly
measuring multiple local similarities within a few timesteps, the sm-LSTM
sequentially aggregates them with hidden states to obtain a final matching
score as the desired global similarity. Extensive experiments show that our
model can well match image and sentence with complex content, and achieve the
state-of-the-art results on two public benchmark datasets.