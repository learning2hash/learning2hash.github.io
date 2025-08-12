---
layout: publication
title: Metric-based Few-shot Learning For Video Action Recognition
authors: Chris Careaga, Brian Hutchinson, Nathan Hodas, Lawrence Phillips
conference: Arxiv
year: 2019
bibkey: careaga2019metric
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.09602'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Careaga et al.
---
In the few-shot scenario, a learner must effectively generalize to unseen
classes given a small support set of labeled examples. While a relatively large
amount of research has gone into few-shot learning for image classification,
little work has been done on few-shot video classification. In this work, we
address the task of few-shot video action recognition with a set of two-stream
models. We evaluate the performance of a set of convolutional and recurrent
neural network video encoder architectures used in conjunction with three
popular metric-based few-shot algorithms. We train and evaluate using a
few-shot split of the Kinetics 600 dataset. Our experiments confirm the
importance of the two-stream setup, and find prototypical networks and pooled
long short-term memory network embeddings to give the best performance as
few-shot method and video encoder, respectively. For a 5-shot 5-way task, this
setup obtains 84.2% accuracy on the test set and 59.4% on a special "challenge"
test set, composed of highly confusable classes.