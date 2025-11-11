---
layout: publication
title: Deep Music Retrieval For Fine-grained Videos By Exploiting Cross-modal-encoded
  Voice-overs
authors: Tingtian Li, Zixun Sun, Haoruo Zhang, Jin Li, Ziming Wu, Hui Zhan, Yipeng
  Yu, Hengcan Shi
conference: Proceedings of the 44th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2021
bibkey: li2021deep
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.10557'}]
tags: ["CVPR", "Distance Metric Learning", "Evaluation", "Few Shot & Zero Shot", "Survey Paper"]
short_authors: Li et al.
---
Recently, the witness of the rapidly growing popularity of short videos on
different Internet platforms has intensified the need for a background music
(BGM) retrieval system. However, existing video-music retrieval methods only
based on the visual modality cannot show promising performance regarding videos
with fine-grained virtual contents. In this paper, we also investigate the
widely added voice-overs in short videos and propose a novel framework to
retrieve BGM for fine-grained short videos. In our framework, we use the
self-attention (SA) and the cross-modal attention (CMA) modules to explore the
intra- and the inter-relationships of different modalities respectively. For
balancing the modalities, we dynamically assign different weights to the modal
features via a fusion gate. For paring the query and the BGM embeddings, we
introduce a triplet pseudo-label loss to constrain the semantics of the modal
embeddings. As there are no existing virtual-content video-BGM retrieval
datasets, we build and release two virtual-content video datasets HoK400 and
CFM400. Experimental results show that our method achieves superior performance
and outperforms other state-of-the-art methods with large margins.