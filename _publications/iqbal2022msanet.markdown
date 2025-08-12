---
layout: publication
title: 'Msanet: Multi-similarity And Attention Guidance For Boosting Few-shot Segmentation'
authors: Ehtesham Iqbal, Sirojbek Safarov, Seongdeok Bang
conference: Arxiv
year: 2022
bibkey: iqbal2022msanet
citations: 25
additional_links: [{name: Code, url: 'https://github.com/AIVResearch/MSANet'}, {name: Paper,
    url: 'https://arxiv.org/abs/2206.09667'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Ehtesham Iqbal, Sirojbek Safarov, Seongdeok Bang
---
Few-shot segmentation aims to segment unseen-class objects given only a
handful of densely labeled samples. Prototype learning, where the support
feature yields a singleor several prototypes by averaging global and local
object information, has been widely used in FSS. However, utilizing only
prototype vectors may be insufficient to represent the features for all
training data. To extract abundant features and make more precise predictions,
we propose a Multi-Similarity and Attention Network (MSANet) including two
novel modules, a multi-similarity module and an attention module. The
multi-similarity module exploits multiple feature-maps of support images and
query images to estimate accurate semantic relationships. The attention module
instructs the network to concentrate on class-relevant information. The network
is tested on standard FSS datasets, PASCAL-5i 1-shot, PASCAL-5i 5-shot,
COCO-20i 1-shot, and COCO-20i 5-shot. The MSANet with the backbone of
ResNet-101 achieves the state-of-the-art performance for all 4-benchmark
datasets with mean intersection over union (mIoU) of 69.13%, 73.99%, 51.09%,
56.80%, respectively. Code is available at
https://github.com/AIVResearch/MSANet