---
layout: publication
title: 'AMNS: Attention-weighted Selective Mask And Noise Label Suppression For Text-to-image
  Person Retrieval'
authors: Runqing Zhang, Xue Zhou
conference: Arxiv
year: 2024
bibkey: zhang2024amns
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.06385'}]
tags: [Evaluation]
short_authors: Runqing Zhang, Xue Zhou
---
Most existing text-to-image person retrieval methods usually assume that the
training image-text pairs are perfectly aligned; however, the noisy
correspondence(NC) issue (i.e., incorrect or unreliable alignment) exists due
to poor image quality and labeling errors. Additionally, random masking
augmentation may inadvertently discard critical semantic content, introducing
noisy matches between images and text descriptions. To address the above two
challenges, we propose a noise label suppression method to mitigate NC and an
Attention-Weighted Selective Mask (AWM) strategy to resolve the issues caused
by random masking. Specifically, the Bidirectional Similarity Distribution
Matching (BSDM) loss enables the model to effectively learn from positive pairs
while preventing it from over-relying on them, thereby mitigating the risk of
overfitting to noisy labels. In conjunction with this, Weight Adjustment Focal
(WAF) loss improves the model's ability to handle hard samples. Furthermore,
AWM processes raw images through an EMA version of the image encoder,
selectively retaining tokens with strong semantic connections to the text,
enabling better feature extraction. Extensive experiments demonstrate the
effectiveness of our approach in addressing noise-related issues and improving
retrieval performance.