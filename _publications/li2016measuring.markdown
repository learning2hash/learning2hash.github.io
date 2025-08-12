---
layout: publication
title: Measuring And Predicting Tag Importance For Image Retrieval
authors: Shangwen Li, Sanjay Purushotham, Chen Chen, Yuzhuo Ren, C. -c. Jay Kuo
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2017
bibkey: li2016measuring
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.08680'}]
tags: ["Image Retrieval"]
short_authors: Li et al.
---
Textual data such as tags, sentence descriptions are combined with visual
cues to reduce the semantic gap for image retrieval applications in today's
Multimodal Image Retrieval (MIR) systems. However, all tags are treated as
equally important in these systems, which may result in misalignment between
visual and textual modalities during MIR training. This will further lead to
degenerated retrieval performance at query time. To address this issue, we
investigate the problem of tag importance prediction, where the goal is to
automatically predict the tag importance and use it in image retrieval. To
achieve this, we first propose a method to measure the relative importance of
object and scene tags from image sentence descriptions. Using this as the
ground truth, we present a tag importance prediction model to jointly exploit
visual, semantic and context cues. The Structural Support Vector Machine (SSVM)
formulation is adopted to ensure efficient training of the prediction model.
Then, the Canonical Correlation Analysis (CCA) is employed to learn the
relation between the image visual feature and tag importance to obtain robust
retrieval performance. Experimental results on three real-world datasets show a
significant performance improvement of the proposed MIR with Tag Importance
Prediction (MIR/TIP) system over other MIR systems.