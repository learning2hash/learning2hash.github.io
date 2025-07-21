---
layout: publication
title: Do Better Imagenet Models Transfer Better... For Image Recommendation?
authors: del et al.
conference: Arxiv
year: 2018
bibkey: delrio2018do
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.09870'}]
tags: ["Recommender Systems"]
---
Visual embeddings from Convolutional Neural Networks (CNN) trained on the
ImageNet dataset for the ILSVRC challenge have shown consistently good
performance for transfer learning and are widely used in several tasks,
including image recommendation. However, some important questions have not yet
been answered in order to use these embeddings for a larger scope of
recommendation domains: a) Do CNNs that perform better in ImageNet are also
better for transfer learning in content-based image recommendation?, b) Does
fine-tuning help to improve performance? and c) Which is the best way to
perform the fine-tuning?
  In this paper we compare several CNN models pre-trained with ImageNet to
evaluate their transfer learning performance to an artwork image recommendation
task. Our results indicate that models with better performance in the ImageNet
challenge do not always imply better transfer learning for recommendation tasks
(e.g. NASNet vs. ResNet). Our results also show that fine-tuning can be helpful
even with a small dataset, but not every fine-tuning works. Our results can
inform other researchers and practitioners on how to train their CNNs for
better transfer learning towards image recommendation systems.