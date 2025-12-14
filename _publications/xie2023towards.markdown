---
layout: publication
title: Towards Lightweight And Automated Representation Learning System For Networks
authors: Yuyang Xie, Jiezhong Qiu, Laxman Dhulipala, Wenjian Yu, Jie Tang, Richard
  Peng, Chi Wang
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2023
bibkey: xie2023towards
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.07084'}]
tags: [Evaluation, Efficiency, Memory Efficiency, Scalability, Tools & Libraries]
short_authors: Xie et al.
---
We propose LIGHTNE 2.0, a cost-effective, scalable, automated, and
high-quality network embedding system that scales to graphs with hundreds of
billions of edges on a single machine. In contrast to the mainstream belief
that distributed architecture and GPUs are needed for large-scale network
embedding with good quality, we prove that we can achieve higher quality,
better scalability, lower cost, and faster runtime with shared-memory, CPU-only
architecture. LIGHTNE 2.0 combines two theoretically grounded embedding methods
NetSMF and ProNE. We introduce the following techniques to network embedding
for the first time: (1) a newly proposed downsampling method to reduce the
sample complexity of NetSMF while preserving its theoretical advantages; (2) a
high-performance parallel graph processing stack GBBS to achieve high memory
efficiency and scalability; (3) sparse parallel hash table to aggregate and
maintain the matrix sparsifier in memory; (4) a fast randomized singular value
decomposition (SVD) enhanced by power iteration and fast orthonormalization to
improve vanilla randomized SVD in terms of both efficiency and effectiveness;
(5) Intel MKL for proposed fast randomized SVD and spectral propagation; and
(6) a fast and lightweight AutoML library FLAML for automated hyperparameter
tuning. Experimental results show that LIGHTNE 2.0 can be up to 84X faster than
GraphVite, 30X faster than PBG and 9X faster than NetSMF while delivering
better performance. LIGHTNE 2.0 can embed very large graph with 1.7 billion
nodes and 124 billion edges in half an hour on a CPU server, while other
baselines cannot handle very large graphs of this scale.