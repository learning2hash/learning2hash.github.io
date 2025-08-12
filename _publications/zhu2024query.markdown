---
layout: publication
title: Query-based Knowledge Sharing For Open-vocabulary Multi-label Classification
authors: Xuelin Zhu, Jian Liu, Dongqi Tang, Jiawei Ge, Weijia Liu, Bo Liu, Jiuxin
  Cao
conference: Arxiv
year: 2024
bibkey: zhu2024query
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.01181'}]
tags: []
short_authors: Zhu et al.
---
Identifying labels that did not appear during training, known as multi-label
zero-shot learning, is a non-trivial task in computer vision. To this end,
recent studies have attempted to explore the multi-modal knowledge of
vision-language pre-training (VLP) models by knowledge distillation, allowing
to recognize unseen labels in an open-vocabulary manner. However, experimental
evidence shows that knowledge distillation is suboptimal and provides limited
performance gain in unseen label prediction. In this paper, a novel query-based
knowledge sharing paradigm is proposed to explore the multi-modal knowledge
from the pretrained VLP model for open-vocabulary multi-label classification.
Specifically, a set of learnable label-agnostic query tokens is trained to
extract critical vision knowledge from the input image, and further shared
across all labels, allowing them to select tokens of interest as visual clues
for recognition. Besides, we propose an effective prompt pool for robust label
embedding, and reformulate the standard ranking learning into a form of
classification to allow the magnitude of feature vectors for matching, which
both significantly benefit label recognition. Experimental results show that
our framework significantly outperforms state-of-the-art methods on zero-shot
task by 5.9% and 4.5% in mAP on the NUS-WIDE and Open Images, respectively.