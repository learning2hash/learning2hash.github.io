---
layout: publication
title: Leveraging CLIP Encoder For Multimodal Emotion Recognition
authors: Yehun Song, Sunyoung Cho
conference: 2025 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2025
bibkey: song2025leveraging
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.00903'}]
tags: []
short_authors: Yehun Song, Sunyoung Cho
---
Multimodal emotion recognition (MER) aims to identify human emotions by combining data from various modalities such as language, audio, and vision. Despite the recent advances of MER approaches, the limitations in obtaining extensive datasets impede the improvement of performance. To mitigate this issue, we leverage a Contrastive Language-Image Pre-training (CLIP)-based architecture and its semantic knowledge from massive datasets that aims to enhance the discriminative multimodal representation. We propose a label encoder-guided MER framework based on CLIP (MER-CLIP) to learn emotion-related representations across modalities. Our approach introduces a label encoder that treats labels as text embeddings to incorporate their semantic information, leading to the learning of more representative emotional features. To further exploit label semantics, we devise a cross-modal decoder that aligns each modality to a shared embedding space by sequentially fusing modality features based on emotion-related input from the label encoder. Finally, the label encoder-guided prediction enables generalization across diverse labels by embedding their semantic information as well as word labels. Experimental results show that our method outperforms the state-of-the-art MER methods on the benchmark datasets, CMU-MOSI and CMU-MOSEI.