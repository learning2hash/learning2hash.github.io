---
layout: publication
title: 'Tagging Before Alignment: Integrating Multi-modal Tags For Video-text Retrieval'
authors: Yizhen Chen, Jie Wang, Lijian Lin, Zhongang Qi, Jin Ma, Ying Shan
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2023
bibkey: chen2023tagging
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.12644'}]
tags: ["AAAI", "Multimodal Retrieval", "Supervised", "Video Retrieval"]
short_authors: Chen et al.
---
Vision-language alignment learning for video-text retrieval arouses a lot of
attention in recent years. Most of the existing methods either transfer the
knowledge of image-text pretraining model to video-text retrieval task without
fully exploring the multi-modal information of videos, or simply fuse
multi-modal features in a brute force manner without explicit guidance. In this
paper, we integrate multi-modal information in an explicit manner by tagging,
and use the tags as the anchors for better video-text alignment. Various
pretrained experts are utilized for extracting the information of multiple
modalities, including object, person, motion, audio, etc. To take full
advantage of these information, we propose the TABLE (TAgging Before aLignmEnt)
network, which consists of a visual encoder, a tag encoder, a text encoder, and
a tag-guiding cross-modal encoder for jointly encoding multi-frame visual
features and multi-modal tags information. Furthermore, to strengthen the
interaction between video and text, we build a joint cross-modal encoder with
the triplet input of [vision, tag, text] and perform two additional supervised
tasks, Video Text Matching (VTM) and Masked Language Modeling (MLM). Extensive
experimental results demonstrate that the TABLE model is capable of achieving
State-Of-The-Art (SOTA) performance on various video-text retrieval benchmarks,
including MSR-VTT, MSVD, LSMDC and DiDeMo.