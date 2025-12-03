---
layout: publication
title: Metric Compatible Training For Online Backfilling In Large-scale Retrieval
authors: Seonguk Seo, Mustafa Gokhan Uzunbas, Bohyung Han, Sara Cao, Ser-Nam Lim
conference: Arxiv
year: 2023
bibkey: seo2023metric
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.03767'}]
tags: ["Evaluation", "Image Retrieval", "Scalability", "Self-Supervised", "Tools & Libraries"]
short_authors: Seo et al.
---
Backfilling is the process of re-extracting all gallery embeddings from
upgraded models in image retrieval systems. It inevitably requires a
prohibitively large amount of computational cost and even entails the downtime
of the service. Although backward-compatible learning sidesteps this challenge
by tackling query-side representations, this leads to suboptimal solutions in
principle because gallery embeddings cannot benefit from model upgrades. We
address this dilemma by introducing an online backfilling algorithm, which
enables us to achieve a progressive performance improvement during the
backfilling process while not sacrificing the final performance of new model
after the completion of backfilling. To this end, we first propose a simple
distance rank merge technique for online backfilling. Then, we incorporate a
reverse transformation module for more effective and efficient merging, which
is further enhanced by adopting a metric-compatible contrastive learning
approach. These two components help to make the distances of old and new models
compatible, resulting in desirable merge results during backfilling with no
extra computational overhead. Extensive experiments show the effectiveness of
our framework on four standard benchmarks in various settings.