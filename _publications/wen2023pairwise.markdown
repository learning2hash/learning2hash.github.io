---
layout: publication
title: Pairwise Similarity Learning Is Simple
authors: "Yandong Wen, Weiyang Liu, Yao Feng, Bhiksha Raj, Rita Singh, Adrian Weller,\
  \ Michael J. Black, Bernhard Sch\xF6lkopf"
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: wen2023pairwise
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.09449'}]
tags: ["Evaluation", "ICCV", "Image Retrieval", "Scalability"]
short_authors: Wen et al.
---
In this paper, we focus on a general yet important learning problem, pairwise
similarity learning (PSL). PSL subsumes a wide range of important applications,
such as open-set face recognition, speaker verification, image retrieval and
person re-identification. The goal of PSL is to learn a pairwise similarity
function assigning a higher similarity score to positive pairs (i.e., a pair of
samples with the same label) than to negative pairs (i.e., a pair of samples
with different label). We start by identifying a key desideratum for PSL, and
then discuss how existing methods can achieve this desideratum. We then propose
a surprisingly simple proxy-free method, called SimPLE, which requires neither
feature/proxy normalization nor angular margin and yet is able to generalize
well in open-set recognition. We apply the proposed method to three challenging
PSL tasks: open-set face recognition, image retrieval and speaker verification.
Comprehensive experimental results on large-scale benchmarks show that our
method performs significantly better than current state-of-the-art methods.