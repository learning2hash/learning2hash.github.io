---
layout: publication
title: Boost Image Captioning With Knowledge Reasoning
authors: Feicheng Huang, Zhixin Li, Haiyang Wei, Canlong Zhang, Huifang Ma
conference: Machine Learning
year: 2020
bibkey: huang2020boost
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.00927'}]
tags: []
short_authors: Huang et al.
---
Automatically generating a human-like description for a given image is a
potential research in artificial intelligence, which has attracted a great of
attention recently. Most of the existing attention methods explore the mapping
relationships between words in sentence and regions in image, such
unpredictable matching manner sometimes causes inharmonious alignments that may
reduce the quality of generated captions. In this paper, we make our efforts to
reason about more accurate and meaningful captions. We first propose word
attention to improve the correctness of visual attention when generating
sequential descriptions word-by-word. The special word attention emphasizes on
word importance when focusing on different regions of the input image, and
makes full use of the internal annotation knowledge to assist the calculation
of visual attention. Then, in order to reveal those incomprehensible intentions
that cannot be expressed straightforwardly by machines, we introduce a new
strategy to inject external knowledge extracted from knowledge graph into the
encoder-decoder framework to facilitate meaningful captioning. Finally, we
validate our model on two freely available captioning benchmarks: Microsoft
COCO dataset and Flickr30k dataset. The results demonstrate that our approach
achieves state-of-the-art performance and outperforms many of the existing
approaches.