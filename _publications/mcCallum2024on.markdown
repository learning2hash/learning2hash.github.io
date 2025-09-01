---
layout: publication
title: On The Effect Of Data-augmentation On Local Embedding Properties In The Contrastive
  Learning Of Music Audio Representations
authors: Matthew C. McCallum, Matthew E. P. Davies, Florian Henkel, Jaehun Kim, Samuel
  E. Sandberg
conference: ICASSP 2024 - 2024 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2024
bibkey: mcCallum2024on
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.08889'}]
tags: ["Datasets", "Evaluation", "ICASSP", "Recommender Systems", "Self-Supervised"]
short_authors: McCallum et al.
---
Audio embeddings are crucial tools in understanding large catalogs of music.
Typically embeddings are evaluated on the basis of the performance they provide
in a wide range of downstream tasks, however few studies have investigated the
local properties of the embedding spaces themselves which are important in
nearest neighbor algorithms, commonly used in music search and recommendation.
In this work we show that when learning audio representations on music datasets
via contrastive learning, musical properties that are typically homogeneous
within a track (e.g., key and tempo) are reflected in the locality of
neighborhoods in the resulting embedding space. By applying appropriate data
augmentation strategies, localisation of such properties can not only be
reduced but the localisation of other attributes is increased. For example,
locality of features such as pitch and tempo that are less relevant to
non-expert listeners, may be mitigated while improving the locality of more
salient features such as genre and mood, achieving state-of-the-art performance
in nearest neighbor retrieval accuracy. Similarly, we show that the optimal
selection of data augmentation strategies for contrastive learning of music
audio embeddings is dependent on the downstream task, highlighting this as an
important embedding design decision.