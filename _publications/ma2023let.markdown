---
layout: publication
title: 'Let All Be Whitened: Multi-teacher Distillation For Efficient Visual Retrieval'
authors: Zhe Ma, Jianfeng Dong, Shouling Ji, Zhenguang Liu, Xuhong Zhang, Zonghui
  Wang, Sifeng He, Feng Qian, Xiaobo Zhang, Lei Yang
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2024
bibkey: ma2023let
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.09716'}]
tags: [Efficiency, Datasets, Image Retrieval, Video Retrieval, AAAI, Tools & Libraries,
  Evaluation]
short_authors: Ma et al.
---
Visual retrieval aims to search for the most relevant visual items, e.g.,
images and videos, from a candidate gallery with a given query item. Accuracy
and efficiency are two competing objectives in retrieval tasks. Instead of
crafting a new method pursuing further improvement on accuracy, in this paper
we propose a multi-teacher distillation framework Whiten-MTD, which is able to
transfer knowledge from off-the-shelf pre-trained retrieval models to a
lightweight student model for efficient visual retrieval. Furthermore, we
discover that the similarities obtained by different retrieval models are
diversified and incommensurable, which makes it challenging to jointly distill
knowledge from multiple models. Therefore, we propose to whiten the output of
teacher models before fusion, which enables effective multi-teacher
distillation for retrieval models. Whiten-MTD is conceptually simple and
practically effective. Extensive experiments on two landmark image retrieval
datasets and one video retrieval dataset demonstrate the effectiveness of our
proposed method, and its good balance of retrieval performance and efficiency.
Our source code is released at https://github.com/Maryeon/whiten_mtd.