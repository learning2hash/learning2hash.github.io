---
layout: publication
title: Generalizable Semantic Vision Query Generation For Zero-shot Panoptic And Semantic
  Segmentation
authors: Jialei Chen, Daisuke Deguchi, Chenkai Zhang, Hiroshi Murase
conference: Arxiv
year: 2024
bibkey: chen2024generalizable
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.13697'}]
tags: []
short_authors: Chen et al.
---
Zero-shot Panoptic Segmentation (ZPS) aims to recognize foreground instances
and background stuff without images containing unseen categories in training.
Due to the visual data sparsity and the difficulty of generalizing from seen to
unseen categories, this task remains challenging. To better generalize to
unseen classes, we propose Conditional tOken aligNment and Cycle trAnsiTion
(CONCAT), to produce generalizable semantic vision queries. First, a feature
extractor is trained by CON to link the vision and semantics for providing
target queries. Formally, CON is proposed to align the semantic queries with
the CLIP visual CLS token extracted from complete and masked images. To address
the lack of unseen categories, a generator is required. However, one of the
gaps in synthesizing pseudo vision queries, ie, vision queries for unseen
categories, is describing fine-grained visual details through semantic
embeddings. Therefore, we approach CAT to train the generator in
semantic-vision and vision-semantic manners. In semantic-vision, visual query
contrast is proposed to model the high granularity of vision by pulling the
pseudo vision queries with the corresponding targets containing segments while
pushing those without segments away. To ensure the generated queries retain
semantic information, in vision-semantic, the pseudo vision queries are mapped
back to semantic and supervised by real semantic embeddings. Experiments on ZPS
achieve a 5.2% hPQ increase surpassing SOTA. We also examine inductive ZPS and
open-vocabulary semantic segmentation and obtain comparative results while
being 2 times faster in testing.