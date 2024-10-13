---
layout: publication
title: Count-min Sketch With Variable Number Of Hash Functions An Experimental Study
authors: Fusy Éric, Kucherov Gregory
conference: "Arxiv"
year: 2023
bibkey: fusy2023count
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2302.05245"}
tags: ['ARXIV', 'Independent']
---
Conservative Count-Min, an improved version of Count-Min sketch [Cormode,
Muthukrishnan 2005], is an online-maintained hashing-based data structure
summarizing element frequency information without storing elements themselves.
Although several works attempted to analyze the error that can be made by
Count-Min, the behavior of this data structure remains poorly understood. In
[Fusy, Kucherov 2022], we demonstrated that under the uniform distribution of
input elements, the error of conservative Count-Min follows two distinct
regimes depending on its load factor.
  In this work, we provide a series of experimental results providing new
insights into the behavior of conservative Count-Min. Our contributions can be
seen as twofold. On one hand, we provide a detailed experimental analysis of
the behavior of Count-Min sketch in different regimes and under several
representative probability distributions of input elements. On the other hand,
we demonstrate improvements that can be made by assigning a variable number of
hash functions to different elements. This includes, in particular, reduced
space of the data structure while still supporting a small error.
