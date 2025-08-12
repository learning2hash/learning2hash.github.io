---
layout: publication
title: Unsupervised Few-shot Action Recognition Via Action-appearance Aligned Meta-adaptation
authors: Jay Patravali, Gaurav Mittal, Ye Yu, Fuxin Li, Mei Chen
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: patravali2021unsupervised
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.15317'}]
tags: ["Few Shot & Zero Shot", "ICCV", "Unsupervised"]
short_authors: Patravali et al.
---
We present MetaUVFS as the first Unsupervised Meta-learning algorithm for
Video Few-Shot action recognition. MetaUVFS leverages over 550K unlabeled
videos to train a two-stream 2D and 3D CNN architecture via contrastive
learning to capture the appearance-specific spatial and action-specific
spatio-temporal video features respectively. MetaUVFS comprises a novel
Action-Appearance Aligned Meta-adaptation (A3M) module that learns to focus on
the action-oriented video features in relation to the appearance features via
explicit few-shot episodic meta-learning over unsupervised hard-mined episodes.
Our action-appearance alignment and explicit few-shot learner conditions the
unsupervised training to mimic the downstream few-shot task, enabling MetaUVFS
to significantly outperform all unsupervised methods on few-shot benchmarks.
Moreover, unlike previous few-shot action recognition methods that are
supervised, MetaUVFS needs neither base-class labels nor a supervised
pretrained backbone. Thus, we need to train MetaUVFS just once to perform
competitively or sometimes even outperform state-of-the-art supervised methods
on popular HMDB51, UCF101, and Kinetics100 few-shot datasets.