---
layout: publication
title: 'Furnishing Your Room By What You See: An End-to-end Furniture Set Retrieval
  Framework With Rich Annotated Benchmark Dataset'
authors: Bingyuan Liu, Jiantao Zhang, Xiaoting Zhang, Wei Zhang, Chuanhui Yu, Yuan
  Zhou
conference: Arxiv
year: 2019
bibkey: liu2019furnishing
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.09299'}]
tags: ["Datasets", "Evaluation", "Supervised"]
short_authors: Liu et al.
---
Understanding interior scenes has attracted enormous interest in computer
vision community. However, few works focus on the understanding of furniture
within the scenes and a large-scale dataset is also lacked to advance the
field. In this paper, we first fill the gap by presenting DeepFurniture, a
richly annotated large indoor scene dataset, including 24k indoor images, 170k
furniture instances and 20k unique furniture identities. On the dataset, we
introduce a new benchmark, named furniture set retrieval. Given an indoor photo
as input, the task requires to detect all the furniture instances and search a
matched set of furniture identities. To address this challenging task, we
propose a feature and context embedding based framework. It contains 3 major
contributions: (1) An improved Mask-RCNN model with an additional mask-based
classifier is introduced for better utilizing the mask information to relieve
the occlusion problems in furniture detection context. (2) A multi-task style
Siamese network is proposed to train the feature embedding model for retrieval,
which is composed of a classification subnet supervised by self-clustered
pseudo attributes and a verification subnet to estimate whether the input pair
is matched. (3) In order to model the relationship of the furniture entities in
an interior design, a context embedding model is employed to re-rank the
retrieval results. Extensive experiments demonstrate the effectiveness of each
module and the overall system.