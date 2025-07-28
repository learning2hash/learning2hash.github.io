---
layout: publication
title: Multi-similarity Contrastive Learning
authors: Emily Mu, John Guttag, Maggie Makar
conference: Arxiv
year: 2023
bibkey: mu2023multi
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.02712'}]
tags: ["Distance Metric Learning", "Self-Supervised"]
short_authors: Emily Mu, John Guttag, Maggie Makar
---
Given a similarity metric, contrastive methods learn a representation in
which examples that are similar are pushed together and examples that are
dissimilar are pulled apart. Contrastive learning techniques have been utilized
extensively to learn representations for tasks ranging from image
classification to caption generation. However, existing contrastive learning
approaches can fail to generalize because they do not take into account the
possibility of different similarity relations. In this paper, we propose a
novel multi-similarity contrastive loss (MSCon), that learns generalizable
embeddings by jointly utilizing supervision from multiple metrics of
similarity. Our method automatically learns contrastive similarity weightings
based on the uncertainty in the corresponding similarity, down-weighting
uncertain tasks and leading to better out-of-domain generalization to new
tasks. We show empirically that networks trained with MSCon outperform
state-of-the-art baselines on in-domain and out-of-domain settings.