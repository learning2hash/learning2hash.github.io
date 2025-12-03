---
layout: publication
title: 'Clip2video: Mastering Video-text Retrieval Via Image CLIP'
authors: Han Fang, Pengfei Xiong, Luhui Xu, Yu Chen
conference: Arxiv
year: 2021
bibkey: fang2021clip2video
citations: 130
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.11097'}]
tags: ["Datasets", "Evaluation", "Scalability", "Text Retrieval", "Tools & Libraries"]
short_authors: Fang et al.
---
We present CLIP2Video network to transfer the image-language pre-training
model to video-text retrieval in an end-to-end manner. Leading approaches in
the domain of video-and-language learning try to distill the spatio-temporal
video features and multi-modal interaction between videos and languages from a
large-scale video-text dataset. Different from them, we leverage pretrained
image-language model, simplify it as a two-stage framework with co-learning of
image-text and enhancing temporal relations between video frames and video-text
respectively, make it able to train on comparatively small datasets.
Specifically, based on the spatial semantics captured by Contrastive
Language-Image Pretraining (CLIP) model, our model involves a Temporal
Difference Block to capture motions at fine temporal video frames, and a
Temporal Alignment Block to re-align the tokens of video clips and phrases and
enhance the multi-modal correlation. We conduct thorough ablation studies, and
achieve state-of-the-art performance on major text-to-video and video-to-text
retrieval benchmarks, including new records of retrieval accuracy on MSR-VTT,
MSVD and VATEX.