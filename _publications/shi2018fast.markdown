---
layout: publication
title: Fast Locality Sensitive Hashing For Beam Search On GPU
authors: Shi Xing, Xu Shizhen, Knight Kevin
conference: "Arxiv"
year: 2018
bibkey: shi2018fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1806.00588"}
tags: ['ARXIV', 'Independent', 'LSH']
---
We present a GPU-based Locality Sensitive Hashing (LSH) algorithm to speed up beam search for sequence models. We utilize the winner-take-all (WTA) hash, which is based on relative ranking order of hidden dimensions and thus resilient to perturbations in numerical values. Our algorithm is designed by fully considering the underling architecture of CUDA-enabled GPUs (Algorithm/Architecture Co-design): 1) A parallel Cuckoo hash table is applied for LSH code lookup (guaranteed O(1) lookup time); 2) Candidate lists are shared across beams to maximize the parallelism; 3) Top frequent words are merged into candidate lists to improve performance. Experiments on 4 large-scale neural machine translation models demonstrate that our algorithm can achieve up to 4x speedup on softmax module, and 2x overall speedup without hurting BLEU on GPU.
