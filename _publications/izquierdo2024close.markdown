---
layout: publication
title: 'Close, But Not There: Boosting Geographic Distance Sensitivity In Visual Place
  Recognition'
authors: Sergio Izquierdo, Javier Civera
conference: Lecture Notes in Computer Science
year: 2024
bibkey: izquierdo2024close
citations: 4
additional_links: [{name: Code, url: 'https://github.com/serizba/cliquemining'}, {
    name: Paper, url: 'https://arxiv.org/abs/2407.02422'}]
tags: ["Evaluation"]
short_authors: Sergio Izquierdo, Javier Civera
---
Visual Place Recognition (VPR) plays a critical role in many localization and
mapping pipelines. It consists of retrieving the closest sample to a query
image, in a certain embedding space, from a database of geotagged references.
The image embedding is learned to effectively describe a place despite
variations in visual appearance, viewpoint, and geometric changes. In this
work, we formulate how limitations in the Geographic Distance Sensitivity of
current VPR embeddings result in a high probability of incorrectly sorting the
top-k retrievals, negatively impacting the recall. In order to address this
issue in single-stage VPR, we propose a novel mining strategy, CliqueMining,
that selects positive and negative examples by sampling cliques from a graph of
visually similar images. Our approach boosts the sensitivity of VPR embeddings
at small distance ranges, significantly improving the state of the art on
relevant benchmarks. In particular, we raise recall@1 from 75% to 82% in MSLS
Challenge, and from 76% to 90% in Nordland. Models and code are available at
https://github.com/serizba/cliquemining.