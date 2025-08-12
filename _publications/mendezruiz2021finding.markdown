---
layout: publication
title: Finding Significant Features For Few-shot Learning Using Dimensionality Reduction
authors: Mauricio Mendez-Ruiz, Ivan Garcia Jorge Gonzalez-Zapata, Gilberto Ochoa-Ruiz,
  Andres Mendez-Vazquez
conference: Lecture Notes in Computer Science
year: 2021
bibkey: mendezruiz2021finding
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.06992'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Mendez-Ruiz et al.
---
Few-shot learning is a relatively new technique that specializes in problems
where we have little amounts of data. The goal of these methods is to classify
categories that have not been seen before with just a handful of samples.
Recent approaches, such as metric learning, adopt the meta-learning strategy in
which we have episodic tasks conformed by support (training) data and query
(test) data. Metric learning methods have demonstrated that simple models can
achieve good performance by learning a similarity function to compare the
support and the query data. However, the feature space learned by a given
metric learning approach may not exploit the information given by a specific
few-shot task. In this work, we explore the use of dimension reduction
techniques as a way to find task-significant features helping to make better
predictions. We measure the performance of the reduced features by assigning a
score based on the intra-class and inter-class distance, and selecting a
feature reduction method in which instances of different classes are far away
and instances of the same class are close. This module helps to improve the
accuracy performance by allowing the similarity function, given by the metric
learning method, to have more discriminative features for the classification.
Our method outperforms the metric learning baselines in the miniImageNet
dataset by around 2% in accuracy performance.