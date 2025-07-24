---
layout: publication
title: 'Towards Unified Text-based Person Retrieval: A Large-scale Multi-attribute
  And Language Search Benchmark'
authors: Shuyu Yang, Yinan Zhou, Yaxiong Wang, Yujiao Wu, Li Zhu, Zhedong Zheng
conference: Proceedings of the 31st ACM International Conference on Multimedia
year: 2023
bibkey: yang2023towards
citations: 60
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.02898'}]
tags: ["Datasets", "Evaluation", "Scalability"]
short_authors: Yang et al.
---
In this paper, we introduce a large Multi-Attribute and Language Search
dataset for text-based person retrieval, called MALS, and explore the
feasibility of performing pre-training on both attribute recognition and
image-text matching tasks in one stone. In particular, MALS contains 1,510,330
image-text pairs, which is about 37.5 times larger than prevailing CUHK-PEDES,
and all images are annotated with 27 attributes. Considering the privacy
concerns and annotation costs, we leverage the off-the-shelf diffusion models
to generate the dataset. To verify the feasibility of learning from the
generated data, we develop a new joint Attribute Prompt Learning and Text
Matching Learning (APTM) framework, considering the shared knowledge between
attribute and text. As the name implies, APTM contains an attribute prompt
learning stream and a text matching learning stream. (1) The attribute prompt
learning leverages the attribute prompts for image-attribute alignment, which
enhances the text matching learning. (2) The text matching learning facilitates
the representation learning on fine-grained details, and in turn, boosts the
attribute prompt learning. Extensive experiments validate the effectiveness of
the pre-training on MALS, achieving state-of-the-art retrieval performance via
APTM on three challenging real-world benchmarks. In particular, APTM achieves a
consistent improvement of +6.96%, +7.68%, and +16.95% Recall@1 accuracy on
CUHK-PEDES, ICFG-PEDES, and RSTPReid datasets by a clear margin, respectively.