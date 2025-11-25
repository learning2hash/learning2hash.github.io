---
layout: publication
title: Unsupervised Part-based Weighting Aggregation Of Deep Convolutional Features
  For Image Retrieval
authors: Jian Xu, Cunzhao Shi, Chengzuo Qi, Chunheng Wang, Baihua Xiao
conference: Arxiv
year: 2017
bibkey: xu2017unsupervised
citations: 26
additional_links: [{name: Code, url: 'https://github.com/XJhaoren/PWA'}, {name: Paper,
    url: 'https://arxiv.org/abs/1705.01247'}]
tags: ["Image Retrieval", "Unsupervised"]
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