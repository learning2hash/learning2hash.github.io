---
layout: publication
title: Unsupervised Multi45;index Semantic Hashing
authors: Hansen Christian, Hansen Casper, Simonsen Jakob Grue, Alstrup Stephen, Lioma Christina
conference: "Arxiv"
year: 2021
bibkey: hansen2021unsupervised
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2103.14460"}
tags: ['ARXIV', 'Unsupervised']
---
Semantic hashing represents documents as compact binary vectors (hash codes) and allows both efficient and effective similarity search in large45;scale information retrieval. The state of the art has primarily focused on learning hash codes that improve similarity search effectiveness while assuming a brute45;force linear scan strategy for searching over all the hash codes even though much faster alternatives exist. One such alternative is multi45;index hashing an approach that constructs a smaller candidate set to search over which depending on the distribution of the hash codes can lead to sub45;linear search time. In this work we propose Multi45;Index Semantic Hashing (MISH) an unsupervised hashing model that learns hash codes that are both effective and highly efficient by being optimized for multi45;index hashing. We derive novel training objectives which enable to learn hash codes that reduce the candidate sets produced by multi45;index hashing while being end45;to45;end trainable. In fact our proposed training objectives are model agnostic i.e. not tied to how the hash codes are generated specifically in MISH and are straight45;forward to include in existing and future semantic hashing models. We experimentally compare MISH to state45;of45;the45;art semantic hashing baselines in the task of document similarity search. We find that even though multi45;index hashing also improves the efficiency of the baselines compared to a linear scan they are still upwards of 3337; slower than MISH while MISH is still able to obtain state45;of45;the45;art effectiveness.
