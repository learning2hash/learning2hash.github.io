---
layout: publication
title: 'Grid Jigsaw Representation With CLIP: A New Perspective On Image Clustering'
authors: Zijie Song, Zhenzhen Hu, Richang Hong
conference: Multimedia Systems
year: 2025
bibkey: song2023grid
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.17869'}]
tags: ["Unsupervised"]
short_authors: Zijie Song, Zhenzhen Hu, Richang Hong
---
Unsupervised representation learning for image clustering is essential in
computer vision. Although the advancement of visual models has improved image
clustering with efficient visual representations, challenges still remain.
Firstly, existing features often lack the ability to represent the internal
structure of images, hindering the accurate clustering of visually similar
images. Secondly, finer-grained semantic labels are often missing, limiting the
ability to capture nuanced differences and similarities between images. In this
paper, we propose a new perspective on image clustering, the pretrain-based
Grid Jigsaw Representation (pGJR). Inspired by human jigsaw puzzle processing,
we modify the traditional jigsaw learning to gain a more sequential and
incremental understanding of image structure. We also leverage the pretrained
CLIP to extract the prior features which can benefit from the enhanced
cross-modal representation for richer and more nuanced semantic information and
label level differentiation. Our experiments demonstrate that using the
pretrained model as a feature extractor can accelerate the convergence of
clustering. We append the GJR module to pGJR and observe significant
improvements on common-use benchmark datasets. The experimental results
highlight the effectiveness of our approach in the clustering task, as
evidenced by improvements in the ACC, NMI, and ARI metrics, as well as the
super-fast convergence speed.