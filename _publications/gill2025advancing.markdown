---
layout: publication
title: Advancing Semantic Caching For Llms With Domain-specific Embeddings And Synthetic
  Data
authors: Gill Waris 1 And 2, Cechmanek Justin Redis, Hutcherson Tyler Redis, Rajamohan
  Srijith Redis, Agarwal Jen Redis, Gulzar Muhammad Ali Virginia Tech, Singh Manvinder
  Redis, Dion Benoit
conference: Arxiv
year: 2025
bibkey: gill2025advancing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.02268'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Neural Hashing", "Similarity Search", "Transformer-based ANN"]
short_authors: Gill et al.
---
This report investigates enhancing semantic caching effectiveness by
employing specialized, fine-tuned embedding models. Semantic caching relies on
embedding similarity rather than exact key matching, presenting unique
challenges in balancing precision, query latency, and computational efficiency.
We propose leveraging smaller, domain-specific embedding models, fine-tuned
with targeted real-world and synthetically generated datasets. Our empirical
evaluations demonstrate that compact embedding models fine-tuned for just one
epoch on specialized datasets significantly surpass both state-of-the-art
open-source and proprietary alternatives in precision and recall. Moreover, we
introduce a novel synthetic data generation pipeline for the semantic cache
that mitigates the challenge of limited domain-specific annotated data, further
boosting embedding performance. Our approach effectively balances computational
overhead and accuracy, establishing a viable and efficient strategy for
practical semantic caching implementations.