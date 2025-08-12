---
layout: publication
title: Mining Latent Classes For Few-shot Segmentation
authors: Lihe Yang, Wei Zhuo, Lei Qi, Yinghuan Shi, Yang Gao
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: yang2021mining
citations: 117
additional_links: [{name: Code, url: 'https://github.com/LiheYoung/MiningFSS'}, {
    name: Paper, url: 'https://arxiv.org/abs/2103.15402'}]
tags: ["Few Shot & Zero Shot", "ICCV"]
short_authors: Yang et al.
---
Few-shot segmentation (FSS) aims to segment unseen classes given only a few
annotated samples. Existing methods suffer the problem of feature undermining,
i.e. potential novel classes are treated as background during training phase.
Our method aims to alleviate this problem and enhance the feature embedding on
latent novel classes. In our work, we propose a novel joint-training framework.
Based on conventional episodic training on support-query pairs, we add an
additional mining branch that exploits latent novel classes via transferable
sub-clusters, and a new rectification technique on both background and
foreground categories to enforce more stable prototypes. Over and above that,
our transferable sub-cluster has the ability to leverage extra unlabeled data
for further feature enhancement. Extensive experiments on two FSS benchmarks
demonstrate that our method outperforms previous state-of-the-art by a large
margin of 3.7% mIOU on PASCAL-5i and 7.0% mIOU on COCO-20i at the cost of 74%
fewer parameters and 2.5x faster inference speed. The source code is available
at https://github.com/LiheYoung/MiningFSS.