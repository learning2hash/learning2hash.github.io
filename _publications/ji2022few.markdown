---
layout: publication
title: Few-shot Named Entity Recognition With Entity-level Prototypical Network Enhanced
  By Dispersedly Distributed Prototypes
authors: Bin Ji, Shasha Li, Shaoduo Gan, Jie Yu, Jun Ma, Huijun Liu
conference: Arxiv
year: 2022
bibkey: ji2022few
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.08023'}]
tags: ["Evaluation", "Few Shot & Zero Shot"]
short_authors: Ji et al.
---
Few-shot named entity recognition (NER) enables us to build a NER system for
a new domain using very few labeled examples. However, existing prototypical
networks for this task suffer from roughly estimated label dependency and
closely distributed prototypes, thus often causing misclassifications. To
address the above issues, we propose EP-Net, an Entity-level Prototypical
Network enhanced by dispersedly distributed prototypes. EP-Net builds
entity-level prototypes and considers text spans to be candidate entities, so
it no longer requires the label dependency. In addition, EP-Net trains the
prototypes from scratch to distribute them dispersedly and aligns spans to
prototypes in the embedding space using a space projection. Experimental
results on two evaluation tasks and the Few-NERD settings demonstrate that
EP-Net consistently outperforms the previous strong models in terms of overall
performance. Extensive analyses further validate the effectiveness of EP-Net.