---
layout: publication
title: 'Large-scale Historical Watermark Recognition: Dataset And A New Consistency-based
  Approach'
authors: Xi Shen, Ilaria Pastrolin, Oumayma Bounou, Spyros Gidaris, Marc Smith, Olivier
  Poncet, Mathieu Aubry
conference: 2020 25th International Conference on Pattern Recognition (ICPR)
year: 2021
bibkey: shen2019large
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.10254'}]
tags: ["Datasets", "Evaluation", "Scalability"]
short_authors: Shen et al.
---
Historical watermark recognition is a highly practical, yet unsolved
challenge for archivists and historians. With a large number of well-defined
classes, cluttered and noisy samples, different types of representations, both
subtle differences between classes and high intra-class variation, historical
watermarks are also challenging for pattern recognition. In this paper,
overcoming the difficulty of data collection, we present a large public dataset
with more than 6k new photographs, allowing for the first time to tackle at
scale the scenarios of practical interest for scholars: one-shot instance
recognition and cross-domain one-shot instance recognition amongst more than
16k fine-grained classes. We demonstrate that this new dataset is large enough
to train modern deep learning approaches, and show that standard methods can be
improved considerably by using mid-level deep features. More precisely, we
design both a matching score and a feature fine-tuning strategy based on
filtering local matches using spatial consistency. This consistency-based
approach provides important performance boost compared to strong baselines. Our
model achieves 55% top-1 accuracy on our very challenging 16,753-class one-shot
cross-domain recognition task, each class described by a single drawing from
the classic Briquet catalog. In addition to watermark classification, we show
our approach provides promising results on fine-grained sketch-based image
retrieval.