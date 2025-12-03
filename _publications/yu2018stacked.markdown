---
layout: publication
title: Stacked Semantic-guided Attention Model For Fine-grained Zero-shot Learning
authors: Yunlong Yu, Zhong Ji, Yanwei Fu, Jichang Guo, Yanwei Pang, Zhongfei Zhang
conference: Arxiv
year: 2018
bibkey: yu2018stacked
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.08113'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Tools & Libraries"]
short_authors: Yu et al.
---
Zero-Shot Learning (ZSL) is achieved via aligning the semantic relationships
between the global image feature vector and the corresponding class semantic
descriptions. However, using the global features to represent fine-grained
images may lead to sub-optimal results since they neglect the discriminative
differences of local regions. Besides, different regions contain distinct
discriminative information. The important regions should contribute more to the
prediction. To this end, we propose a novel stacked semantics-guided attention
(S2GA) model to obtain semantic relevant features by using individual class
semantic features to progressively guide the visual features to generate an
attention map for weighting the importance of different local regions. Feeding
both the integrated visual features and the class semantic features into a
multi-class classification architecture, the proposed framework can be trained
end-to-end. Extensive experimental results on CUB and NABird datasets show that
the proposed approach has a consistent improvement on both fine-grained
zero-shot classification and retrieval tasks.