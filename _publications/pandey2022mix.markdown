---
layout: publication
title: 'Mix-and-match: Scalable Dialog Response Retrieval Using Gaussian Mixture Embeddings'
authors: Gaurav Pandey, Danish Contractor, Sachindra Joshi
conference: 'Findings of the Association for Computational Linguistics: EMNLP 2022'
year: 2022
bibkey: pandey2022mix
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.02710'}]
tags: [EMNLP, Evaluation, ACL]
short_authors: Gaurav Pandey, Danish Contractor, Sachindra Joshi
---
Embedding-based approaches for dialog response retrieval embed the
context-response pairs as points in the embedding space. These approaches are
scalable, but fail to account for the complex, many-to-many relationships that
exist between context-response pairs. On the other end of the spectrum, there
are approaches that feed the context-response pairs jointly through multiple
layers of neural networks. These approaches can model the complex relationships
between context-response pairs, but fail to scale when the set of responses is
moderately large (>100). In this paper, we combine the best of both worlds by
proposing a scalable model that can learn complex relationships between
context-response pairs. Specifically, the model maps the contexts as well as
responses to probability distributions over the embedding space. We train the
models by optimizing the Kullback-Leibler divergence between the distributions
induced by context-response pairs in the training data. We show that the
resultant model achieves better performance as compared to other
embedding-based approaches on publicly available conversation data.