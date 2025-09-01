---
layout: publication
title: 'Better Generalization With Semantic Ids: A Case Study In Ranking For Recommendations'
authors: Anima Singh, Trung Vu, Nikhil Mehta, Raghunandan Keshavan, Maheswaran Sathiamoorthy,
  Yilin Zheng, Lichan Hong, Lukasz Heldt, Li Wei, Devansh Tandon, Ed H. Chi, Xinyang
  Yi
conference: 18th ACM Conference on Recommender Systems
year: 2024
bibkey: singh2023better
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.08121'}]
tags: ["Hashing Methods", "Recommender Systems"]
short_authors: Singh et al.
---
Randomly-hashed item ids are used ubiquitously in recommendation models.
However, the learned representations from random hashing prevents
generalization across similar items, causing problems of learning unseen and
long-tail items, especially when item corpus is large, power-law distributed,
and evolving dynamically. In this paper, we propose using content-derived
features as a replacement for random ids. We show that simply replacing ID
features with content-based embeddings can cause a drop in quality due to
reduced memorization capability. To strike a good balance of memorization and
generalization, we propose to use Semantic IDs -- a compact discrete item
representation learned from frozen content embeddings using RQ-VAE that
captures the hierarchy of concepts in items -- as a replacement for random item
ids. Similar to content embeddings, the compactness of Semantic IDs poses a
problem of easy adaption in recommendation models. We propose novel methods for
adapting Semantic IDs in industry-scale ranking models, through hashing
sub-pieces of of the Semantic-ID sequences. In particular, we find that the
SentencePiece model that is commonly used in LLM tokenization outperforms
manually crafted pieces such as N-grams. To the end, we evaluate our approaches
in a real-world ranking model for YouTube recommendations. Our experiments
demonstrate that Semantic IDs can replace the direct use of video IDs by
improving the generalization ability on new and long-tail item slices without
sacrificing overall model quality.