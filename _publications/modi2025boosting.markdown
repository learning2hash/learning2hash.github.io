---
layout: publication
title: Boosting Weak Positives For Text Based Person Search
authors: Akshay Modi, Ashhar Aziz, Nilanjana Chatterjee, A V Subramanyam
conference: Arxiv
year: 2025
bibkey: modi2025boosting
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.17586'}]
tags: []
short_authors: Modi et al.
---
Large vision-language models have revolutionized cross-modal object
retrieval, but text-based person search (TBPS) remains a challenging task due
to limited data and fine-grained nature of the task. Existing methods primarily
focus on aligning image-text pairs into a common representation space, often
disregarding the fact that real world positive image-text pairs share a varied
degree of similarity in between them. This leads models to prioritize easy
pairs, and in some recent approaches, challenging samples are discarded as
noise during training. In this work, we introduce a boosting technique that
dynamically identifies and emphasizes these challenging samples during
training. Our approach is motivated from classical boosting technique and
dynamically updates the weights of the weak positives, wherein, the rank-1
match does not share the identity of the query. The weight allows these
misranked pairs to contribute more towards the loss and the network has to pay
more attention towards such samples. Our method achieves improved performance
across four pedestrian datasets, demonstrating the effectiveness of our
proposed module.