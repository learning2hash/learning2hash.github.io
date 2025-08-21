---
layout: publication
title: Faster Person Re-identification
authors: Guan'An Wang, Shaogang Gong, Jian Cheng, Zengguang Hou
conference: Lecture Notes in Computer Science
year: 2020
bibkey: wang2020faster
citations: 54
additional_links: [{name: Code, url: 'https://github.com/wangguanan/light-reid.'},
  {name: Paper, url: 'https://arxiv.org/abs/2008.06826'}]
tags: ["Compact Codes", "Datasets", "Hashing Methods", "Tools & Libraries"]
short_authors: Wang et al.
---
Fast person re-identification (ReID) aims to search person images quickly and
accurately. The main idea of recent fast ReID methods is the hashing algorithm,
which learns compact binary codes and performs fast Hamming distance and
counting sort. However, a very long code is needed for high accuracy (e.g.
2048), which compromises search speed. In this work, we introduce a new
solution for fast ReID by formulating a novel Coarse-to-Fine (CtF) hashing code
search strategy, which complementarily uses short and long codes, achieving
both faster speed and better accuracy. It uses shorter codes to coarsely rank
broad matching similarities and longer codes to refine only a few top
candidates for more accurate instance ReID. Specifically, we design an
All-in-One (AiO) framework together with a Distance Threshold Optimization
(DTO) algorithm. In AiO, we simultaneously learn and enhance multiple codes of
different lengths in a single model. It learns multiple codes in a pyramid
structure, and encourage shorter codes to mimic longer codes by
self-distillation. DTO solves a complex threshold search problem by a simple
optimization process, and the balance between accuracy and speed is easily
controlled by a single parameter. It formulates the optimization target as a
\(F_\{\beta\}\) score that can be optimised by Gaussian cumulative distribution
functions. Experimental results on 2 datasets show that our proposed method
(CtF) is not only 8% more accurate but also 5x faster than contemporary hashing
ReID methods. Compared with non-hashing ReID methods, CtF is \(50\times\) faster
with comparable accuracy. Code is available at
https://github.com/wangguanan/light-reid.