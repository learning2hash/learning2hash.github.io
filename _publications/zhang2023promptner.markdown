---
layout: publication
title: 'Promptner: A Prompting Method For Few-shot Named Entity Recognition Via K
  Nearest Neighbor Search'
authors: Mozhi Zhang, Hang Yan, Yaqian Zhou, Xipeng Qiu
conference: Arxiv
year: 2023
bibkey: zhang2023promptner
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.12217'}]
tags: ["Datasets", "Few Shot & Zero Shot"]
short_authors: Zhang et al.
---
Few-shot Named Entity Recognition (NER) is a task aiming to identify named
entities via limited annotated samples. Recently, prototypical networks have
shown promising performance in few-shot NER. Most of prototypical networks will
utilize the entities from the support set to construct label prototypes and use
the query set to compute span-level similarities and optimize these label
prototype representations. However, these methods are usually unsuitable for
fine-tuning in the target domain, where only the support set is available. In
this paper, we propose PromptNER: a novel prompting method for few-shot NER via
k nearest neighbor search. We use prompts that contains entity category
information to construct label prototypes, which enables our model to fine-tune
with only the support set. Our approach achieves excellent transfer learning
ability, and extensive experiments on the Few-NERD and CrossNER datasets
demonstrate that our model achieves superior performance over state-of-the-art
methods.