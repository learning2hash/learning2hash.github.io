---
layout: publication
title: An Empirical Study Of Pretrained Representations For Few-shot Classification
authors: Tiago Ramalho, Thierry Sousbie, Stefano Peluchetti
conference: Arxiv
year: 2019
bibkey: ramalho2019empirical
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.01319'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Tiago Ramalho, Thierry Sousbie, Stefano Peluchetti
---
Recent algorithms with state-of-the-art few-shot classification results start
their procedure by computing data features output by a large pretrained model.
In this paper we systematically investigate which models provide the best
representations for a few-shot image classification task when pretrained on the
Imagenet dataset. We test their representations when used as the starting point
for different few-shot classification algorithms. We observe that models
trained on a supervised classification task have higher performance than models
trained in an unsupervised manner even when transferred to out-of-distribution
datasets. Models trained with adversarial robustness transfer better, while
having slightly lower accuracy than supervised models.