---
layout: publication
title: 'Afanet: Adaptive Frequency-aware Network For Weakly-supervised Few-shot Semantic
  Segmentation'
authors: Jiaqi Ma, Guo-sen Xie, Fang Zhao, Zechao Li
conference: IEEE Transactions on Multimedia
year: 2025
bibkey: ma2024afanet
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.17601'}]
tags: ["Few Shot & Zero Shot", "Supervised"]
short_authors: Ma et al.
---
Few-shot learning aims to recognize novel concepts by leveraging prior
knowledge learned from a few samples. However, for visually intensive tasks
such as few-shot semantic segmentation, pixel-level annotations are
time-consuming and costly. Therefore, in this paper, we utilize the more
challenging image-level annotations and propose an adaptive frequency-aware
network (AFANet) for weakly-supervised few-shot semantic segmentation (WFSS).
Specifically, we first propose a cross-granularity frequency-aware module (CFM)
that decouples RGB images into high-frequency and low-frequency distributions
and further optimizes semantic structural information by realigning them.
Unlike most existing WFSS methods using the textual information from the
multi-modal language-vision model, e.g., CLIP, in an offline learning manner,
we further propose a CLIP-guided spatial-adapter module (CSM), which performs
spatial domain adaptive transformation on textual information through online
learning, thus providing enriched cross-modal semantic information for CFM.
Extensive experiments on the Pascal-5\textsuperscript\{i\} and
COCO-20\textsuperscript\{i\} datasets demonstrate that AFANet has achieved
state-of-the-art performance. The code is available at
https://github.com/jarch-ma/AFANet.