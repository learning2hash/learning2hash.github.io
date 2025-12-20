---
layout: publication
title: Self-supervised Video Representation Learning By Video Incoherence Detection
authors: Haozhi Cao, Yuecong Xu, Jianfei Yang, Kezhi Mao, Lihua Xie, Jianxiong Yin,
  Simon See
conference: Arxiv
year: 2021
bibkey: cao2021self
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.12493'}]
tags: ["Datasets", "Evaluation", "Self-Supervised", "Supervised", "Video Retrieval"]
short_authors: Cao et al.
---
This paper introduces a novel self-supervised method that leverages
incoherence detection for video representation learning. It roots from the
observation that visual systems of human beings can easily identify video
incoherence based on their comprehensive understanding of videos. Specifically,
the training sample, denoted as the incoherent clip, is constructed by multiple
sub-clips hierarchically sampled from the same raw video with various lengths
of incoherence between each other. The network is trained to learn high-level
representation by predicting the location and length of incoherence given the
incoherent clip as input. Additionally, intra-video contrastive learning is
introduced to maximize the mutual information between incoherent clips from the
same raw video. We evaluate our proposed method through extensive experiments
on action recognition and video retrieval utilizing various backbone networks.
Experiments show that our proposed method achieves state-of-the-art performance
across different backbone networks and different datasets compared with
previous coherence-based methods.