---
layout: publication
title: Bridging Video-text Retrieval With Multiple Choice Questions
authors: Yuying Ge, Yixiao Ge, Xihui Liu, Dian Li, Ying Shan, Xiaohu Qie, Ping Luo
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: ge2022bridging
citations: 117
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.04850'}]
tags: [Video Retrieval, Evaluation, Few-shot & Zero-shot, Efficiency, Similarity Search,
  Datasets, CVPR, Text Retrieval]
short_authors: Ge et al.
---
Pre-training a model to learn transferable video-text representation for
retrieval has attracted a lot of attention in recent years. Previous dominant
works mainly adopt two separate encoders for efficient retrieval, but ignore
local associations between videos and texts. Another line of research uses a
joint encoder to interact video with texts, but results in low efficiency since
each text-video pair needs to be fed into the model. In this work, we enable
fine-grained video-text interactions while maintaining high efficiency for
retrieval via a novel pretext task, dubbed as Multiple Choice Questions (MCQ),
where a parametric module BridgeFormer is trained to answer the "questions"
constructed by the text features via resorting to the video features.
Specifically, we exploit the rich semantics of text (i.e., nouns and verbs) to
build questions, with which the video encoder can be trained to capture more
regional content and temporal dynamics. In the form of questions and answers,
the semantic associations between local video-text features can be properly
established. BridgeFormer is able to be removed for downstream retrieval,
rendering an efficient and flexible model with only two encoders. Our method
outperforms state-of-the-art methods on the popular text-to-video retrieval
task in five datasets with different experimental setups (i.e., zero-shot and
fine-tune), including HowTo100M (one million videos). We further conduct
zero-shot action recognition, which can be cast as video-to-text retrieval, and
our approach also significantly surpasses its counterparts. As an additional
benefit, our method achieves competitive results with much shorter pre-training
videos on single-modality downstream tasks, e.g., action recognition with
linear evaluation.