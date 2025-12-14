---
layout: publication
title: 'BEV-TSR: Text-scene Retrieval In BEV Space For Autonomous Driving'
authors: Tao Tang, Dafeng Wei, Zhengyu Jia, Tian Gao, Changwei Cai, Chengkai Hou,
  Peng Jia, Kun Zhan, Haiyang Sun, Jingchen Fan, Yixing Zhao, Fu Liu, Xiaodan Liang,
  Xianpeng Lang, Yang Wang
conference: Arxiv
year: 2024
bibkey: tang2024bev
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.01065'}]
tags: [Evaluation, Image Retrieval, Datasets, Tools & Libraries, Text Retrieval]
short_authors: Tang et al.
---
The rapid development of the autonomous driving industry has led to a
significant accumulation of autonomous driving data. Consequently, there comes
a growing demand for retrieving data to provide specialized optimization.
However, directly applying previous image retrieval methods faces several
challenges, such as the lack of global feature representation and inadequate
text retrieval ability for complex driving scenes. To address these issues,
firstly, we propose the BEV-TSR framework which leverages descriptive text as
an input to retrieve corresponding scenes in the Bird's Eye View (BEV) space.
Then to facilitate complex scene retrieval with extensive text descriptions, we
employ a large language model (LLM) to extract the semantic features of the
text inputs and incorporate knowledge graph embeddings to enhance the semantic
richness of the language embedding. To achieve feature alignment between the
BEV feature and language embedding, we propose Shared Cross-modal Embedding
with a set of shared learnable embeddings to bridge the gap between these two
modalities, and employ a caption generation task to further enhance the
alignment. Furthermore, there lack of well-formed retrieval datasets for
effective evaluation. To this end, we establish a multi-level retrieval
dataset, nuScenes-Retrieval, based on the widely adopted nuScenes dataset.
Experimental results on the multi-level nuScenes-Retrieval show that BEV-TSR
achieves state-of-the-art performance, e.g., 85.78% and 87.66% top-1 accuracy
on scene-to-text and text-to-scene retrieval respectively. Codes and datasets
will be available.