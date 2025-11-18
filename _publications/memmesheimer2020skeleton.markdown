---
layout: publication
title: 'Skeleton-dml: Deep Metric Learning For Skeleton-based One-shot Action Recognition'
authors: "Raphael Memmesheimer, Simon H\xE4ring, Nick Theisen, Dietrich Paulus"
conference: 2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2020
bibkey: memmesheimer2020skeleton
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.13823'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation"]
short_authors: Memmesheimer et al.
---
One-shot action recognition allows the recognition of human-performed actions
with only a single training example. This can influence human-robot-interaction
positively by enabling the robot to react to previously unseen behaviour. We
formulate the one-shot action recognition problem as a deep metric learning
problem and propose a novel image-based skeleton representation that performs
well in a metric learning setting. Therefore, we train a model that projects
the image representations into an embedding space. In embedding space the
similar actions have a low euclidean distance while dissimilar actions have a
higher distance. The one-shot action recognition problem becomes a
nearest-neighbor search in a set of activity reference samples. We evaluate the
performance of our proposed representation against a variety of other
skeleton-based image representations. In addition, we present an ablation study
that shows the influence of different embedding vector sizes, losses and
augmentation. Our approach lifts the state-of-the-art by 3.3% for the one-shot
action recognition protocol on the NTU RGB+D 120 dataset under a comparable
training setup. With additional augmentation our result improved over 7.7%.