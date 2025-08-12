---
layout: publication
title: Revisiting Local Descriptor For Improved Few-shot Classification
authors: Jun He, Richang Hong, Xueliang Liu, Mingliang Xu, Qianru Sun
conference: ACM Transactions on Multimedia Computing, Communications, and Applications
year: 2022
bibkey: he2021revisiting
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.16009'}]
tags: ["Few Shot & Zero Shot"]
short_authors: He et al.
---
Few-shot classification studies the problem of quickly adapting a deep
learner to understanding novel classes based on few support images. In this
context, recent research efforts have been aimed at designing more and more
complex classifiers that measure similarities between query and support images,
but left the importance of feature embeddings seldom explored. We show that the
reliance on sophisticated classifiers is not necessary, and a simple classifier
applied directly to improved feature embeddings can instead outperform most of
the leading methods in the literature. To this end, we present a new method
named \textbf\{DCAP\} for few-shot classification, in which we investigate how
one can improve the quality of embeddings by leveraging \textbf\{D\}ense
\textbf\{C\}lassification and \textbf\{A\}ttentive \textbf\{P\}ooling. Specifically,
we propose to train a learner on base classes with abundant samples to solve
dense classification problem first and then meta-train the learner on a bunch
of randomly sampled few-shot tasks to adapt it to few-shot scenario or the test
time scenario. During meta-training, we suggest to pool feature maps by
applying attentive pooling instead of the widely used global average pooling
(GAP) to prepare embeddings for few-shot classification. Attentive pooling
learns to reweight local descriptors, explaining what the learner is looking
for as evidence for decision making. Experiments on two benchmark datasets show
the proposed method to be superior in multiple few-shot settings while being
simpler and more explainable. Code is available at:
https://github.com/Ukeyboard/dcap/.