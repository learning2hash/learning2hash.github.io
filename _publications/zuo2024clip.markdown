---
layout: publication
title: 'CLIP-FSAC++: Few-shot Anomaly Classification With Anomaly Descriptor Based
  On CLIP'
authors: Zuo Zuo, Jiahao Dong, Yao Wu, Yanyun Qu, Zongze Wu
conference: Arxiv
year: 2024
bibkey: zuo2024clip
citations: 0
additional_links: [{name: Code, url: 'https://github.com/Jay-zzcoder/clip-fsac-pp'},
  {name: Paper, url: 'https://arxiv.org/abs/2412.03829'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Zuo et al.
---
Industrial anomaly classification (AC) is an indispensable task in industrial
manufacturing, which guarantees quality and safety of various product. To
address the scarcity of data in industrial scenarios, lots of few-shot anomaly
detection methods emerge recently. In this paper, we propose an effective
few-shot anomaly classification (FSAC) framework with one-stage training,
dubbed CLIP-FSAC++. Specifically, we introduce a cross-modality interaction
module named Anomaly Descriptor following image and text encoders, which
enhances the correlation of visual and text embeddings and adapts the
representations of CLIP from pre-trained data to target data. In anomaly
descriptor, image-to-text cross-attention module is used to obtain
image-specific text embeddings and text-to-image cross-attention module is used
to obtain text-specific visual embeddings. Then these modality-specific
embeddings are used to enhance original representations of CLIP for better
matching ability. Comprehensive experiment results are provided for evaluating
our method in few-normal shot anomaly classification on VisA and MVTEC-AD for
1, 2, 4 and 8-shot settings. The source codes are at
https://github.com/Jay-zzcoder/clip-fsac-pp