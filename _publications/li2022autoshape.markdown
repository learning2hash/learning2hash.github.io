---
layout: publication
title: 'AUTOSHAPE: An Autoencoder-shapelet Approach For Time Series Clustering'
authors: Guozhong Li, Byron Choi, Jianliang Xu, Sourav S Bhowmick, Daphne Ngar-Yin
  Mah, Grace Lai-Hung Wong
conference: Arxiv
year: 2022
bibkey: li2022autoshape
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.04313'}]
tags: ["Unsupervised"]
short_authors: Li et al.
---
Time series shapelets are discriminative subsequences that have been recently
found effective for time series clustering (TSC). The shapelets are convenient
for interpreting the clusters. Thus, the main challenge for TSC is to discover
high-quality variable-length shapelets to discriminate different clusters. In
this paper, we propose a novel autoencoder-shapelet approach (AUTOSHAPE), which
is the first study to take the advantage of both autoencoder and shapelet for
determining shapelets in an unsupervised manner. An autoencoder is specially
designed to learn high-quality shapelets. More specifically, for guiding the
latent representation learning, we employ the latest self-supervised loss to
learn the unified embeddings for variable-length shapelet candidates (time
series subsequences) of different variables, and propose the diversity loss to
select the discriminating embeddings in the unified space. We introduce the
reconstruction loss to recover shapelets in the original time series space for
clustering. Finally, we adopt Davies Bouldin index (DBI) to inform AUTOSHAPE of
the clustering performance during learning. We present extensive experiments on
AUTOSHAPE. To evaluate the clustering performance on univariate time series
(UTS), we compare AUTOSHAPE with 15 representative methods using UCR archive
datasets. To study the performance of multivariate time series (MTS), we
evaluate AUTOSHAPE on 30 UEA archive datasets with 5 competitive methods. The
results validate that AUTOSHAPE is the best among all the methods compared. We
interpret clusters with shapelets, and can obtain interesting intuitions about
clusters in two UTS case studies and one MTS case study, respectively.