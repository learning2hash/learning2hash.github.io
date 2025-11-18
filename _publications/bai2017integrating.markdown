---
layout: publication
title: Integrating Scene Text And Visual Appearance For Fine-grained Image Classification
authors: Xiang Bai, Mingkun Yang, Pengyuan Lyu, Yongchao Xu, Jiebo Luo
conference: IEEE Access
year: 2017
bibkey: bai2017integrating
citations: 64
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.04613'}]
tags: ["Datasets", "Evaluation", "Tools & Libraries"]
short_authors: Bai et al.
---
Text in natural images contains rich semantics that are often highly relevant
to objects or scene. In this paper, we focus on the problem of fully exploiting
scene text for visual understanding. The main idea is combining word
representations and deep visual features into a globally trainable deep
convolutional neural network. First, the recognized words are obtained by a
scene text reading system. Then, we combine the word embedding of the
recognized words and the deep visual features into a single representation,
which is optimized by a convolutional neural network for fine-grained image
classification. In our framework, the attention mechanism is adopted to reveal
the relevance between each recognized word and the given image, which further
enhances the recognition performance. We have performed experiments on two
datasets: Con-Text dataset and Drink Bottle dataset, that are proposed for
fine-grained classification of business places and drink bottles, respectively.
The experimental results consistently demonstrate that the proposed method
combining textual and visual cues significantly outperforms classification with
only visual representations. Moreover, we have shown that the learned
representation improves the retrieval performance on the drink bottle images by
a large margin, making it potentially useful in product search.