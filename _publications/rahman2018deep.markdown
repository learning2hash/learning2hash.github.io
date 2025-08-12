---
layout: publication
title: Deep Multiple Instance Learning For Zero-shot Image Tagging
authors: Shafin Rahman, Salman Khan
conference: IEEE Transactions on Multimedia
year: 2019
bibkey: rahman2018deep
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.06051'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Shafin Rahman, Salman Khan
---
In-line with the success of deep learning on traditional recognition problem,
several end-to-end deep models for zero-shot recognition have been proposed in
the literature. These models are successful to predict a single unseen label
given an input image, but does not scale to cases where multiple unseen objects
are present. In this paper, we model this problem within the framework of
Multiple Instance Learning (MIL). To the best of our knowledge, we propose the
first end-to-end trainable deep MIL framework for the multi-label zero-shot
tagging problem. Due to its novel design, the proposed framework has several
interesting features: (1) Unlike previous deep MIL models, it does not use any
off-line procedure (e.g., Selective Search or EdgeBoxes) for bag generation.
(2) During test time, it can process any number of unseen labels given their
semantic embedding vectors. (3) Using only seen labels per image as weak
annotation, it can produce a bounding box for each predicted labels. We
experiment with the NUS-WIDE dataset and achieve superior performance across
conventional, zero-shot and generalized zero-shot tagging tasks.