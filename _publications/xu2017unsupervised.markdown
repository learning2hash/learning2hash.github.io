---
layout: publication
title: Unsupervised Part-based Weighting Aggregation Of Deep Convolutional Features
  For Image Retrieval
authors: Jian Xu, Cunzhao Shi, Chengzuo Qi, Chunheng Wang, Baihua Xiao
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2018
bibkey: xu2017unsupervised
citations: 48
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.01247'}]
tags: ["AAAI", "Datasets", "Image Retrieval", "Supervised", "Unsupervised"]
short_authors: Xu et al.
---
In this paper, we propose a simple but effective semantic part-based
weighting aggregation (PWA) for image retrieval. The proposed PWA utilizes the
discriminative filters of deep convolutional layers as part detectors.
Moreover, we propose the effective unsupervised strategy to select some part
detectors to generate the "probabilistic proposals", which highlight certain
discriminative parts of objects and suppress the noise of background. The final
global PWA representation could then be acquired by aggregating the regional
representations weighted by the selected "probabilistic proposals"
corresponding to various semantic content. We conduct comprehensive experiments
on four standard datasets and show that our unsupervised PWA outperforms the
state-of-the-art unsupervised and supervised aggregation methods. Code is
available at https://github.com/XJhaoren/PWA.