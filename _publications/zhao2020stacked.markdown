---
layout: publication
title: Stacked Convolutional Deep Encoding Network For Video-text Retrieval
authors: Zhao Rui, Zheng Kecheng, Zha Zheng-jun
conference: 2020 IEEE International Conference on Multimedia and Expo (ICME)
year: 2020
bibkey: zhao2020stacked
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.04959'}]
tags: ["Evaluation", "Text-Retrieval", "Datasets"]
short_authors: Zhao Rui, Zheng Kecheng, Zha Zheng-jun
---
Existing dominant approaches for cross-modal video-text retrieval task are to
learn a joint embedding space to measure the cross-modal similarity. However,
these methods rarely explore long-range dependency inside video frames or
textual words leading to insufficient textual and visual details. In this
paper, we propose a stacked convolutional deep encoding network for video-text
retrieval task, which considers to simultaneously encode long-range and
short-range dependency in the videos and texts. Specifically, a multi-scale
dilated convolutional (MSDC) block within our approach is able to encode
short-range temporal cues between video frames or text words by adopting
different scales of kernel size and dilation size of convolutional layer. A
stacked structure is designed to expand the receptive fields by repeatedly
adopting the MSDC block, which further captures the long-range relations
between these cues. Moreover, to obtain more robust textual representations, we
fully utilize the powerful language model named Transformer in two stages:
pretraining phrase and fine-tuning phrase. Extensive experiments on two
different benchmark datasets (MSR-VTT, MSVD) show that our proposed method
outperforms other state-of-the-art approaches.