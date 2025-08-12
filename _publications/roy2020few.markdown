---
layout: publication
title: Few-shot Learning With Intra-class Knowledge Transfer
authors: Vivek Roy, Yan Xu, Yu-Xiong Wang, Kris Kitani, Ruslan Salakhutdinov, Martial
  Hebert
conference: Arxiv
year: 2020
bibkey: roy2020few
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.09892'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Roy et al.
---
We consider the few-shot classification task with an unbalanced dataset, in
which some classes have sufficient training samples while other classes only
have limited training samples. Recent works have proposed to solve this task by
augmenting the training data of the few-shot classes using generative models
with the few-shot training samples as the seeds. However, due to the limited
number of the few-shot seeds, the generated samples usually have small
diversity, making it difficult to train a discriminative classifier for the
few-shot classes. To enrich the diversity of the generated samples, we propose
to leverage the intra-class knowledge from the neighbor many-shot classes with
the intuition that neighbor classes share similar statistical information. Such
intra-class information is obtained with a two-step mechanism. First, a
regressor trained only on the many-shot classes is used to evaluate the
few-shot class means from only a few samples. Second, superclasses are
clustered, and the statistical mean and feature variance of each superclass are
used as transferable knowledge inherited by the children few-shot classes. Such
knowledge is then used by a generator to augment the sparse training data to
help the downstream classification tasks. Extensive experiments show that our
method achieves state-of-the-art across different datasets and \(n\)-shot
settings.