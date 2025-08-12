---
layout: publication
title: Revisiting Unsupervised Meta-learning Via The Characteristics Of Few-shot Tasks
authors: Han-jia Ye, Lu Han, De-chuan Zhan
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2022
bibkey: ye2020revisiting
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.14663'}]
tags: ["Few Shot & Zero Shot", "Unsupervised"]
short_authors: Han-jia Ye, Lu Han, De-chuan Zhan
---
Meta-learning has become a practical approach towards few-shot image
classification, where "a strategy to learn a classifier" is meta-learned on
labeled base classes and can be applied to tasks with novel classes. We remove
the requirement of base class labels and learn generalizable embeddings via
Unsupervised Meta-Learning (UML). Specifically, episodes of tasks are
constructed with data augmentations from unlabeled base classes during
meta-training, and we apply embedding-based classifiers to novel tasks with
labeled few-shot examples during meta-test. We observe two elements play
important roles in UML, i.e., the way to sample tasks and measure similarities
between instances. Thus we obtain a strong baseline with two simple
modifications -- a sufficient sampling strategy constructing multiple tasks per
episode efficiently together with a semi-normalized similarity. We then take
advantage of the characteristics of tasks from two directions to get further
improvements. First, synthesized confusing instances are incorporated to help
extract more discriminative embeddings. Second, we utilize an additional
task-specific embedding transformation as an auxiliary component during
meta-training to promote the generalization ability of the pre-adapted
embeddings. Experiments on few-shot learning benchmarks verify that our
approaches outperform previous UML methods and achieve comparable or even
better performance than its supervised variants.