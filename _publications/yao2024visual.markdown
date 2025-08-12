---
layout: publication
title: Visual Grounding With Multi-modal Conditional Adaptation
authors: Ruilin Yao, Shengwu Xiong, Yichen Zhao, Yi Rong
conference: Proceedings of the 32nd ACM International Conference on Multimedia
year: 2024
bibkey: yao2024visual
citations: 2
additional_links: [{name: Code, url: 'https://github.com/Mr-Bigworth/MMCA'}, {name: Paper,
    url: 'https://arxiv.org/abs/2409.04999'}]
tags: []
short_authors: Yao et al.
---
Visual grounding is the task of locating objects specified by natural
language expressions. Existing methods extend generic object detection
frameworks to tackle this task. They typically extract visual and textual
features separately using independent visual and textual encoders, then fuse
these features in a multi-modal decoder for final prediction. However, visual
grounding presents unique challenges. It often involves locating objects with
different text descriptions within the same image. Existing methods struggle
with this task because the independent visual encoder produces identical visual
features for the same image, limiting detection performance. Some recently
approaches propose various language-guided visual encoders to address this
issue, but they mostly rely solely on textual information and require
sophisticated designs. In this paper, we introduce Multi-modal Conditional
Adaptation (MMCA), which enables the visual encoder to adaptively update
weights, directing its focus towards text-relevant regions. Specifically, we
first integrate information from different modalities to obtain multi-modal
embeddings. Then we utilize a set of weighting coefficients, which generated
from the multimodal embeddings, to reorganize the weight update matrices and
apply them to the visual encoder of the visual grounding model. Extensive
experiments on four widely used datasets demonstrate that MMCA achieves
significant improvements and state-of-the-art results. Ablation experiments
further demonstrate the lightweight and efficiency of our method. Our source
code is available at: https://github.com/Mr-Bigworth/MMCA.