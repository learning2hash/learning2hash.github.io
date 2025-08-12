---
layout: publication
title: Revisiting Few-shot Activity Detection With Class Similarity Control
authors: Huijuan Xu, Ximeng Sun, Eric Tzeng, Abir Das, Kate Saenko, Trevor Darrell
conference: Arxiv
year: 2020
bibkey: xu2020revisiting
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.00137'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Xu et al.
---
Many interesting events in the real world are rare making preannotated
machine learning ready videos a rarity in consequence. Thus, temporal activity
detection models that are able to learn from a few examples are desirable. In
this paper, we present a conceptually simple and general yet novel framework
for few-shot temporal activity detection based on proposal regression which
detects the start and end time of the activities in untrimmed videos. Our model
is end-to-end trainable, takes into account the frame rate differences between
few-shot activities and untrimmed test videos, and can benefit from additional
few-shot examples. We experiment on three large scale benchmarks for temporal
activity detection (ActivityNet1.2, ActivityNet1.3 and THUMOS14 datasets) in a
few-shot setting. We also study the effect on performance of different amount
of overlap with activities used to pretrain the video classification backbone
and propose corrective measures for future works in this domain. Our code will
be made available.