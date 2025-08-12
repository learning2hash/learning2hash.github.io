---
layout: publication
title: Rethinking Image-based Table Recognition Using Weakly Supervised Methods
authors: Nam Tuan Ly, Atsuhiro Takasu, Phuc Nguyen, Hideaki Takeda
conference: Proceedings of the 12th International Conference on Pattern Recognition
  Applications and Methods
year: 2023
bibkey: ly2023rethinking
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.07641'}]
tags: []
short_authors: Ly et al.
---
Most of the previous methods for table recognition rely on training datasets
containing many richly annotated table images. Detailed table image annotation,
e.g., cell or text bounding box annotation, however, is costly and often
subjective. In this paper, we propose a weakly supervised model named WSTabNet
for table recognition that relies only on HTML (or LaTeX) code-level
annotations of table images. The proposed model consists of three main parts:
an encoder for feature extraction, a structure decoder for generating table
structure, and a cell decoder for predicting the content of each cell in the
table. Our system is trained end-to-end by stochastic gradient descent
algorithms, requiring only table images and their ground-truth HTML (or LaTeX)
representations. To facilitate table recognition with deep learning, we create
and release WikiTableSet, the largest publicly available image-based table
recognition dataset built from Wikipedia. WikiTableSet contains nearly 4
million English table images, 590K Japanese table images, and 640k French table
images with corresponding HTML representation and cell bounding boxes. The
extensive experiments on WikiTableSet and two large-scale datasets: FinTabNet
and PubTabNet demonstrate that the proposed weakly supervised model achieves
better, or similar accuracies compared to the state-of-the-art models on all
benchmark datasets.