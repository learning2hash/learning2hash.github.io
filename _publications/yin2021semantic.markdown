---
layout: publication
title: Semantic-based Few-shot Learning By Interactive Psychometric Testing
authors: Lu Yin, Vlado Menkovski, Yulong Pei, Mykola Pechenizkiy
conference: Arxiv
year: 2021
bibkey: yin2021semantic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.09201'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Yin et al.
---
Few-shot classification tasks aim to classify images in query sets based on
only a few labeled examples in support sets. Most studies usually assume that
each image in a task has a single and unique class association. Under these
assumptions, these algorithms may not be able to identify the proper class
assignment when there is no exact matching between support and query classes.
For example, given a few images of lions, bikes, and apples to classify a
tiger. However, in a more general setting, we could consider the higher-level
concept, the large carnivores, to match the tiger to the lion for semantic
classification. Existing studies rarely considered this situation due to the
incompatibility of label-based supervision with complex conception
relationships. In this work, we advance the few-shot learning towards this more
challenging scenario, the semantic-based few-shot learning, and propose a
method to address the paradigm by capturing the inner semantic relationships
using interactive psychometric learning. The experiment results on the
CIFAR-100 dataset show the superiority of our method for the semantic-based
few-shot learning compared to the baseline.