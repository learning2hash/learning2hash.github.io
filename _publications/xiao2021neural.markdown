---
layout: publication
title: Neural Pathsim For Inductive Similarity Search In Heterogeneous Information
  Networks
authors: Xiao et al.
conference: Proceedings of the 30th ACM International Conference on Information &amp;
  Knowledge Management
year: 2021
bibkey: xiao2021neural
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.01549'}]
tags: [DATASETS, Evaluation, CIKM, Similarity Search, Tools & Libraries]
---
PathSim is a widely used meta-path-based similarity in heterogeneous
information networks. Numerous applications rely on the computation of PathSim,
including similarity search and clustering. Computing PathSim scores on large
graphs is computationally challenging due to its high time and storage
complexity. In this paper, we propose to transform the problem of approximating
the ground truth PathSim scores into a learning problem. We design an
encoder-decoder based framework, NeuPath, where the algorithmic structure of
PathSim is considered. Specifically, the encoder module identifies Top T
optimized path instances, which can approximate the ground truth PathSim, and
maps each path instance to an embedding vector. The decoder transforms each
embedding vector into a scalar respectively, which identifies the similarity
score. We perform extensive experiments on two real-world datasets in different
domains, ACM and IMDB. Our results demonstrate that NeuPath performs better
than state-of-the-art baselines in the PathSim approximation task and
similarity search task.