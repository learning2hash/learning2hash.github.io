---
layout: publication
title: Deep Attentional Structured Representation Learning For Visual Recognition
authors: Krishna Kanth Nakka, Mathieu Salzmann
conference: Arxiv
year: 2018
bibkey: nakka2018deep
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.05389'}]
tags: []
short_authors: Krishna Kanth Nakka, Mathieu Salzmann
---
Structured representations, such as Bags of Words, VLAD and Fisher Vectors,
have proven highly effective to tackle complex visual recognition tasks. As
such, they have recently been incorporated into deep architectures. However,
while effective, the resulting deep structured representation learning
strategies typically aggregate local features from the entire image, ignoring
the fact that, in complex recognition tasks, some regions provide much more
discriminative information than others.
  In this paper, we introduce an attentional structured representation learning
framework that incorporates an image-specific attention mechanism within the
aggregation process. Our framework learns to predict jointly the image class
label and an attention map in an end-to-end fashion and without any other
supervision than the target label. As evidenced by our experiments, this
consistently outperforms attention-less structured representation learning and
yields state-of-the-art results on standard scene recognition and fine-grained
categorization benchmarks.