---
layout: publication
title: Self-supervised Semantic Segmentation Grounded In Visual Concepts
authors: Wenbin He, William Surmeier, Arvind Kumar Shekar, Liang Gou, Liu Ren
conference: Proceedings of the Thirty-First International Joint Conference on Artificial
  Intelligence
year: 2022
bibkey: he2022self
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.13868'}]
tags: ["IJCAI", "Self-Supervised"]
short_authors: He et al.
---
Unsupervised semantic segmentation requires assigning a label to every pixel
without any human annotations. Despite recent advances in self-supervised
representation learning for individual images, unsupervised semantic
segmentation with pixel-level representations is still a challenging task and
remains underexplored. In this work, we propose a self-supervised pixel
representation learning method for semantic segmentation by using visual
concepts (i.e., groups of pixels with semantic meanings, such as parts,
objects, and scenes) extracted from images. To guide self-supervised learning,
we leverage three types of relationships between pixels and concepts, including
the relationships between pixels and local concepts, local and global concepts,
as well as the co-occurrence of concepts. We evaluate the learned pixel
embeddings and visual concepts on three datasets, including PASCAL VOC 2012,
COCO 2017, and DAVIS 2017. Our results show that the proposed method gains
consistent and substantial improvements over recent unsupervised semantic
segmentation approaches, and also demonstrate that visual concepts can reveal
insights into image datasets.