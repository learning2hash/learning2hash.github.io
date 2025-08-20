---
layout: publication
title: 'Revisiting Few-shot Relation Classification: Evaluation Data And Classification
  Schemes'
authors: Ofer Sabo, Yanai Elazar, Yoav Goldberg, Ido Dagan
conference: Transactions of the Association for Computational Linguistics
year: 2021
bibkey: sabo2021revisiting
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.08481'}]
tags: [TACL, Datasets, ACL, Supervised, Few-shot & Zero-shot, Evaluation]
short_authors: Sabo et al.
---
We explore Few-Shot Learning (FSL) for Relation Classification (RC). Focusing
on the realistic scenario of FSL, in which a test instance might not belong to
any of the target categories (none-of-the-above, aka NOTA), we first revisit
the recent popular dataset structure for FSL, pointing out its unrealistic data
distribution. To remedy this, we propose a novel methodology for deriving more
realistic few-shot test data from available datasets for supervised RC, and
apply it to the TACRED dataset. This yields a new challenging benchmark for FSL
RC, on which state of the art models show poor performance. Next, we analyze
classification schemes within the popular embedding-based nearest-neighbor
approach for FSL, with respect to constraints they impose on the embedding
space. Triggered by this analysis we propose a novel classification scheme, in
which the NOTA category is represented as learned vectors, shown empirically to
be an appealing option for FSL.