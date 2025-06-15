---
layout: publication
title: 'Training Vision Transformers For Image Retrieval'
authors: Alaaeldin El-nouby, Natalia Neverova, Ivan Laptev, Hervé Jégou
conference: "Arxiv"
year: 2021
citations: 120
bibkey: elnouby2021training
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2102.05644'}
tags: ['Evaluation Metrics', 'Loss Functions', 'Applications']
---
Transformers have shown outstanding results for natural language
understanding and, more recently, for image classification. We here extend this
work and propose a transformer-based approach for image retrieval: we adopt
vision transformers for generating image descriptors and train the resulting
model with a metric learning objective, which combines a contrastive loss with
a differential entropy regularizer. Our results show consistent and significant
improvements of transformers over convolution-based approaches. In particular,
our method outperforms the state of the art on several public benchmarks for
category-level retrieval, namely Stanford Online Product, In-Shop and CUB-200.
Furthermore, our experiments on ROxford and RParis also show that, in
comparable settings, transformers are competitive for particular object
retrieval, especially in the regime of short vector representations and
low-resolution images.
