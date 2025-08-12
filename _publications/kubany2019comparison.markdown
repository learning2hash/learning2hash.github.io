---
layout: publication
title: Comparison Of State-of-the-art Deep Learning Apis For Image Multi-label Classification
  Using Semantic Metrics
authors: Adam Kubany, Shimon Ben Ishay, Ruben-sacha Ohayon, Armin Shmilovici, Lior
  Rokach, Tomer Doitshman
conference: Expert Systems with Applications
year: 2020
bibkey: kubany2019comparison
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.09190'}]
tags: ["Datasets", "Evaluation"]
short_authors: Kubany et al.
---
Image understanding heavily relies on accurate multi-label classification. In
recent years, deep learning algorithms have become very successful for such
tasks, and various commercial and open-source APIs have been released for
public use. However, these APIs are often trained on different datasets, which,
besides affecting their performance, might pose a challenge to their
performance evaluation. This challenge concerns the different object-class
dictionaries of the APIs' training dataset and the benchmark dataset, in which
the predicted labels are semantically similar to the benchmark labels but
considered different simply because they have different wording in the
dictionaries. To face this challenge, we propose semantic similarity metrics to
obtain richer understating of the APIs predicted labels and thus their
performance. In this study, we evaluate and compare the performance of 13 of
the most prominent commercial and open-source APIs in a best-of-breed challenge
on the Visual Genome and Open Images benchmark datasets. Our findings
demonstrate that, while using traditional metrics, the Microsoft Computer
Vision, Imagga, and IBM APIs performed better than others. However, applying
semantic metrics also unveil the InceptionResNet-v2, Inception-v3, and ResNet50
APIs, which are trained only with the simple ImageNet dataset, as challengers
for top semantic performers.