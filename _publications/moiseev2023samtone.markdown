---
layout: publication
title: 'Samtone: Improving Contrastive Loss For Dual Encoder Retrieval Models With
  Same Tower Negatives'
authors: Fedor Moiseev, Gustavo Hernandez Abrego, Peter Dornbach, Imed Zitouni, Enrique
  Alfonseca, Zhe Dong
conference: 'Findings of the Association for Computational Linguistics: ACL 2023'
year: 2023
bibkey: moiseev2023samtone
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.02516'}]
tags: ["Distance Metric Learning"]
short_authors: Moiseev et al.
---
Dual encoders have been used for retrieval tasks and representation learning
with good results. A standard way to train dual encoders is using a contrastive
loss with in-batch negatives. In this work, we propose an improved contrastive
learning objective by adding queries or documents from the same encoder towers
to the negatives, for which we name it as "contrastive loss with SAMe TOwer
NEgatives" (SamToNe). By evaluating on question answering retrieval benchmarks
from MS MARCO and MultiReQA, and heterogenous zero-shot information retrieval
benchmarks (BEIR), we demonstrate that SamToNe can effectively improve the
retrieval quality for both symmetric and asymmetric dual encoders. By directly
probing the embedding spaces of the two encoding towers via the t-SNE algorithm
(van der Maaten and Hinton, 2008), we observe that SamToNe ensures the
alignment between the embedding spaces from the two encoder towers. Based on
the analysis of the embedding distance distributions of the top-\\(1\\) retrieved
results, we further explain the efficacy of the method from the perspective of
regularisation.