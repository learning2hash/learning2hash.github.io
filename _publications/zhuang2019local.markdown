---
layout: publication
title: Local Aggregation For Unsupervised Learning Of Visual Embeddings
authors: Chengxu Zhuang, Alex Lin Zhai, Daniel Yamins
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: zhuang2019local
citations: 408
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.12355'}]
tags: ["Datasets", "Evaluation", "ICCV", "Supervised", "Unsupervised"]
short_authors: Chengxu Zhuang, Alex Lin Zhai, Daniel Yamins
---
Unsupervised approaches to learning in neural networks are of substantial
interest for furthering artificial intelligence, both because they would enable
the training of networks without the need for large numbers of expensive
annotations, and because they would be better models of the kind of
general-purpose learning deployed by humans. However, unsupervised networks
have long lagged behind the performance of their supervised counterparts,
especially in the domain of large-scale visual recognition. Recent developments
in training deep convolutional embeddings to maximize non-parametric instance
separation and clustering objectives have shown promise in closing this gap.
Here, we describe a method that trains an embedding function to maximize a
metric of local aggregation, causing similar data instances to move together in
the embedding space, while allowing dissimilar instances to separate. This
aggregation metric is dynamic, allowing soft clusters of different scales to
emerge. We evaluate our procedure on several large-scale visual recognition
datasets, achieving state-of-the-art unsupervised transfer learning performance
on object recognition in ImageNet, scene recognition in Places 205, and object
detection in PASCAL VOC.