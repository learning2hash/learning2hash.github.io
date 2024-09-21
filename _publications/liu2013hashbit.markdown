---
layout: "publication"
title: "Hash Bit Selection: a Unified Solution for Selection Problems in Hashing"
authors: X. Liu, J. He, B. Lang, S. Chang
conference: CVPR
year: 2013
bibkey: liu2013hashbit
additional_links:
   - {name: "PDF", url: "https://research.fb.com/wp-content/uploads/2016/11/hash-bit-selection-a-unified-solution-for-selection-problems-in-hashing.pdf?"}
---
Hashing based methods recently have been shown promising for large-scale nearest neighbor search. However, good designs involve difficult decisions of many unknowns – data features, hashing algorithms, parameter settings, kernels, etc. In this paper, we provide a unified solution as hash bit selection, i.e., selecting the most informative hash bits from a pool of candidates that may have been generated under various conditions mentioned above. We represent the candidate bit pool as a vertex- and edge-weighted graph with the pooled bits as vertices. Then we formulate the bit selection problem as quadratic programming over the graph, and solve it efficiently by replicator dynamics. Extensive experiments show that our bit selection approach can achieve superior performance over both naive selection methods and state-of-the-art methods under each scenario, usually with significant accuracy gains from 10% to 50% relatively.

