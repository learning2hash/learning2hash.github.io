---
layout: publication
title: Enhancing Dynamic Image Advertising With Vision-language Pre-training
authors: Zhoufutu Wen, Xinyu Zhao, Zhipeng Jin, Yi Yang, Wei Jia, Xiaodong Chen, Shuanglong
  Li, Lin Liu
conference: Proceedings of the 46th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2023
bibkey: wen2023enhancing
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.14112'}]
tags: ["Evaluation", "Image Retrieval", "SIGIR", "Scalability", "Tools & Libraries"]
short_authors: Wen et al.
---
In the multimedia era, image is an effective medium in search advertising.
Dynamic Image Advertising (DIA), a system that matches queries with ad images
and generates multimodal ads, is introduced to improve user experience and ad
revenue. The core of DIA is a query-image matching module performing ad image
retrieval and relevance modeling. Current query-image matching suffers from
limited and inconsistent data, and insufficient cross-modal interaction. Also,
the separate optimization of retrieval and relevance models affects overall
performance. To address this issue, we propose a vision-language framework
consisting of two parts. First, we train a base model on large-scale image-text
pairs to learn general multimodal representation. Then, we fine-tune the base
model on advertising business data, unifying relevance modeling and retrieval
through multi-objective learning. Our framework has been implemented in Baidu
search advertising system "Phoneix Nest". Online evaluation shows that it
improves cost per mille (CPM) and click-through rate (CTR) by 1.04% and 1.865%.