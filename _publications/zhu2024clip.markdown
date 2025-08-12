---
layout: publication
title: 'CLIP-VIS: Adapting CLIP For Open-vocabulary Video Instance Segmentation'
authors: Wenqi Zhu, Jiale Cao, Jin Xie, Shuangming Yang, Yanwei Pang
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2024
bibkey: zhu2024clip
citations: 2
additional_links: [{name: Code, url: 'https://github.com/zwq456/CLIP-VIS.git'}, {
    name: Paper, url: 'https://arxiv.org/abs/2403.12455'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Zhu et al.
---
Open-vocabulary video instance segmentation strives to segment and track
instances belonging to an open set of categories in a videos. The
vision-language model Contrastive Language-Image Pre-training (CLIP) has shown
robust zero-shot classification ability in image-level open-vocabulary tasks.
In this paper, we propose a simple encoder-decoder network, called CLIP-VIS, to
adapt CLIP for open-vocabulary video instance segmentation. Our CLIP-VIS adopts
frozen CLIP and introduces three modules, including class-agnostic mask
generation, temporal topK-enhanced matching, and weighted open-vocabulary
classification. Given a set of initial queries, class-agnostic mask generation
introduces a pixel decoder and a transformer decoder on CLIP pre-trained image
encoder to predict query masks and corresponding object scores and mask IoU
scores. Then, temporal topK-enhanced matching performs query matching across
frames using the K mostly matched frames. Finally, weighted open-vocabulary
classification first employs mask pooling to generate query visual features
from CLIP pre-trained image encoder, and second performs weighted
classification using object scores and mask IoU scores. Our CLIP-VIS does not
require the annotations of instance categories and identities. The experiments
are performed on various video instance segmentation datasets, which
demonstrate the effectiveness of our proposed method, especially for novel
categories. When using ConvNeXt-B as backbone, our CLIP-VIS achieves the AP and
APn scores of 32.2% and 40.2% on the validation set of LV-VIS dataset, which
outperforms OV2Seg by 11.1% and 23.9% respectively. We will release the source
code and models at https://github.com/zwq456/CLIP-VIS.git.