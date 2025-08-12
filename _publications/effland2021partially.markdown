---
layout: publication
title: Partially Supervised Named Entity Recognition Via The Expected Entity Ratio
  Loss
authors: Thomas Effland, Michael Collins
conference: Transactions of the Association for Computational Linguistics
year: 2021
bibkey: effland2021partially
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.07216'}]
tags: ["Supervised", "TACL"]
short_authors: Thomas Effland, Michael Collins
---
We study learning named entity recognizers in the presence of missing entity
annotations. We approach this setting as tagging with latent variables and
propose a novel loss, the Expected Entity Ratio, to learn models in the
presence of systematically missing tags. We show that our approach is both
theoretically sound and empirically useful. Experimentally, we find that it
meets or exceeds performance of strong and state-of-the-art baselines across a
variety of languages, annotation scenarios, and amounts of labeled data. In
particular, we find that it significantly outperforms the previous
state-of-the-art methods from Mayhew et al. (2019) and Li et al. (2021) by
+12.7 and +2.3 F1 score in a challenging setting with only 1,000 biased
annotations, averaged across 7 datasets. We also show that, when combined with
our approach, a novel sparse annotation scheme outperforms exhaustive
annotation for modest annotation budgets.