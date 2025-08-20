---
layout: publication
title: Multimodal Clustering Networks For Self-supervised Learning From Unlabeled
  Videos
authors: Brian Chen, Andrew Rouditchenko, Kevin Duarte, Hilde Kuehne, Samuel Thomas,
  Angie Boggust, Rameswar Panda, Brian Kingsbury, Rogerio Feris, David Harwath, James
  Glass, Michael Picheny, Shih-Fu Chang
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: chen2021multimodal
citations: 52
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.12671'}]
tags: [Video Retrieval, Datasets, ICCV, Supervised, Few-shot & Zero-shot, Tools &
    Libraries, Self-Supervised]
short_authors: Chen et al.
---
Multimodal self-supervised learning is getting more and more attention as it
allows not only to train large networks without human supervision but also to
search and retrieve data across various modalities. In this context, this paper
proposes a self-supervised training framework that learns a common multimodal
embedding space that, in addition to sharing representations across different
modalities, enforces a grouping of semantically similar instances. To this end,
we extend the concept of instance-level contrastive learning with a multimodal
clustering step in the training pipeline to capture semantic similarities
across modalities. The resulting embedding space enables retrieval of samples
across all modalities, even from unseen datasets and different domains. To
evaluate our approach, we train our model on the HowTo100M dataset and evaluate
its zero-shot retrieval capabilities in two challenging domains, namely
text-to-video retrieval, and temporal action localization, showing
state-of-the-art results on four different datasets.