---
layout: publication
title: Retrieving And Highlighting Action With Spatiotemporal Reference
authors: Seito Kasai, Yuchi Ishikawa, Masaki Hayashi, Yoshimitsu Aoki, Kensho Hara,
  Hirokatsu Kataoka
conference: Arxiv
year: 2020
bibkey: kasai2020retrieving
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.09183'}]
tags: ["Datasets", "Evaluation", "Multimodal Retrieval", "Tools & Libraries"]
short_authors: Kasai et al.
---
In this paper, we present a framework that jointly retrieves and
spatiotemporally highlights actions in videos by enhancing current deep
cross-modal retrieval methods. Our work takes on the novel task of action
highlighting, which visualizes where and when actions occur in an untrimmed
video setting. Action highlighting is a fine-grained task, compared to
conventional action recognition tasks which focus on classification or
window-based localization. Leveraging weak supervision from annotated captions,
our framework acquires spatiotemporal relevance maps and generates local
embeddings which relate to the nouns and verbs in captions. Through
experiments, we show that our model generates various maps conditioned on
different actions, in which conventional visual reasoning methods only go as
far as to show a single deterministic saliency map. Also, our model improves
retrieval recall over our baseline without alignment by 2-3% on the MSR-VTT
dataset.