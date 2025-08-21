---
layout: publication
title: Active Learning For Finely-categorized Image-text Retrieval By Selecting Hard
  Negative Unpaired Samples
authors: Dae Ung Jo, Kyuewang Lee, Jaeho Chung, Jin Young Choi
conference: Arxiv
year: 2024
bibkey: jo2024active
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.16301'}]
tags: ["Datasets", "Text Retrieval"]
short_authors: Jo et al.
---
Securing a sufficient amount of paired data is important to train an
image-text retrieval (ITR) model, but collecting paired data is very expensive.
To address this issue, in this paper, we propose an active learning algorithm
for ITR that can collect paired data cost-efficiently. Previous studies assume
that image-text pairs are given and their category labels are asked to the
annotator. However, in the recent ITR studies, the importance of category label
is decreased since a retrieval model can be trained with only image-text pairs.
For this reason, we set up an active learning scenario where unpaired images
(or texts) are given and the annotator provides corresponding texts (or images)
to make paired data. The key idea of the proposed AL algorithm is to select
unpaired images (or texts) that can be hard negative samples for existing texts
(or images). To this end, we introduce a novel scoring function to choose hard
negative samples. We validate the effectiveness of the proposed method on
Flickr30K and MS-COCO datasets.