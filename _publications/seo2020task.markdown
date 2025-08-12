---
layout: publication
title: Task-adaptive Clustering For Semi-supervised Few-shot Classification
authors: Jun Seo, Sung Whan Yoon, Jaekyun Moon
conference: Arxiv
year: 2020
bibkey: seo2020task
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.08221'}]
tags: ["Few Shot & Zero Shot", "Supervised"]
short_authors: Jun Seo, Sung Whan Yoon, Jaekyun Moon
---
Few-shot learning aims to handle previously unseen tasks using only a small
amount of new training data. In preparing (or meta-training) a few-shot
learner, however, massive labeled data are necessary. In the real world,
unfortunately, labeled data are expensive and/or scarce. In this work, we
propose a few-shot learner that can work well under the semi-supervised setting
where a large portion of training data is unlabeled. Our method employs
explicit task-conditioning in which unlabeled sample clustering for the current
task takes place in a new projection space different from the embedding feature
space. The conditioned clustering space is linearly constructed so as to
quickly close the gap between the class centroids for the current task and the
independent per-class reference vectors meta-trained across tasks. In a more
general setting, our method introduces a concept of controlling the degree of
task-conditioning for meta-learning: the amount of task-conditioning varies
with the number of repetitive updates for the clustering space. Extensive
simulation results based on the miniImageNet and tieredImageNet datasets show
state-of-the-art semi-supervised few-shot classification performance of the
proposed method. Simulation results also indicate that the proposed
task-adaptive clustering shows graceful degradation with a growing number of
distractor samples, i.e., unlabeled sample images coming from outside the
candidate classes.