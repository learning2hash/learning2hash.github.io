---
layout: publication
title: Deeply Supervised Semantic Model For Click-through Rate Prediction In Sponsored
  Search
authors: Jelena Gligorijevic, Djordje Gligorijevic, Ivan Stojkovic, Xiao Bai, Amit
  Goyal, Zoran Obradovic
conference: Arxiv
year: 2018
bibkey: gligorijevic2018deeply
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.10739'}]
tags: ["Large Scale Search", "Supervised"]
short_authors: Gligorijevic et al.
---
In sponsored search it is critical to match ads that are relevant to a query
and to accurately predict their likelihood of being clicked. Commercial search
engines typically use machine learning models for both query-ad relevance
matching and click-through-rate (CTR) prediction. However, matching models are
based on the similarity between a query and an ad, ignoring the fact that a
retrieved ad may not attract clicks, while click models rely on click history,
being of limited use for new queries and ads. We propose a deeply supervised
architecture that jointly learns the semantic embeddings of a query and an ad
as well as their corresponding CTR.We also propose a novel cohort negative
sampling technique for learning implicit negative signals. We trained the
proposed architecture using one billion query-ad pairs from a major commercial
web search engine. This architecture improves the best-performing baseline deep
neural architectures by 2% of AUC for CTR prediction and by statistically
significant 0.5% of NDCG for query-ad matching.