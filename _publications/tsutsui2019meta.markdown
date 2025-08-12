---
layout: publication
title: Meta-reinforced Synthetic Data For One-shot Fine-grained Visual Recognition
authors: Satoshi Tsutsui, Yanwei Fu, David Crandall
conference: Arxiv
year: 2019
bibkey: tsutsui2019meta
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.07164'}]
tags: []
short_authors: Satoshi Tsutsui, Yanwei Fu, David Crandall
---
One-shot fine-grained visual recognition often suffers from the problem of
training data scarcity for new fine-grained classes. To alleviate this problem,
an off-the-shelf image generator can be applied to synthesize additional
training images, but these synthesized images are often not helpful for
actually improving the accuracy of one-shot fine-grained recognition. This
paper proposes a meta-learning framework to combine generated images with
original images, so that the resulting ``hybrid'' training images can improve
one-shot learning. Specifically, the generic image generator is updated by a
few training instances of novel classes, and a Meta Image Reinforcing Network
(MetaIRNet) is proposed to conduct one-shot fine-grained recognition as well as
image reinforcement. The model is trained in an end-to-end manner, and our
experiments demonstrate consistent improvement over baselines on one-shot
fine-grained image classification benchmarks.