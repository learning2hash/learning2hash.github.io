---
layout: publication
title: 'Cobnet: Cross Attention On Object And Background For Few-shot Segmentation'
authors: Haoyan Guan, Michael Spratling
conference: 2022 26th International Conference on Pattern Recognition (ICPR)
year: 2022
bibkey: guan2022cobnet
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.11968'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Haoyan Guan, Michael Spratling
---
Few-shot segmentation aims to segment images containing objects from
previously unseen classes using only a few annotated samples. Most current
methods focus on using object information extracted, with the aid of human
annotations, from support images to identify the same objects in new query
images. However, background information can also be useful to distinguish
objects from their surroundings. Hence, some previous methods also extract
background information from the support images. In this paper, we argue that
such information is of limited utility, as the background in different images
can vary widely. To overcome this issue, we propose CobNet which utilises
information about the background that is extracted from the query images
without annotations of those images. Experiments show that our method achieves
a mean Intersection-over-Union score of 61.4% and 37.8% for 1-shot segmentation
on PASCAL-5i and COCO-20i respectively, outperforming previous methods. It is
also shown to produce state-of-the-art performances of 53.7% for
weakly-supervised few-shot segmentation, where no annotations are provided for
the support images.