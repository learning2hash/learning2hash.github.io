---
layout: publication
title: Transfer Learning By Ranking For Weakly Supervised Object Annotation
authors: Zhiyuan Shi, Parthipan Siva, Tao Xiang
conference: Procedings of the British Machine Vision Conference 2012
year: 2012
bibkey: shi2012transfer
citations: 55
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.00873'}]
tags: ["Supervised"]
short_authors: Zhiyuan Shi, Parthipan Siva, Tao Xiang
---
Most existing approaches to training object detectors rely on fully
supervised learning, which requires the tedious manual annotation of object
location in a training set. Recently there has been an increasing interest in
developing weakly supervised approach to detector training where the object
location is not manually annotated but automatically determined based on binary
(weak) labels indicating if a training image contains the object. This is a
challenging problem because each image can contain many candidate object
locations which partially overlaps the object of interest. Existing approaches
focus on how to best utilise the binary labels for object location annotation.
In this paper we propose to solve this problem from a very different
perspective by casting it as a transfer learning problem. Specifically, we
formulate a novel transfer learning based on learning to rank, which
effectively transfers a model for automatic annotation of object location from
an auxiliary dataset to a target dataset with completely unrelated object
categories. We show that our approach outperforms existing state-of-the-art
weakly supervised approach to annotating objects in the challenging VOC
dataset.