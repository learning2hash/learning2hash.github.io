---
layout: publication
title: Exploring A Fine-grained Multiscale Method For Cross-modal Remote Sensing Image
  Retrieval
authors: Yuan Zhiqiang, Zhang Wenkai, Fu Kun, Li Xuan, Deng Chubo, Wang Hongqi, Sun
  Xian
conference: IEEE Transactions on Geoscience and Remote Sensing
year: 2021
bibkey: yuan2022exploring
citations: 110
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.09868'}]
tags: ["Distance Metric Learning", "Evaluation", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Yuan et al.
---
Remote sensing (RS) cross-modal text-image retrieval has attracted extensive
attention for its advantages of flexible input and efficient query. However,
traditional methods ignore the characteristics of multi-scale and redundant
targets in RS image, leading to the degradation of retrieval accuracy. To cope
with the problem of multi-scale scarcity and target redundancy in RS multimodal
retrieval task, we come up with a novel asymmetric multimodal feature matching
network (AMFMN). Our model adapts to multi-scale feature inputs, favors
multi-source retrieval methods, and can dynamically filter redundant features.
AMFMN employs the multi-scale visual self-attention (MVSA) module to extract
the salient features of RS image and utilizes visual features to guide the text
representation. Furthermore, to alleviate the positive samples ambiguity caused
by the strong intraclass similarity in RS image, we propose a triplet loss
function with dynamic variable margin based on prior similarity of sample
pairs. Finally, unlike the traditional RS image-text dataset with coarse text
and higher intraclass similarity, we construct a fine-grained and more
challenging Remote sensing Image-Text Match dataset (RSITMD), which supports RS
image retrieval through keywords and sentence separately and jointly.
Experiments on four RS text-image datasets demonstrate that the proposed model
can achieve state-of-the-art performance in cross-modal RS text-image retrieval
task.