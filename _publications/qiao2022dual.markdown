---
layout: publication
title: Dual Skipping Guidance For Document Retrieval With Learned Sparse Representations
authors: Yifan Qiao, Yingrui Yang, Haixin Lin, Tianbo Xiong, Xiyue Wang, Tao Yang
conference: Arxiv
year: 2022
bibkey: qiao2022dual
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.11154'}]
tags: ["Efficiency", "Text Retrieval"]
short_authors: Qiao et al.
---
This paper proposes a dual skipping guidance scheme with hybrid scoring to
accelerate document retrieval that uses learned sparse representations while
still delivering a good relevance. This scheme uses both lexical BM25 and
learned neural term weights to bound and compose the rank score of a candidate
document separately for skipping and final ranking, and maintains two top-k
thresholds during inverted index traversal. This paper evaluates time
efficiency and ranking relevance of the proposed scheme in searching MS MARCO
TREC datasets.