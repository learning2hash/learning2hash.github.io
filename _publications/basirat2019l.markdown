---
layout: publication
title: 'L*relu: Piece-wise Linear Activation Functions For Deep Fine-grained Visual
  Categorization'
authors: Mina Basirat, Peter M. Roth
conference: 2020 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2020
bibkey: basirat2019l
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.12259'}]
tags: []
short_authors: Mina Basirat, Peter M. Roth
---
Deep neural networks paved the way for significant improvements in image
visual categorization during the last years. However, even though the tasks are
highly varying, differing in complexity and difficulty, existing solutions
mostly build on the same architectural decisions. This also applies to the
selection of activation functions (AFs), where most approaches build on
Rectified Linear Units (ReLUs). In this paper, however, we show that the choice
of a proper AF has a significant impact on the classification accuracy, in
particular, if fine, subtle details are of relevance. Therefore, we propose to
model the degree of absence and the presence of features via the AF by using
piece-wise linear functions, which we refer to as L*ReLU. In this way, we can
ensure the required properties, while still inheriting the benefits in terms of
computational efficiency from ReLUs. We demonstrate our approach for the task
of Fine-grained Visual Categorization (FGVC), running experiments on seven
different benchmark datasets. The results do not only demonstrate superior
results but also that for different tasks, having different characteristics,
different AFs are selected.