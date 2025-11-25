---
layout: publication
title: A Clip-hitchhiker's Guide To Long Video Retrieval
authors: "Max Bain, Arsha Nagrani, G\xFCl Varol, Andrew Zisserman"
conference: Arxiv
year: 2022
bibkey: bain2022a
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.08508'}]
tags: ["Evaluation", "Video Retrieval"]
short_authors: Bain et al.
---
Our goal in this paper is the adaptation of image-text models for long video
retrieval. Recent works have demonstrated state-of-the-art performance in video
retrieval by adopting CLIP, effectively hitchhiking on the image-text
representation for video tasks. However, there has been limited success in
learning temporal aggregation that outperform mean-pooling the image-level
representations extracted per frame by CLIP. We find that the simple yet
effective baseline of weighted-mean of frame embeddings via query-scoring is a
significant improvement above all prior temporal modelling attempts and
mean-pooling. In doing so, we provide an improved baseline for others to
compare to and demonstrate state-of-the-art performance of this simple baseline
on a suite of long video retrieval benchmarks.