---
layout: publication
title: Social Anchor-unit Graph Regularized Tensor Completion For Large-scale Image
  Retagging
authors: Jinhui Tang, Xiangbo Shu, Zechao Li, Yu-gang Jiang, Qi Tian
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2019
bibkey: tang2018social
citations: 76
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.04397'}]
tags: ["Scalability"]
short_authors: Tang et al.
---
Image retagging aims to improve tag quality of social images by refining
their original tags or assigning new high-quality tags. Recent approaches
simultaneously explore visual, user and tag information to improve the
performance of image retagging by constructing and exploring an image-tag-user
graph. However, such methods will become computationally infeasible with the
rapidly increasing number of images, tags and users. It has been proven that
Anchor Graph Regularization (AGR) can significantly accelerate large-scale
graph learning model by exploring only a small number of anchor points.
Inspired by this, we propose a novel Social anchor-Unit GrAph Regularized
Tensor Completion (SUGAR-TC) method to effectively refine the tags of social
images, which is insensitive to the scale of the applied data. First, we
construct an anchor-unit graph across multiple domains (e.g., image and user
domains) rather than traditional anchor graph in a single domain. Second, a
tensor completion based on SUGAR is implemented on the original image-tag-user
tensor to refine the tags of the anchor images. Third, we efficiently assign
tags to non-anchor images by leveraging the relationship between the non-anchor
images and the anchor units. Experimental results on a real-world social image
database well demonstrate the effectiveness of SUGAR-TC, outperforming several
related methods.