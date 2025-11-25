---
layout: publication
title: Contrastive Learning Of Medical Visual Representations From Paired Images And
  Text
authors: Yuhao Zhang, Hang Jiang, Yasuhide Miura, Christopher D. Manning, Curtis P.
  Langlotz
conference: Arxiv
year: 2020
bibkey: zhang2020contrastive
citations: 275
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.00747'}]
tags: ["Few Shot & Zero Shot", "Self-Supervised", "Unsupervised"]
short_authors: Zhang et al.
---
Learning visual representations of medical images (e.g., X-rays) is core to
medical image understanding but its progress has been held back by the scarcity
of human annotations. Existing work commonly relies on fine-tuning weights
transferred from ImageNet pretraining, which is suboptimal due to drastically
different image characteristics, or rule-based label extraction from the
textual report data paired with medical images, which is inaccurate and hard to
generalize. Meanwhile, several recent studies show exciting results from
unsupervised contrastive learning from natural images, but we find these
methods help little on medical images because of their high inter-class
similarity. We propose ConVIRT, an alternative unsupervised strategy to learn
medical visual representations by exploiting naturally occurring paired
descriptive text. Our new method of pretraining medical image encoders with the
paired text data via a bidirectional contrastive objective between the two
modalities is domain-agnostic, and requires no additional expert input. We test
ConVIRT by transferring our pretrained weights to 4 medical image
classification tasks and 2 zero-shot retrieval tasks, and show that it leads to
image representations that considerably outperform strong baselines in most
settings. Notably, in all 4 classification tasks, our method requires only 10%
as much labeled training data as an ImageNet initialized counterpart to achieve
better or comparable performance, demonstrating superior data efficiency.