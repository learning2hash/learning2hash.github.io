---
layout: publication
title: Cascaded Fast And Slow Models For Efficient Semantic Code Search
authors: Akhilesh Deepak Gotmare, Junnan Li, Shafiq Joty, Steven C. H. Hoi
conference: Arxiv
year: 2021
bibkey: gotmare2021cascaded
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.07811'}]
tags: [Scalability, Hybrid ANN Methods, Re-ranking, Efficiency, Tools & Libraries,
  Evaluation]
short_authors: Gotmare et al.
---
The goal of natural language semantic code search is to retrieve a
semantically relevant code snippet from a fixed set of candidates using a
natural language query. Existing approaches are neither effective nor efficient
enough towards a practical semantic code search system. In this paper, we
propose an efficient and accurate semantic code search framework with cascaded
fast and slow models, in which a fast transformer encoder model is learned to
optimize a scalable index for fast retrieval followed by learning a slow
classification-based re-ranking model to improve the performance of the top K
results from the fast retrieval. To further reduce the high memory cost of
deploying two separate models in practice, we propose to jointly train the fast
and slow model based on a single transformer encoder with shared parameters.
The proposed cascaded approach is not only efficient and scalable, but also
achieves state-of-the-art results with an average mean reciprocal ranking (MRR)
score of 0.7795 (across 6 programming languages) as opposed to the previous
state-of-the-art result of 0.713 MRR on the CodeSearchNet benchmark.