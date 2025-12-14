---
layout: publication
title: 'Darwinian Model Upgrades: Model Evolving With Selective Compatibility'
authors: Binjie Zhang, Shupeng Su, Yixiao Ge, Xuyuan Xu, Yexin Wang, Chun Yuan, Mike
  Zheng Shou, Ying Shan
conference: Arxiv
year: 2022
bibkey: zhang2022darwinian
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.06954'}]
tags: [Scalability, Evaluation]
short_authors: Zhang et al.
---
The traditional model upgrading paradigm for retrieval requires recomputing
all gallery embeddings before deploying the new model (dubbed as
"backfilling"), which is quite expensive and time-consuming considering
billions of instances in industrial applications. BCT presents the first step
towards backward-compatible model upgrades to get rid of backfilling. It is
workable but leaves the new model in a dilemma between new feature
discriminativeness and new-to-old compatibility due to the undifferentiated
compatibility constraints. In this work, we propose Darwinian Model Upgrades
(DMU), which disentangle the inheritance and variation in the model evolving
with selective backward compatibility and forward adaptation, respectively. The
old-to-new heritable knowledge is measured by old feature discriminativeness,
and the gallery features, especially those of poor quality, are evolved in a
lightweight manner to become more adaptive in the new latent space. We
demonstrate the superiority of DMU through comprehensive experiments on
large-scale landmark retrieval and face recognition benchmarks. DMU effectively
alleviates the new-to-new degradation and improves new-to-old compatibility,
rendering a more proper model upgrading paradigm in large-scale retrieval
systems.