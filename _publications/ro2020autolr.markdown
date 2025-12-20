---
layout: publication
title: 'Autolr: Layer-wise Pruning And Auto-tuning Of Learning Rates In Fine-tuning
  Of Deep Networks'
authors: Youngmin Ro, Jin Young Choi
conference: Arxiv
year: 2020
bibkey: ro2020autolr
citations: 1
additional_links: [{name: Code, url: 'https://github.com/youngminPIL/AutoLR'}, {name: Paper,
    url: 'https://arxiv.org/abs/2002.06048'}]
tags: ["Datasets", "Evaluation", "Image Retrieval"]
short_authors: Youngmin Ro, Jin Young Choi
---
Existing fine-tuning methods use a single learning rate over all layers. In
this paper, first, we discuss that trends of layer-wise weight variations by
fine-tuning using a single learning rate do not match the well-known notion
that lower-level layers extract general features and higher-level layers
extract specific features. Based on our discussion, we propose an algorithm
that improves fine-tuning performance and reduces network complexity through
layer-wise pruning and auto-tuning of layer-wise learning rates. The proposed
algorithm has verified the effectiveness by achieving state-of-the-art
performance on the image retrieval benchmark datasets (CUB-200, Cars-196,
Stanford online product, and Inshop). Code is available at
https://github.com/youngminPIL/AutoLR.