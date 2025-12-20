---
layout: publication
title: 'Bridging The Gap: Multi-level Cross-modality Joint Alignment For Visible-infrared
  Person Re-identification'
authors: Tengfei Liang, Yi Jin, Wu Liu, Tao Wang, Songhe Feng, Yidong Li
conference: 2024 IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)
year: 2023
bibkey: liang2023bridging
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.08316'}]
tags: ["Distance Metric Learning", "Evaluation", "Image Retrieval"]
short_authors: Liang et al.
---
Visible-Infrared person Re-IDentification (VI-ReID) is a challenging
cross-modality image retrieval task that aims to match pedestrians' images
across visible and infrared cameras. To solve the modality gap, existing
mainstream methods adopt a learning paradigm converting the image retrieval
task into an image classification task with cross-entropy loss and auxiliary
metric learning losses. These losses follow the strategy of adjusting the
distribution of extracted embeddings to reduce the intra-class distance and
increase the inter-class distance. However, such objectives do not precisely
correspond to the final test setting of the retrieval task, resulting in a new
gap at the optimization level. By rethinking these keys of VI-ReID, we propose
a simple and effective method, the Multi-level Cross-modality Joint Alignment
(MCJA), bridging both modality and objective-level gap. For the former, we
design the Modality Alignment Augmentation, which consists of three novel
strategies, the weighted grayscale, cross-channel cutmix, and spectrum jitter
augmentation, effectively reducing modality discrepancy in the image space. For
the latter, we introduce a new Cross-Modality Retrieval loss. It is the first
work to constrain from the perspective of the ranking list, aligning with the
goal of the testing stage. Moreover, based on the global feature only, our
method exhibits good performance and can serve as a strong baseline method for
the VI-ReID community.