---
layout: publication
title: Embedding And Clustering Your Data Can Improve Contrastive Pretraining
authors: Luke Merrick
conference: Arxiv
year: 2024
bibkey: merrick2024embedding
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.18887'}]
tags: ["Scalability"]
short_authors: Luke Merrick
---
Recent studies of large-scale contrastive pretraining in the text embedding
domain show that using single-source minibatches, rather than mixed-source
minibatches, can substantially improve overall model accuracy. In this work, we
explore extending training data stratification beyond source granularity by
leveraging a pretrained text embedding model and the classic k-means clustering
algorithm to further split training data apart by the semantic clusters within
each source. Experimentally, we observe a notable increase in NDCG@10 when
pretraining a BERT-based text embedding model on query-passage pairs from the
MSMARCO passage retrieval dataset. Additionally, we conceptually connect our
clustering approach to both the Topic Aware Sampling (TAS) aspect of the TAS-B
methodology and the nearest-neighbor-based hard-negative mining aspect of the
ANCE methodology and discuss how this unified view motivates future lines of
research on the organization of contrastive pretraining data.