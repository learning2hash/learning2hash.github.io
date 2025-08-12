---
layout: publication
title: 'Learn From Foundation Model: Fruit Detection Model Without Manual Annotation'
authors: Yanan Wang, Zhenghao Fei, Ruichen Li, Yibin Ying
conference: Arxiv
year: 2024
bibkey: wang2024learn
citations: 0
additional_links: [{name: Code, url: 'https://github.com/AgRoboticsResearch/SDM-D.git'},
  {name: Paper, url: 'https://arxiv.org/abs/2411.16196'}]
tags: ["Few Shot & Zero Shot", "Tools & Libraries"]
short_authors: Wang et al.
---
Recent breakthroughs in large foundation models have enabled the possibility
of transferring knowledge pre-trained on vast datasets to domains with limited
data availability. Agriculture is one of the domains that lacks sufficient
data. This study proposes a framework to train effective, domain-specific,
small models from foundation models without manual annotation. Our approach
begins with SDM (Segmentation-Description-Matching), a stage that leverages two
foundation models: SAM2 (Segment Anything in Images and Videos) for
segmentation and OpenCLIP (Open Contrastive Language-Image Pretraining) for
zero-shot open-vocabulary classification. In the second stage, a novel
knowledge distillation mechanism is utilized to distill compact,
edge-deployable models from SDM, enhancing both inference speed and perception
accuracy. The complete method, termed SDM-D
(Segmentation-Description-Matching-Distilling), demonstrates strong performance
across various fruit detection tasks object detection, semantic segmentation,
and instance segmentation) without manual annotation. It nearly matches the
performance of models trained with abundant labels. Notably, SDM-D outperforms
open-set detection methods such as Grounding SAM and YOLO-World on all tested
fruit detection datasets. Additionally, we introduce MegaFruits, a
comprehensive fruit segmentation dataset encompassing over 25,000 images, and
all code and datasets are made publicly available at
https://github.com/AgRoboticsResearch/SDM-D.git.