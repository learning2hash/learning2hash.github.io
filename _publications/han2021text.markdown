---
layout: publication
title: Text-based Person Search With Limited Data
authors: Xiao Han, Sen He, Li Zhang, Tao Xiang
conference: Arxiv
year: 2021
bibkey: han2021text
citations: 36
additional_links: [{name: Code, url: 'https://github.com/BrandonHanx/TextReID'}, {
    name: Paper, url: 'https://arxiv.org/abs/2110.10807'}]
tags: ["Datasets", "Evaluation", "Multimodal Retrieval", "Scalability", "Self-Supervised"]
short_authors: Han et al.
---
Text-based person search (TBPS) aims at retrieving a target person from an
image gallery with a descriptive text query. Solving such a fine-grained
cross-modal retrieval task is challenging, which is further hampered by the
lack of large-scale datasets. In this paper, we present a framework with two
novel components to handle the problems brought by limited data. Firstly, to
fully utilize the existing small-scale benchmarking datasets for more
discriminative feature learning, we introduce a cross-modal momentum
contrastive learning framework to enrich the training data for a given
mini-batch. Secondly, we propose to transfer knowledge learned from existing
coarse-grained large-scale datasets containing image-text pairs from
drastically different problem domains to compensate for the lack of TBPS
training data. A transfer learning method is designed so that useful
information can be transferred despite the large domain gap. Armed with these
components, our method achieves new state of the art on the CUHK-PEDES dataset
with significant improvements over the prior art in terms of Rank-1 and mAP.
Our code is available at https://github.com/BrandonHanx/TextReID.