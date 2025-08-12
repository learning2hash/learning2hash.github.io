---
layout: publication
title: 'LAVA: Label-efficient Visual Learning And Adaptation'
authors: Islam Nassar, Munawar Hayat, Ehsan Abbasnejad, Hamid Rezatofighi, Mehrtash
  Harandi, Gholamreza Haffari
conference: Arxiv
year: 2022
bibkey: nassar2022lava
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.10317'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Nassar et al.
---
We present LAVA, a simple yet effective method for multi-domain visual
transfer learning with limited data. LAVA builds on a few recent innovations to
enable adapting to partially labelled datasets with class and domain shifts.
First, LAVA learns self-supervised visual representations on the source dataset
and ground them using class label semantics to overcome transfer collapse
problems associated with supervised pretraining. Secondly, LAVA maximises the
gains from unlabelled target data via a novel method which uses multi-crop
augmentations to obtain highly robust pseudo-labels. By combining these
ingredients, LAVA achieves a new state-of-the-art on ImageNet semi-supervised
protocol, as well as on 7 out of 10 datasets in multi-domain few-shot learning
on the Meta-dataset. Code and models are made available.