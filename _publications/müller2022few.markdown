---
layout: publication
title: Few-shot Learning With Siamese Networks And Label Tuning
authors: "Thomas M\xFCller, Guillermo P\xE9rez-Torr\xF3, Marc Franco-Salvador"
conference: 'Proceedings of the 60th Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2022
bibkey: "m\xFCller2022few"
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.14655'}]
tags: ["Few Shot & Zero Shot"]
short_authors: "Thomas M\xFCller, Guillermo P\xE9rez-Torr\xF3, Marc Franco-Salvador"
---
We study the problem of building text classifiers with little or no training
data, commonly known as zero and few-shot text classification. In recent years,
an approach based on neural textual entailment models has been found to give
strong results on a diverse range of tasks. In this work, we show that with
proper pre-training, Siamese Networks that embed texts and labels offer a
competitive alternative. These models allow for a large reduction in inference
cost: constant in the number of labels rather than linear. Furthermore, we
introduce label tuning, a simple and computationally efficient approach that
allows to adapt the models in a few-shot setup by only changing the label
embeddings. While giving lower performance than model fine-tuning, this
approach has the architectural advantage that a single encoder can be shared by
many different tasks.