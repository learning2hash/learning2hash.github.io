---
layout: publication
title: Improving Sound Source Localization With Joint Slot Attention On Image And
  Audio
authors: Inho Kim, Youngkil Song, Jicheol Park, Won Hwa Kim, Suha Kwak
conference: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2025
bibkey: kim2025improving
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.15118'}]
tags: ["CVPR", "Multimodal Retrieval", "Self-Supervised"]
short_authors: Kim et al.
---
Sound source localization (SSL) is the task of locating the source of sound within an image. Due to the lack of localization labels, the de facto standard in SSL has been to represent an image and audio as a single embedding vector each, and use them to learn SSL via contrastive learning. To this end, previous work samples one of local image features as the image embedding and aggregates all local audio features to obtain the audio embedding, which is far from optimal due to the presence of noise and background irrelevant to the actual target in the input. We present a novel SSL method that addresses this chronic issue by joint slot attention on image and audio. To be specific, two slots competitively attend image and audio features to decompose them into target and off-target representations, and only target representations of image and audio are used for contrastive learning. Also, we introduce cross-modal attention matching to further align local features of image and audio. Our method achieved the best in almost all settings on three public benchmarks for SSL, and substantially outperformed all the prior work in cross-modal retrieval.