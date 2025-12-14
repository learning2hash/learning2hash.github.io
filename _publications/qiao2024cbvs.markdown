---
layout: publication
title: 'CBVS: A Large-scale Chinese Image-text Benchmark For Real-world Short Video
  Search Scenarios'
authors: Xiangshuo Qiao, Xianxin Li, Xiaozhe Qu, Jie Zhang, Yang Liu, Yu Luo, Cihang
  Jin, Jin Ma
conference: Arxiv
year: 2024
bibkey: qiao2024cbvs
citations: 0
additional_links: [{name: Code, url: 'https://github.com/QQBrowserVideoSearch/CBVS-UniCLIP'},
  {name: Paper, url: 'https://arxiv.org/abs/2401.10475'}]
tags: [Video Retrieval, Evaluation, Image Retrieval, Datasets, Scalability]
short_authors: Qiao et al.
---
Vision-Language Models pre-trained on large-scale image-text datasets have
shown superior performance in downstream tasks such as image retrieval. Most of
the images for pre-training are presented in the form of open domain
common-sense visual elements. Differently, video covers in short video search
scenarios are presented as user-originated contents that provide important
visual summaries of videos. In addition, a portion of the video covers come
with manually designed cover texts that provide semantic complements. In order
to fill in the gaps in short video cover data, we establish the first
large-scale cover-text benchmark for Chinese short video search scenarios.
Specifically, we release two large-scale datasets CBVS-5M/10M to provide short
video covers, and the manual fine-labeling dataset CBVS-20K to provide real
user queries, which serves as an image-text benchmark test in the Chinese short
video search field. To integrate the semantics of cover text in the case of
modality missing, we propose UniCLIP where cover texts play a guiding role
during training, however are not relied upon by inference. Extensive evaluation
on CBVS-20K demonstrates the excellent performance of our proposal. UniCLIP has
been deployed to Tencent's online video search systems with hundreds of
millions of visits and achieved significant gains. The dataset and code are
available at https://github.com/QQBrowserVideoSearch/CBVS-UniCLIP.