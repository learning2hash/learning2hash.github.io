---
layout: publication
title: Coresets For Kernel Clustering
authors: Shaofeng H. -C. Jiang, Robert Krauthgamer, Jianing Lou, Yubo Zhang
conference: Arxiv
year: 2021
bibkey: jiang2021coresets
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.02898'}]
tags: ["Efficiency"]
short_authors: Jiang et al.
---
We devise coresets for kernel \(k\)-Means with a general kernel, and use them
to obtain new, more efficient, algorithms. Kernel \(k\)-Means has superior
clustering capability compared to classical \(k\)-Means, particularly when
clusters are non-linearly separable, but it also introduces significant
computational challenges. We address this computational issue by constructing a
coreset, which is a reduced dataset that accurately preserves the clustering
costs.
  Our main result is a coreset for kernel \(k\)-Means that works for a general
kernel and has size \(\mathrm\{poly\}(k\epsilon^\{-1\})\). Our new coreset both
generalizes and greatly improves all previous results; moreover, it can be
constructed in time near-linear in \(n\). This result immediately implies new
algorithms for kernel \(k\)-Means, such as a \((1+\epsilon)\)-approximation in time
near-linear in \(n\), and a streaming algorithm using space and update time
\(\mathrm\{poly\}(k \epsilon^\{-1\} log n)\).
  We validate our coreset on various datasets with different kernels. Our
coreset performs consistently well, achieving small errors while using very few
points. We show that our coresets can speed up kernel \(k\)-Means++ (the
kernelized version of the widely used \(k\)-Means++ algorithm), and we further
use this faster kernel \(k\)-Means++ for spectral clustering. In both
applications, we achieve significant speedup and a better asymptotic growth
while the error is comparable to baselines that do not use coresets.