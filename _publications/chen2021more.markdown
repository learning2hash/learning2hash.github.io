---
layout: publication
title: 'More Than Just Attention: Improving Cross-modal Attentions With Contrastive
  Constraints For Image-text Matching'
authors: Yuxiao Chen, Jianbo Yuan, Long Zhao, Tianlang Chen, Rui Luo, Larry Davis,
  Dimitris N. Metaxas
conference: Arxiv
year: 2021
bibkey: chen2021more
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.09597'}]
tags: ["Datasets", "Evaluation", "Self-Supervised", "Supervised"]
short_authors: Chen et al.
---
Cross-modal attention mechanisms have been widely applied to the image-text
matching task and have achieved remarkable improvements thanks to its
capability of learning fine-grained relevance across different modalities.
However, the cross-modal attention models of existing methods could be
sub-optimal and inaccurate because there is no direct supervision provided
during the training process. In this work, we propose two novel training
strategies, namely Contrastive Content Re-sourcing (CCR) and Contrastive
Content Swapping (CCS) constraints, to address such limitations. These
constraints supervise the training of cross-modal attention models in a
contrastive learning manner without requiring explicit attention annotations.
They are plug-in training strategies and can be easily integrated into existing
cross-modal attention models. Additionally, we introduce three metrics
including Attention Precision, Recall, and F1-Score to quantitatively measure
the quality of learned attention models. We evaluate the proposed constraints
by incorporating them into four state-of-the-art cross-modal attention-based
image-text matching models. Experimental results on both Flickr30k and MS-COCO
datasets demonstrate that integrating these constraints improves the model
performance in terms of both retrieval performance and attention metrics.