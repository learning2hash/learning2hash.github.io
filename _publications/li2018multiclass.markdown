---
layout: publication
title: A Multiclass Multiple Instance Learning Method With Exact Likelihood
authors: Xi-Lin Li
conference: Arxiv
year: 2018
bibkey: li2018multiclass
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.12346'}]
tags: []
short_authors: Xi-Lin Li
---
We study a multiclass multiple instance learning (MIL) problem where the
labels only suggest whether any instance of a class exists or does not exist in
a training sample or example. No further information, e.g., the number of
instances of each class, relative locations or orders of all instances in a
training sample, is exploited. Such a weak supervision learning problem can be
exactly solved by maximizing the model likelihood fitting given observations,
and finds applications to tasks like multiple object detection and localization
for image understanding. We discuss its relationship to the classic
classification problem, the traditional MIL, and connectionist temporal
classification (CTC). We use image recognition as the example task to develop
our method, although it is applicable to data with higher or lower dimensions
without much modification. Experimental results show that our method can be
used to learn all convolutional neural networks for solving real-world multiple
object detection and localization tasks with weak annotations, e.g.,
transcribing house number sequences from the Google street view imagery
dataset.