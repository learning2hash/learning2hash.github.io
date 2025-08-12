---
layout: publication
title: Clockwork Convnets For Video Semantic Segmentation
authors: Evan Shelhamer, Kate Rakelly, Judy Hoffman, Trevor Darrell
conference: Lecture Notes in Computer Science
year: 2016
bibkey: shelhamer2016clockwork
citations: 196
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1608.03609'}]
tags: []
short_authors: Shelhamer et al.
---
Recent years have seen tremendous progress in still-image segmentation;
however the na\"ive application of these state-of-the-art algorithms to every
video frame requires considerable computation and ignores the temporal
continuity inherent in video. We propose a video recognition framework that
relies on two key observations: 1) while pixels may change rapidly from frame
to frame, the semantic content of a scene evolves more slowly, and 2) execution
can be viewed as an aspect of architecture, yielding purpose-fit computation
schedules for networks. We define a novel family of "clockwork" convnets driven
by fixed or adaptive clock signals that schedule the processing of different
layers at different update rates according to their semantic stability. We
design a pipeline schedule to reduce latency for real-time recognition and a
fixed-rate schedule to reduce overall computation. Finally, we extend clockwork
scheduling to adaptive video processing by incorporating data-driven clocks
that can be tuned on unlabeled video. The accuracy and efficiency of clockwork
convnets are evaluated on the Youtube-Objects, NYUD, and Cityscapes video
datasets.