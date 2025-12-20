---
layout: publication
title: Residual Quantization With Implicit Neural Codebooks
authors: Iris A. M. Huijben, Matthijs Douze, Matthew Muckley, Ruud J. G. van Sloun,
  Jakob Verbeek
conference: Arxiv
year: 2024
bibkey: huijben2024residual
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.14732'}]
tags: ["Datasets", "Quantization"]
short_authors: Huijben et al.
---
Vector quantization is a fundamental operation for data compression and
vector search. To obtain high accuracy, multi-codebook methods represent each
vector using codewords across several codebooks. Residual quantization (RQ) is
one such method, which iteratively quantizes the error of the previous step.
While the error distribution is dependent on previously-selected codewords,
this dependency is not accounted for in conventional RQ as it uses a fixed
codebook per quantization step. In this paper, we propose QINCo, a neural RQ
variant that constructs specialized codebooks per step that depend on the
approximation of the vector from previous steps. Experiments show that QINCo
outperforms state-of-the-art methods by a large margin on several datasets and
code sizes. For example, QINCo achieves better nearest-neighbor search accuracy
using 12-byte codes than the state-of-the-art UNQ using 16 bytes on the
BigANN1M and Deep1M datasets.