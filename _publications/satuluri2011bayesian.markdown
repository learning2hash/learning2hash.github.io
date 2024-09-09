---
    layout: publication
    title: "Bayesian Locality Sensitive Hashing for Fast Similarity Search"
    authors: Satuluri Venu, Parthasarathy Srinivasan
    conference: PVLDB
    year: 2011
    bibkey: satuluri2011bayesian
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/1110.1328"}
    tags: ['LSH']
    ---
    Given a collection of objects and an associated similarity measure, the all-pairs similarity search problem asks us to find all pairs of objects with similarity greater than a certain user-specified threshold. Locality-sensitive hashing (LSH) based methods have become a very popular approach for this problem. However, most such methods only use LSH for the first phase of similarity search - i.e. efficient indexing for candidate generation. In this paper, we present BayesLSH, a principled Bayesian algorithm for the subsequent phase of similarity search - performing candidate pruning and similarity estimation using LSH. A simpler variant, BayesLSH-Lite, which calculates similarities exactly, is also presented. BayesLSH is able to quickly prune away a large majority of the false positive candidate pairs, leading to significant speedups over baseline approaches. For BayesLSH, we also provide probabilistic guarantees on the quality of the output, both in terms of accuracy and recall. Finally, the quality of BayesLSH's output can be easily tuned and does not require any manual setting of the number of hashes to use for similarity estimation, unlike standard approaches. For two state-of-the-art candidate generation algorithms, AllPairs and LSH, BayesLSH enables significant speedups, typically in the range 2x-20x for a wide variety of datasets.