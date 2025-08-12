---
layout: publication
title: Heavy-tailed Kernels Reveal A Finer Cluster Structure In T-sne Visualisations
authors: Dmitry Kobak, George Linderman, Stefan Steinerberger, Yuval Kluger, Philipp
  Berens
conference: Lecture Notes in Computer Science
year: 2020
bibkey: kobak2019heavy
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.05804'}]
tags: []
short_authors: Kobak et al.
---
T-distributed stochastic neighbour embedding (t-SNE) is a widely used data
visualisation technique. It differs from its predecessor SNE by the
low-dimensional similarity kernel: the Gaussian kernel was replaced by the
heavy-tailed Cauchy kernel, solving the "crowding problem" of SNE. Here, we
develop an efficient implementation of t-SNE for a \\(t\\)-distribution kernel with
an arbitrary degree of freedom \\(\nu\\), with \\(\nu\to\infty\\) corresponding to SNE
and \\(\nu=1\\) corresponding to the standard t-SNE. Using theoretical analysis and
toy examples, we show that \\(\nu<1\\) can further reduce the crowding problem and
reveal finer cluster structure that is invisible in standard t-SNE. We further
demonstrate the striking effect of heavier-tailed kernels on large real-life
data sets such as MNIST, single-cell RNA-sequencing data, and the HathiTrust
library. We use domain knowledge to confirm that the revealed clusters are
meaningful. Overall, we argue that modifying the tail heaviness of the t-SNE
kernel can yield additional insight into the cluster structure of the data.