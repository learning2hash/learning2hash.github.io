---
layout: publication
title: 'Mfnet: Multi-class Few-shot Segmentation Network With Pixel-wise Metric Learning'
authors: Miao Zhang, Miaojing Shi, Li Li
conference: Arxiv
year: 2021
bibkey: zhang2021mfnet
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.00232'}]
tags: ["Distance Metric Learning", "Few Shot & Zero Shot"]
short_authors: Miao Zhang, Miaojing Shi, Li Li
---
In visual recognition tasks, few-shot learning requires the ability to learn
object categories with few support examples. Its re-popularity in light of the
deep learning development is mainly in image classification. This work focuses
on few-shot semantic segmentation, which is still a largely unexplored field. A
few recent advances are often restricted to single-class few-shot segmentation.
In this paper, we first present a novel multi-way (class) encoding and decoding
architecture which effectively fuses multi-scale query information and
multi-class support information into one query-support embedding. Multi-class
segmentation is directly decoded upon this embedding. For better feature
fusion, a multi-level attention mechanism is proposed within the architecture,
which includes the attention for support feature modulation and attention for
multi-scale combination. Last, to enhance the embedding space learning, an
additional pixel-wise metric learning module is introduced with triplet loss
formulated on the pixel-level embedding of the input image. Extensive
experiments on standard benchmarks PASCAL-5i and COCO-20i show clear benefits
of our method over the state of the art in few-shot segmentation