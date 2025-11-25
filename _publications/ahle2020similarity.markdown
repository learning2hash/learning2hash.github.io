---
layout: publication
title: Similarity Search With Tensor Core Units
authors: Thomas D. Ahle, Francesco Silvestri
conference: Lecture Notes in Computer Science
year: 2020
bibkey: ahle2020similarity
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.12608'}]
tags: ["Efficiency", "Similarity Search"]
short_authors: Thomas D. Ahle, Francesco Silvestri
---
Tensor Core Units (TCUs) are hardware accelerators developed for deep neural
networks, which efficiently support the multiplication of two dense
\(\sqrt\{m\}\times \sqrt\{m\}\) matrices, where \(m\) is a given hardware parameter. In
this paper, we show that TCUs can speed up similarity search problems as well.
We propose algorithms for the Johnson-Lindenstrauss dimensionality reduction
and for similarity join that, by leveraging TCUs, achieve a \(\sqrt\{m\}\) speedup
up with respect to traditional approaches.