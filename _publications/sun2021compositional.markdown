---
layout: publication
title: A Compositional Feature Embedding And Similarity Metric For Ultra-fine-grained
  Visual Categorization
authors: Yajie Sun, Miaohua Zhang, Xiaohan Yu, Yi Liao, Yongsheng Gao
conference: '2021 Digital Image Computing: Techniques and Applications (DICTA)'
year: 2021
bibkey: sun2021compositional
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.12380'}]
tags: ["Distance Metric Learning"]
short_authors: Sun et al.
---
Fine-grained visual categorization (FGVC), which aims at classifying objects
with small inter-class variances, has been significantly advanced in recent
years. However, ultra-fine-grained visual categorization (ultra-FGVC), which
targets at identifying subclasses with extremely similar patterns, has not
received much attention. In ultra-FGVC datasets, the samples per category are
always scarce as the granularity moves down, which will lead to overfitting
problems. Moreover, the difference among different categories is too subtle to
distinguish even for professional experts. Motivated by these issues, this
paper proposes a novel compositional feature embedding and similarity metric
(CECS). Specifically, in the compositional feature embedding module, we
randomly select patches in the original input image, and these patches are then
replaced by patches from the images of different categories or masked out. Then
the replaced and masked images are used to augment the original input images,
which can provide more diverse samples and thus largely alleviate overfitting
problem resulted from limited training samples. Besides, learning with diverse
samples forces the model to learn not only the most discriminative features but
also other informative features in remaining regions, enhancing the
generalization and robustness of the model. In the compositional similarity
metric module, a new similarity metric is developed to improve the
classification performance by narrowing the intra-category distance and
enlarging the inter-category distance. Experimental results on two ultra-FGVC
datasets and one FGVC dataset with recent benchmark methods consistently
demonstrate that the proposed CECS method achieves the state of-the-art
performance.