---
layout: publication
title: Towards Cross-modal Text-molecule Retrieval With Better Modality Alignment
authors: Jia Song, Wanru Zhuang, Yujie Lin, Liang Zhang, Chunyan Li, Jinsong Su, Song
  He, Xiaochen Bo
conference: 2024 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)
year: 2024
bibkey: song2024towards
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.23715'}]
tags: [Self-Supervised, Evaluation, Robustness]
short_authors: Song et al.
---
Cross-modal text-molecule retrieval model aims to learn a shared feature
space of the text and molecule modalities for accurate similarity calculation,
which facilitates the rapid screening of molecules with specific properties and
activities in drug design. However, previous works have two main defects.
First, they are inadequate in capturing modality-shared features considering
the significant gap between text sequences and molecule graphs. Second, they
mainly rely on contrastive learning and adversarial training for cross-modality
alignment, both of which mainly focus on the first-order similarity, ignoring
the second-order similarity that can capture more structural information in the
embedding space. To address these issues, we propose a novel cross-modal
text-molecule retrieval model with two-fold improvements. Specifically, on the
top of two modality-specific encoders, we stack a memory bank based feature
projector that contain learnable memory vectors to extract modality-shared
features better. More importantly, during the model training, we calculate four
kinds of similarity distributions (text-to-text, text-to-molecule,
molecule-to-molecule, and molecule-to-text similarity distributions) for each
instance, and then minimize the distance between these similarity distributions
(namely second-order similarity losses) to enhance cross-modal alignment.
Experimental results and analysis strongly demonstrate the effectiveness of our
model. Particularly, our model achieves SOTA performance, outperforming the
previously-reported best result by 6.4%.