---
layout: publication
title: 'Felrec: Efficient Handling Of Item Cold-start With Dynamic Representation
  Learning In Recommender Systems'
authors: Kuba Weimann, Tim O. F. Conrad
conference: International Journal of Data Science and Analytics
year: 2024
bibkey: weimann2022felrec
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.16928'}]
tags: ["Datasets", "Few Shot & Zero Shot", "Recommender Systems"]
short_authors: Kuba Weimann, Tim O. F. Conrad
---
Recommender systems suffer from the cold-start problem whenever a new user
joins the platform or a new item is added to the catalog. To address item
cold-start, we propose to replace the embedding layer in sequential
recommenders with a dynamic storage that has no learnable weights and can keep
an arbitrary number of representations. In this paper, we present FELRec, a
large embedding network that refines the existing representations of users and
items in a recursive manner, as new information becomes available. In contrast
to similar approaches, our model represents new users and items without side
information and time-consuming finetuning, instead it runs a single forward
pass over a sequence of existing representations. During item cold-start, our
method outperforms similar method by 29.50%-47.45%. Further, our proposed model
generalizes well to previously unseen datasets in zero-shot settings. The
source code is publicly available at https://github.com/kweimann/FELRec .