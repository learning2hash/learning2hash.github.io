---
layout: publication
title: End-to-end Biomedical Entity Linking With Span-based Dictionary Matching
authors: Shogo Ujiie, Hayate Iso, Shuntaro Yada, Shoko Wakamiya, Eiji Aramaki
conference: Proceedings of the 20th Workshop on Biomedical Language Processing
year: 2021
bibkey: ujiie2021end
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.10493'}]
tags: ["Datasets", "Evaluation"]
short_authors: Ujiie et al.
---
Disease name recognition and normalization, which is generally called
biomedical entity linking, is a fundamental process in biomedical text mining.
Recently, neural joint learning of both tasks has been proposed to utilize the
mutual benefits. While this approach achieves high performance, disease
concepts that do not appear in the training dataset cannot be accurately
predicted. This study introduces a novel end-to-end approach that combines span
representations with dictionary-matching features to address this problem. Our
model handles unseen concepts by referring to a dictionary while maintaining
the performance of neural network-based models, in an end-to-end fashion.
Experiments using two major datasets demonstrate that our model achieved
competitive results with strong baselines, especially for unseen concepts
during training.