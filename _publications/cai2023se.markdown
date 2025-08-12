---
layout: publication
title: 'Se-shapelets: Semi-supervised Clustering Of Time Series Using Representative
  Shapelets'
authors: Borui Cai, Guangyan Huang, Shuiqiao Yang, Yong Xiang, Chi-Hung Chi
conference: Expert Systems with Applications
year: 2023
bibkey: cai2023se
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.03292'}]
tags: []
short_authors: Cai et al.
---
Shapelets that discriminate time series using local features (subsequences)
are promising for time series clustering. Existing time series clustering
methods may fail to capture representative shapelets because they discover
shapelets from a large pool of uninformative subsequences, and thus result in
low clustering accuracy. This paper proposes a Semi-supervised Clustering of
Time Series Using Representative Shapelets (SE-Shapelets) method, which
utilizes a small number of labeled and propagated pseudo-labeled time series to
help discover representative shapelets, thereby improving the clustering
accuracy. In SE-Shapelets, we propose two techniques to discover representative
shapelets for the effective clustering of time series. 1) A \textit\{salient
subsequence chain\} (\(SSC\)) that can extract salient subsequences (as candidate
shapelets) of a labeled/pseudo-labeled time series, which helps remove massive
uninformative subsequences from the pool. 2) A \textit\{linear discriminant
selection\} (\(LDS\)) algorithm to identify shapelets that can capture
representative local features of time series in different classes, for
convenient clustering. Experiments on UCR time series datasets demonstrate that
SE-shapelets discovers representative shapelets and achieves higher clustering
accuracy than counterpart semi-supervised time series clustering methods.