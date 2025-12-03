---
layout: publication
title: 'Text Is MASS: Modeling As Stochastic Embedding For Text-video Retrieval'
authors: Jiamian Wang, Guohao Sun, Pichao Wang, Dongfang Liu, Sohail Dianat, Majid
  Rabbani, Raghuveer Rao, Zhiqiang Tao
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: wang2024text
citations: 36
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.17998'}]
tags: ["CVPR", "Datasets", "Evaluation", "Text Retrieval", "Video Retrieval"]
short_authors: Wang et al.
---
The increasing prevalence of video clips has sparked growing interest in
text-video retrieval. Recent advances focus on establishing a joint embedding
space for text and video, relying on consistent embedding representations to
compute similarity. However, the text content in existing datasets is generally
short and concise, making it hard to fully describe the redundant semantics of
a video. Correspondingly, a single text embedding may be less expressive to
capture the video embedding and empower the retrieval. In this study, we
propose a new stochastic text modeling method T-MASS, i.e., text is modeled as
a stochastic embedding, to enrich text embedding with a flexible and resilient
semantic range, yielding a text mass. To be specific, we introduce a
similarity-aware radius module to adapt the scale of the text mass upon the
given text-video pairs. Plus, we design and develop a support text
regularization to further control the text mass during the training. The
inference pipeline is also tailored to fully exploit the text mass for accurate
retrieval. Empirical evidence suggests that T-MASS not only effectively
attracts relevant text-video pairs while distancing irrelevant ones, but also
enables the determination of precise text embeddings for relevant pairs. Our
experimental results show a substantial improvement of T-MASS over baseline (3%
to 6.3% by R@1). Also, T-MASS achieves state-of-the-art performance on five
benchmark datasets, including MSRVTT, LSMDC, DiDeMo, VATEX, and Charades.