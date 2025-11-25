---
layout: publication
title: 'Lite-mind: Towards Efficient And Robust Brain Representation Network'
authors: Zixuan Gong, Qi Zhang, Guangyin Bao, Lei Zhu, Ke Liu, Liang Hu, Duoqian Miao,
  Yu Zhang
conference: Arxiv
year: 2023
bibkey: gong2023lite
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.03781'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Gong et al.
---
The limited data availability and the low signal-to-noise ratio of fMRI
signals lead to the challenging task of fMRI-to-image retrieval.
State-of-the-art MindEye remarkably improves fMRI-to-image retrieval
performance by leveraging a large model, i.e., a 996M MLP Backbone per subject,
to align fMRI embeddings to the final hidden layer of CLIP's Vision Transformer
(ViT). However, significant individual variations exist among subjects, even
under identical experimental setups, mandating the training of large
subject-specific models. The substantial parameters pose significant challenges
in deploying fMRI decoding on practical devices. To this end, we propose
Lite-Mind, a lightweight, efficient, and robust brain representation learning
paradigm based on Discrete Fourier Transform (DFT), which efficiently aligns
fMRI voxels to fine-grained information of CLIP. We elaborately design a DFT
backbone with Spectrum Compression and Frequency Projector modules to learn
informative and robust voxel embeddings. Our experiments demonstrate that
Lite-Mind achieves an impressive 94.6% fMRI-to-image retrieval accuracy on the
NSD dataset for Subject 1, with 98.7% fewer parameters than MindEye. Lite-Mind
is also proven to be able to be migrated to smaller fMRI datasets and
establishes a new state-of-the-art for zero-shot classification on the GOD
dataset.