---
layout: publication
title: 'Apk2vec: Semi-supervised Multi-view Representation Learning For Profiling
  Android Applications'
authors: Annamalai Narayanan, Charlie Soh, Lihui Chen, Yang Liu, Lipo Wang
conference: 2018 IEEE International Conference on Data Mining (ICDM)
year: 2018
bibkey: narayanan2018apk2vec
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.05693'}]
tags: [Evaluation, Supervised, Scalability, Tools & Libraries, Hashing Methods, Recommender
    Systems]
short_authors: Narayanan et al.
---
Building behavior profiles of Android applications (apps) with holistic, rich
and multi-view information (e.g., incorporating several semantic views of an
app such as API sequences, system calls, etc.) would help catering downstream
analytics tasks such as app categorization, recommendation and malware analysis
significantly better. Towards this goal, we design a semi-supervised
Representation Learning (RL) framework named apk2vec to automatically generate
a compact representation (aka profile/embedding) for a given app. More
specifically, apk2vec has the three following unique characteristics which make
it an excellent choice for largescale app profiling: (1) it encompasses
information from multiple semantic views such as API sequences, permissions,
etc., (2) being a semi-supervised embedding technique, it can make use of
labels associated with apps (e.g., malware family or app category labels) to
build high quality app profiles, and (3) it combines RL and feature hashing
which allows it to efficiently build profiles of apps that stream over time
(i.e., online learning). The resulting semi-supervised multi-view hash
embeddings of apps could then be used for a wide variety of downstream tasks
such as the ones mentioned above. Our extensive evaluations with more than
42,000 apps demonstrate that apk2vec's app profiles could significantly
outperform state-of-the-art techniques in four app analytics tasks namely,
malware detection, familial clustering, app clone detection and app
recommendation.