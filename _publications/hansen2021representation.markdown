---
layout: publication
title: Representation Learning for Efficient and Effective Similarity Search and Recommendation
authors: Hansen Casper
conference: Proceedings of the 46th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2021
bibkey: hansen2021representation
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.01815'}]
tags: ["Similarity-Search", "Recommender-Systems", "SIGIR"]
---
How data is represented and operationalized is critical for building
computational solutions that are both effective and efficient. A common
approach is to represent data objects as binary vectors, denoted \textit\{hash
codes\}, which require little storage and enable efficient similarity search
through direct indexing into a hash table or through similarity computations in
an appropriate space. Due to the limited expressibility of hash codes, compared
to real-valued representations, a core open challenge is how to generate hash
codes that well capture semantic content or latent properties using a small
number of bits, while ensuring that the hash codes are distributed in a way
that does not reduce their search efficiency. State of the art methods use
representation learning for generating such hash codes, focusing on neural
autoencoder architectures where semantics are encoded into the hash codes by
learning to reconstruct the original inputs of the hash codes. This thesis
addresses the above challenge and makes a number of contributions to
representation learning that (i) improve effectiveness of hash codes through
more expressive representations and a more effective similarity measure than
the current state of the art, namely the Hamming distance, and (ii) improve
efficiency of hash codes by learning representations that are especially suited
to the choice of search method. The contributions are empirically validated on
several tasks related to similarity search and recommendation.