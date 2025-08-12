---
layout: publication
title: Multi-level Correlation Network For Few-shot Image Classification
authors: Yunkai Dang, Min Zhang, Zhengyu Chen, Xinliang Zhang, Zheng Wang, Meijun
  Sun, Donglin Wang
conference: 2023 IEEE International Conference on Multimedia and Expo (ICME)
year: 2023
bibkey: dang2023multi
citations: 1
additional_links: [{name: Code, url: 'https://github.com/Yunkai696/MLCN'}, {name: Paper,
    url: 'https://arxiv.org/abs/2412.03159'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Dang et al.
---
Few-shot image classification(FSIC) aims to recognize novel classes given few
labeled images from base classes. Recent works have achieved promising
classification performance, especially for metric-learning methods, where a
measure at only image feature level is usually used. In this paper, we argue
that measure at such a level may not be effective enough to generalize from
base to novel classes when using only a few images. Instead, a multi-level
descriptor of an image is taken for consideration in this paper. We propose a
multi-level correlation network (MLCN) for FSIC to tackle this problem by
effectively capturing local information. Concretely, we present the
self-correlation module and cross-correlation module to learn the semantic
correspondence relation of local information based on learned representations.
Moreover, we propose a pattern-correlation module to capture the pattern of
fine-grained images and find relevant structural patterns between base classes
and novel classes. Extensive experiments and analysis show the effectiveness of
our proposed method on four widely-used FSIC benchmarks. The code for our
approach is available at: https://github.com/Yunkai696/MLCN.