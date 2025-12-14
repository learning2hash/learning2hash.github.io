---
layout: publication
title: 'Conaclip: Exploring Distillation Of Fully-connected Knowledge Interaction
  Graph For Lightweight Text-image Retrieval'
authors: Jiapeng Wang, Chengyu Wang, Xiaodan Wang, Jun Huang, Lianwen Jin
conference: Arxiv
year: 2023
bibkey: wang2023conaclip
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.17652'}]
tags: [Evaluation, Image Retrieval, Efficiency, Scalability, Text Retrieval]
short_authors: Wang et al.
---
Large-scale pre-trained text-image models with dual-encoder architectures
(such as CLIP) are typically adopted for various vision-language applications,
including text-image retrieval. However,these models are still less practical
on edge devices or for real-time situations, due to the substantial indexing
and inference time and the large consumption of computational resources.
Although knowledge distillation techniques have been widely utilized for
uni-modal model compression, how to expand them to the situation when the
numbers of modalities and teachers/students are doubled has been rarely
studied. In this paper, we conduct comprehensive experiments on this topic and
propose the fully-Connected knowledge interaction graph (Cona) technique for
cross-modal pre-training distillation. Based on our findings, the resulting
ConaCLIP achieves SOTA performances on the widely-used Flickr30K and MSCOCO
benchmarks under the lightweight setting. An industry application of our method
on an e-commercial platform further demonstrates the significant effectiveness
of ConaCLIP.