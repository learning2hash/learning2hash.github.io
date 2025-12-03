---
layout: publication
title: 'Online Machine Learning Techniques For Coq: A Comparison'
authors: "Liao Zhang, Lasse Blaauwbroek, Bartosz Piotrowski, Prokop \u010Cern\xFD\
  , Cezary Kaliszyk, Josef Urban"
conference: Lecture Notes in Computer Science
year: 2021
bibkey: zhang2021online
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.05207'}]
tags: ["Evaluation", "Hashing Methods", "Locality-Sensitive-Hashing", "Tools & Libraries"]
short_authors: Zhang et al.
---
We present a comparison of several online machine learning techniques for
tactical learning and proving in the Coq proof assistant. This work builds on
top of Tactician, a plugin for Coq that learns from proofs written by the user
to synthesize new proofs. Learning happens in an online manner, meaning that
Tactician's machine learning model is updated immediately every time the user
performs a step in an interactive proof. This has important advantages compared
to the more studied offline learning systems: (1) it provides the user with a
seamless, interactive experience with Tactician and, (2) it takes advantage of
locality of proof similarity, which means that proofs similar to the current
proof are likely to be found close by. We implement two online methods, namely
approximate k-nearest neighbors based on locality sensitive hashing forests and
random decision forests. Additionally, we conduct experiments with gradient
boosted trees in an offline setting using XGBoost. We compare the relative
performance of Tactician using these three learning methods on Coq's standard
library.