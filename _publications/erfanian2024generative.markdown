---
layout: publication
title: 'Needle: A Generative Ai-powered Multi-modal Database For Answering Complex Natural Language Queries'
authors: Mahdi Erfanian, Mohsen Dehghankar, Abolfazl Asudeh
conference: "Arxiv"
year: 2024
citations: 0
bibkey: erfanian2024generative
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2412.00639'}
tags: ['Cross-Modal', 'Deep', 'Unsupervised', 'Retrieval Models', 'Datasets', 'Applications']
---
Multi-modal datasets, like those involving images, often miss the detailed descriptions that properly capture the rich information encoded in each item. This makes answering complex natural language queries a major challenge in this domain. In particular, unlike the traditional nearest neighbor search, where the tuples and the query are represented as points in a single metric space, these settings involve queries and tuples embedded in fundamentally different spaces, making the traditional query answering methods inapplicable. Existing literature addresses this challenge for image datasets through vector representations jointly trained on natural language and images. This technique, however, underperforms for complex queries due to various reasons.
  This paper takes a step towards addressing this challenge by introducing a Generative-based Monte Carlo method that utilizes foundation models to generate synthetic samples that capture the complexity of the natural language query and represent it in the same metric space as the multi-modal data.
  Following this method, we propose Needle, a database for image data retrieval. Instead of relying on contrastive learning or metadata-searching approaches, our system is based on synthetic data generation to capture the complexities of natural language queries. Our system is open-source and ready for deployment, designed to be easily adopted by researchers and developers. The comprehensive experiments on various benchmark datasets verify that this system significantly outperforms state-of-the-art text-to-image retrieval methods in the literature. Any foundation model and embedder can be easily integrated into Needle to improve the performance, piggybacking on the advancements in these technologies.
