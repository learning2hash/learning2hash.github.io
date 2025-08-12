---
layout: publication
title: Few-shot Class-incremental Semantic Segmentation Via Pseudo-labeling And Knowledge
  Distillation
authors: Chengjia Jiang, Tao Wang, Sien Li, Jinyang Wang, Shirui Wang, Antonios Antoniou
conference: 2023 4th International Conference on Information Science, Parallel and
  Distributed Systems (ISPDS)
year: 2023
bibkey: jiang2023few
citations: 3
additional_links: [{name: Code, url: 'https://github.com/ChasonJiang/FSCILSS'}, {
    name: Paper, url: 'https://arxiv.org/abs/2308.02790'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Jiang et al.
---
We address the problem of learning new classes for semantic segmentation
models from few examples, which is challenging because of the following two
reasons. Firstly, it is difficult to learn from limited novel data to capture
the underlying class distribution. Secondly, it is challenging to retain
knowledge for existing classes and to avoid catastrophic forgetting. For
learning from limited data, we propose a pseudo-labeling strategy to augment
the few-shot training annotations in order to learn novel classes more
effectively. Given only one or a few images labeled with the novel classes and
a much larger set of unlabeled images, we transfer the knowledge from labeled
images to unlabeled images with a coarse-to-fine pseudo-labeling approach in
two steps. Specifically, we first match each labeled image to its nearest
neighbors in the unlabeled image set at the scene level, in order to obtain
images with a similar scene layout. This is followed by obtaining pseudo-labels
within this neighborhood by applying classifiers learned on the few-shot
annotations. In addition, we use knowledge distillation on both labeled and
unlabeled data to retain knowledge on existing classes. We integrate the above
steps into a single convolutional neural network with a unified learning
objective. Extensive experiments on the Cityscapes and KITTI datasets validate
the efficacy of the proposed approach in the self-driving domain. Code is
available from https://github.com/ChasonJiang/FSCILSS.