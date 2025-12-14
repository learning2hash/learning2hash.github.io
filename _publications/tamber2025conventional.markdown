---
layout: publication
title: 'Conventional Contrastive Learning Often Falls Short: Improving Dense Retrieval
  With Cross-encoder Listwise Distillation And Synthetic Data'
authors: Manveer Singh Tamber, Suleman Kazi, Vivek Sourabh, Jimmy Lin
conference: Arxiv
year: 2025
bibkey: tamber2025conventional
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.19274'}]
tags: [Evaluation, Distance Metric Learning, Datasets, Self-Supervised]
short_authors: Tamber et al.
---
We investigate improving the retrieval effectiveness of embedding models through the lens of corpus-specific fine-tuning. Prior work has shown that fine-tuning with queries generated using a dataset's retrieval corpus can boost retrieval effectiveness for the dataset. However, we find that surprisingly, fine-tuning using the conventional InfoNCE contrastive loss often reduces effectiveness in state-of-the-art models. To overcome this, we revisit cross-encoder listwise distillation and demonstrate that, unlike using contrastive learning alone, listwise distillation can help more consistently improve retrieval effectiveness across multiple datasets. Additionally, we show that synthesizing more training data using diverse query types (such as claims, keywords, and questions) yields greater effectiveness than using any single query type alone, regardless of the query type used in evaluation. Our findings further indicate that synthetic queries offer comparable utility to human-written queries for training. We use our approach to train an embedding model that achieves state-of-the-art effectiveness among BERT embedding models. We release our model and both query generation and training code to facilitate further research.