---
layout: publication
title: 'Quantization/clustering: When And Why Does K-means Work?'
authors: "Levrard Cl\xE9ment Lpsm Umr 8001"
conference: Arxiv
year: 2018
bibkey: levrard2018quantization
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.03742'}]
tags: [Quantization]
---
Though mostly used as a clustering algorithm, k-means are originally designed
as a quantization algorithm. Namely, it aims at providing a compression of a
probability distribution with k points. Building upon [21, 33], we try to
investigate how and when these two approaches are compatible. Namely, we show
that provided the sample distribution satisfies a margin like condition (in the
sense of [27] for supervised learning), both the associated empirical risk
minimizer and the output of Lloyd's algorithm provide almost optimal
classification in certain cases (in the sense of [6]). Besides, we also show
that they achieved fast and optimal convergence rates in terms of sample size
and compression risk.