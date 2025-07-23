---
layout: publication
title: Investigating The Scalability Of Approximate Sparse Retrieval Algorithms To
  Massive Datasets
authors: Bruch Sebastian, Nardini Franco Maria, Rulli Cosimo, Venturini Rossano, Venuta
  Leonardo
conference: Lecture Notes in Computer Science
year: 2025
bibkey: bruch2025investigating
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.11628'}]
tags: ["Efficiency", "Evaluation", "Graph-based ANN", "Scalability"]
short_authors: Bruch et al.
---
Learned sparse text embeddings have gained popularity due to their
effectiveness in top-k retrieval and inherent interpretability. Their
distributional idiosyncrasies, however, have long hindered their use in
real-world retrieval systems. That changed with the recent development of
approximate algorithms that leverage the distributional properties of sparse
embeddings to speed up retrieval. Nonetheless, in much of the existing
literature, evaluation has been limited to datasets with only a few million
documents such as MSMARCO. It remains unclear how these systems behave on much
larger datasets and what challenges lurk in larger scales. To bridge that gap,
we investigate the behavior of state-of-the-art retrieval algorithms on massive
datasets. We compare and contrast the recently-proposed Seismic and graph-based
solutions adapted from dense retrieval. We extensively evaluate Splade
embeddings of 138M passages from MsMarco-v2 and report indexing time and other
efficiency and effectiveness metrics.