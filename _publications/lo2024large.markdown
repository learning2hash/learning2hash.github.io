---
layout: publication
title: Large Language Model Informed Patent Image Retrieval
authors: Hao-Cheng Lo, Jung-Mei Chu, Jieh Hsiang, Chun-Chieh Cho
conference: Arxiv
year: 2024
bibkey: lo2024large
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.19360'}]
tags: ["Image Retrieval"]
short_authors: Lo et al.
---
In patent prosecution, image-based retrieval systems for identifying
similarities between current patent images and prior art are pivotal to ensure
the novelty and non-obviousness of patent applications. Despite their growing
popularity in recent years, existing attempts, while effective at recognizing
images within the same patent, fail to deliver practical value due to their
limited generalizability in retrieving relevant prior art. Moreover, this task
inherently involves the challenges posed by the abstract visual features of
patent images, the skewed distribution of image classifications, and the
semantic information of image descriptions. Therefore, we propose a
language-informed, distribution-aware multimodal approach to patent image
feature learning, which enriches the semantic understanding of patent image by
integrating Large Language Models and improves the performance of
underrepresented classes with our proposed distribution-aware contrastive
losses. Extensive experiments on DeepPatent2 dataset show that our proposed
method achieves state-of-the-art or comparable performance in image-based
patent retrieval with mAP +53.3%, Recall@10 +41.8%, and MRR@10 +51.9%.
Furthermore, through an in-depth user analysis, we explore our model in aiding
patent professionals in their image retrieval efforts, highlighting the model's
real-world applicability and effectiveness.