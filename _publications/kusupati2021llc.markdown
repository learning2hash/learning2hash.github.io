---
layout: publication
title: LLC Accurate Multi-purpose Learnt Low-dimensional Binary Codes
authors: Aditya Kusupati, Matthew Wallingford, Vivek Ramanujan, Raghav Somani, Jae Sung Park, Krishna Pillutla, Prateek Jain, Sham Kakade, Ali Farhadi
conference: "Neural Information Processing Systems"
year: 2021
bibkey: kusupati2021llc
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2021/hash/c88d8d0a6097754525e02c2246d8d27f-Abstract.html"}
  - {name: "Code", url: "https://github.com/RAIVNLab/LLC"}
tags: ['Has Code', 'Image Retrieval', 'Information', 'NEURIPS', 'Supervised']
---
Learning binary representations of instances and classes is a classical problem with several high potential applications. In modern settings the compression of high-dimensional neural representations to low-dimensional binary codes is a challenging task and often require large bit-codes to be accurate. In this work we propose a novel method for ()earning ()ow-dimensional binary ()odes (()) for instances as well as classes. Our method does () require any side-information like annotated attributes or label meta-data and learns extremely low-dimensional binary codes ((approx 20) bits for ImageNet-1K). The learnt codes are super-efficient while still ensuring () classification accuracy for ResNet50 on ImageNet-1K. We demonstrate that the learnt codes capture intrinsically important features in the data by discovering an intuitive taxonomy over classes. We further quantitatively measure the quality of our codes by applying it to the efficient image retrieval as well as out-of-distribution (OOD) detection problems. For ImageNet-100 retrieval problem our learnt binary codes outperform (16) bit HashNet using only (10) bits and also are as accurate as (10) dimensional real representations. Finally our learnt binary codes can perform OOD detection out-of-the-box as accurately as a baseline that needs (approx3000) samples to tune its threshold while we require (). Code is open-sourced at https://github.com/RAIVNLab/LLC.
