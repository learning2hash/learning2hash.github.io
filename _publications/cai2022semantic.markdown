---
layout: publication
title: Semantic-enhanced Image Clustering
authors: Shaotian Cai, Liping Qiu, Xiaojun Chen, Qin Zhang, Longteng Chen
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2023
bibkey: cai2022semantic
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.09849'}]
tags: ["AAAI"]
short_authors: Cai et al.
---
Image clustering is an important and open-challenging task in computer
vision. Although many methods have been proposed to solve the image clustering
task, they only explore images and uncover clusters according to the image
features, thus being unable to distinguish visually similar but semantically
different images. In this paper, we propose to investigate the task of image
clustering with the help of a visual-language pre-training model. Different
from the zero-shot setting, in which the class names are known, we only know
the number of clusters in this setting. Therefore, how to map images to a
proper semantic space and how to cluster images from both image and semantic
spaces are two key problems. To solve the above problems, we propose a novel
image clustering method guided by the visual-language pre-training model CLIP,
named \textbf\{Semantic-Enhanced Image Clustering (SIC)\}. In this new method, we
propose a method to map the given images to a proper semantic space first and
efficient methods to generate pseudo-labels according to the relationships
between images and semantics. Finally, we propose performing clustering with
consistency learning in both image space and semantic space, in a
self-supervised learning fashion. The theoretical result of convergence
analysis shows that our proposed method can converge at a sublinear speed.
Theoretical analysis of expectation risk also shows that we can reduce the
expected risk by improving neighborhood consistency, increasing prediction
confidence, or reducing neighborhood imbalance. Experimental results on five
benchmark datasets clearly show the superiority of our new method.