---
layout: publication
title: Image Captioning With Deep Bidirectional Lstms
authors: Cheng Wang, Haojin Yang, Christian Bartz, Christoph Meinel
conference: Proceedings of the 24th ACM international conference on Multimedia
year: 2016
bibkey: wang2016image
citations: 262
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.00790'}]
tags: [Evaluation, Datasets]
short_authors: Wang et al.
---
This work presents an end-to-end trainable deep bidirectional LSTM
(Long-Short Term Memory) model for image captioning. Our model builds on a deep
convolutional neural network (CNN) and two separate LSTM networks. It is
capable of learning long term visual-language interactions by making use of
history and future context information at high level semantic space. Two novel
deep bidirectional variant models, in which we increase the depth of
nonlinearity transition in different way, are proposed to learn hierarchical
visual-language embeddings. Data augmentation techniques such as multi-crop,
multi-scale and vertical mirror are proposed to prevent overfitting in training
deep models. We visualize the evolution of bidirectional LSTM internal states
over time and qualitatively analyze how our models "translate" image to
sentence. Our proposed models are evaluated on caption generation and
image-sentence retrieval tasks with three benchmark datasets: Flickr8K,
Flickr30K and MSCOCO datasets. We demonstrate that bidirectional LSTM models
achieve highly competitive performance to the state-of-the-art results on
caption generation even without integrating additional mechanism (e.g. object
detection, attention model etc.) and significantly outperform recent methods on
retrieval task.