---
layout: publication
title: Hierarchical Matching and Reasoning for Multi-Query Image Retrieval
authors: Ji Zhong, Li Zhihao, Zhang Yan, Wang Haoran, Pang Yanwei, Li Xuelong
conference: Neural Networks
year: 2024
bibkey: ji2023hierarchical
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.14460'}]
tags: ["Evaluation", "Datasets", "Image-Retrieval"]
short_authors: Ji et al.
---
As a promising field, Multi-Query Image Retrieval (MQIR) aims at searching
for the semantically relevant image given multiple region-specific text
queries. Existing works mainly focus on a single-level similarity between image
regions and text queries, which neglects the hierarchical guidance of
multi-level similarities and results in incomplete alignments. Besides, the
high-level semantic correlations that intrinsically connect different
region-query pairs are rarely considered. To address above limitations, we
propose a novel Hierarchical Matching and Reasoning Network (HMRN) for MQIR. It
disentangles MQIR into three hierarchical semantic representations, which is
responsible to capture fine-grained local details, contextual global scopes,
and high-level inherent correlations. HMRN comprises two modules: Scalar-based
Matching (SM) module and Vector-based Reasoning (VR) module. Specifically, the
SM module characterizes the multi-level alignment similarity, which consists of
a fine-grained local-level similarity and a context-aware global-level
similarity. Afterwards, the VR module is developed to excavate the potential
semantic correlations among multiple region-query pairs, which further explores
the high-level reasoning similarity. Finally, these three-level similarities
are aggregated into a joint similarity space to form the ultimate similarity.
Extensive experiments on the benchmark dataset demonstrate that our HMRN
substantially surpasses the current state-of-the-art methods. For instance,
compared with the existing best method Drill-down, the metric R@1 in the last
round is improved by 23.4%. Our source codes will be released at
https://github.com/LZH-053/HMRN.