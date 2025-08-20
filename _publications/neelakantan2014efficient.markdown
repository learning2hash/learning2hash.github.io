---
layout: publication
title: Efficient Non-parametric Estimation Of Multiple Embeddings Per Word In Vector
  Space
authors: Arvind Neelakantan, Jeevan Shankar, Alexandre Passos, Andrew McCallum
conference: Proceedings of the 2014 Conference on Empirical Methods in Natural Language
  Processing (EMNLP)
year: 2014
bibkey: neelakantan2014efficient
citations: 485
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1504.06654'}]
tags: [Efficiency, EMNLP, Scalability]
short_authors: Neelakantan et al.
---
There is rising interest in vector-space word embeddings and their use in
NLP, especially given recent methods for their fast estimation at very large
scale. Nearly all this work, however, assumes a single vector per word type
ignoring polysemy and thus jeopardizing their usefulness for downstream tasks.
We present an extension to the Skip-gram model that efficiently learns multiple
embeddings per word type. It differs from recent related work by jointly
performing word sense discrimination and embedding learning, by
non-parametrically estimating the number of senses per word type, and by its
efficiency and scalability. We present new state-of-the-art results in the word
similarity in context task and demonstrate its scalability by training with one
machine on a corpus of nearly 1 billion tokens in less than 6 hours.