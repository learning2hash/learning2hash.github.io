---
layout: publication
title: Self-supervised Video Hashing Via Bidirectional Transformers
authors: Shuyan Li, Li, Lu, Zhou
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2025
bibkey: li2025self
citations: 43
additional_links: [{name: Paper, url: 'https://openaccess.thecvf.com/content/CVPR2021/papers/Li_Self-Supervised_Video_Hashing_via_Bidirectional_Transformers_CVPR_2021_paper.pdf'}]
tags: ["Hashing Methods", "Self-Supervised", "Supervised", "Unsupervised", "Video Retrieval"]
short_authors: Li et al.
---
Most existing unsupervised video hashing methods are built on unidirectional models with less reliable training objectives, which underuse the correlations among frames and the similarity structure between videos. To enable efficient scalable video retrieval, we propose a self-supervised video Hashing method based on Bidirectional Transformers (BTH). Based on the encoder-decoder structure of transformers, we design a visual cloze task to fully exploit the bidirectional correlations between frames. To unveil the similarity structure between unlabeled video data, we further develop a similarity reconstruction task by establishing reliable and effective similarity connections in the video space. Furthermore, we develop a cluster assignment task to exploit the structural statistics of the whole dataset such that more discriminative binary codes can be learned. Extensive experiments implemented on three public benchmark datasets, FCVID, ActivityNet and YFCC, demonstrate the superiority of our proposed approach.