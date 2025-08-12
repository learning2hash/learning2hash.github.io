---
layout: publication
title: Incomplete Descriptor Mining With Elastic Loss For Person Re-identification
authors: Hongchen Tan, Yuhao Bian, Huasheng Wang, Xiuping Liu, Baocai Yin
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2021
bibkey: tan2020incomplete
citations: 62
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.04010'}]
tags: ["Image Retrieval"]
short_authors: Tan et al.
---
In this paper, we propose a novel person Re-ID model, Consecutive Batch
DropBlock Network (CBDB-Net), to capture the attentive and robust person
descriptor for the person Re-ID task. The CBDB-Net contains two novel designs:
the Consecutive Batch DropBlock Module (CBDBM) and the Elastic Loss (EL). In
the Consecutive Batch DropBlock Module (CBDBM), we firstly conduct uniform
partition on the feature maps. And then, we independently and continuously drop
each patch from top to bottom on the feature maps, which can output multiple
incomplete feature maps. In the training stage, these multiple incomplete
features can better encourage the Re-ID model to capture the robust person
descriptor for the Re-ID task. In the Elastic Loss (EL), we design a novel
weight control item to help the Re-ID model adaptively balance hard sample
pairs and easy sample pairs in the whole training process. Through an extensive
set of ablation studies, we verify that the Consecutive Batch DropBlock Module
(CBDBM) and the Elastic Loss (EL) each contribute to the performance boosts of
CBDB-Net. We demonstrate that our CBDB-Net can achieve the competitive
performance on the three standard person Re-ID datasets (the Market-1501, the
DukeMTMC-Re-ID, and the CUHK03 dataset), three occluded Person Re-ID datasets
(the Occluded DukeMTMC, the Partial-REID, and the Partial iLIDS dataset), and a
general image retrieval dataset (In-Shop Clothes Retrieval dataset).