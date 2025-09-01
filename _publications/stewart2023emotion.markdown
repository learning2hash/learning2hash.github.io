---
layout: publication
title: Emotion-aligned Contrastive Learning Between Images And Music
authors: Shanti Stewart, Kleanthis Avramidis, Tiantian Feng, Shrikanth Narayanan
conference: ICASSP 2024 - 2024 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2024
bibkey: stewart2023emotion
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.12610'}]
tags: ["ICASSP", "Multimodal Retrieval", "Self-Supervised", "Supervised"]
short_authors: Stewart et al.
---
Traditional music search engines rely on retrieval methods that match natural
language queries with music metadata. There have been increasing efforts to
expand retrieval methods to consider the audio characteristics of music itself,
using queries of various modalities including text, video, and speech. While
most approaches aim to match general music semantics to the input queries, only
a few focus on affective qualities. In this work, we address the task of
retrieving emotionally-relevant music from image queries by learning an
affective alignment between images and music audio. Our approach focuses on
learning an emotion-aligned joint embedding space between images and music.
This embedding space is learned via emotion-supervised contrastive learning,
using an adapted cross-modal version of the SupCon loss. We evaluate the joint
embeddings through cross-modal retrieval tasks (image-to-music and
music-to-image) based on emotion labels. Furthermore, we investigate the
generalizability of the learned music embeddings via automatic music tagging.
Our experiments show that the proposed approach successfully aligns images and
music, and that the learned embedding space is effective for cross-modal
retrieval applications.