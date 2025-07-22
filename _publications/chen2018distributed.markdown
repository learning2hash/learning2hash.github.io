---
layout: publication
title: Distributed Collaborative Hashing and Its Applications in Ant Financial
authors: Chen Chaochao, Liu Ziqi, Zhao Peilin, Li Longfei, Zhou Jun, Li Xiaolong
conference: Proceedings of the 24th ACM SIGKDD International Conference on Knowledge
  Discovery &amp; Data Mining
year: 2018
bibkey: chen2018distributed
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.04918'}]
tags: ["Tools-&-Libraries", "Hashing-Methods", "Datasets", "Recommender-Systems", "KDD", "Scalability", "Evaluation", "Efficiency"]
short_authors: Chen et al.
---
Collaborative filtering, especially latent factor model, has been popularly
used in personalized recommendation. Latent factor model aims to learn user and
item latent factors from user-item historic behaviors. To apply it into real
big data scenarios, efficiency becomes the first concern, including offline
model training efficiency and online recommendation efficiency. In this paper,
we propose a Distributed Collaborative Hashing (DCH) model which can
significantly improve both efficiencies. Specifically, we first propose a
distributed learning framework, following the state-of-the-art parameter server
paradigm, to learn the offline collaborative model. Our model can be learnt
efficiently by distributedly computing subgradients in minibatches on workers
and updating model parameters on servers asynchronously. We then adopt hashing
technique to speedup the online recommendation procedure. Recommendation can be
quickly made through exploiting lookup hash tables. We conduct thorough
experiments on two real large-scale datasets. The experimental results
demonstrate that, comparing with the classic and state-of-the-art (distributed)
latent factor models, DCH has comparable performance in terms of recommendation
accuracy but has both fast convergence speed in offline model training
procedure and realtime efficiency in online recommendation procedure.
Furthermore, the encouraging performance of DCH is also shown for several
real-world applications in Ant Financial.