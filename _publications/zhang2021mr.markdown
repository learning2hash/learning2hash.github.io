---
layout: publication
title: 'Mr. Tydi: A Multi-lingual Benchmark For Dense Retrieval'
authors: Zhang et al.
conference: Proceedings of the 1st Workshop on Multilingual Representation Learning
year: 2021
bibkey: zhang2021mr
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.08787'}]
tags: [Evaluation]
---
We present Mr. TyDi, a multi-lingual benchmark dataset for mono-lingual
retrieval in eleven typologically diverse languages, designed to evaluate
ranking with learned dense representations. The goal of this resource is to
spur research in dense retrieval techniques in non-English languages, motivated
by recent observations that existing techniques for representation learning
perform poorly when applied to out-of-distribution data. As a starting point,
we provide zero-shot baselines for this new dataset based on a multi-lingual
adaptation of DPR that we call "mDPR". Experiments show that although the
effectiveness of mDPR is much lower than BM25, dense representations
nevertheless appear to provide valuable relevance signals, improving BM25
results in sparse-dense hybrids. In addition to analyses of our results, we
also discuss future challenges and present a research agenda in multi-lingual
dense retrieval. Mr. TyDi can be downloaded at
https://github.com/castorini/mr.tydi.