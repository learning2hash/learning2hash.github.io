---
layout: publication
title: Embedding-based Zero-shot Retrieval through Query Generation
authors: Liang et al.
conference: Arxiv
year: 2020
bibkey: liang2020embedding
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.10270'}]
tags: ["Few Shot & Zero Shot"]
---
Passage retrieval addresses the problem of locating relevant passages,
usually from a large corpus, given a query. In practice, lexical term-matching
algorithms like BM25 are popular choices for retrieval owing to their
efficiency. However, term-based matching algorithms often miss relevant
passages that have no lexical overlap with the query and cannot be finetuned to
downstream datasets. In this work, we consider the embedding-based two-tower
architecture as our neural retrieval model. Since labeled data can be scarce
and because neural retrieval models require vast amounts of data to train, we
propose a novel method for generating synthetic training data for retrieval.
Our system produces remarkable results, significantly outperforming BM25 on 5
out of 6 datasets tested, by an average of 2.45 points for Recall@1. In some
cases, our model trained on synthetic data can even outperform the same model
trained on real data