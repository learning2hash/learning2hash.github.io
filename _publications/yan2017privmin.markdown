---
layout: publication
title: 'Privmin: Differentially Private Minhash For Jaccard Similarity Computation'
authors: Ziqi Yan, Jiqiang Liu, Gang Li, Zhen Han, Shuo Qiu
conference: Arxiv
year: 2017
bibkey: yan2017privmin
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.07258'}]
tags: ["Datasets", "Locality-Sensitive-Hashing", "Privacy & Security"]
short_authors: Yan et al.
---
In many industrial applications of big data, the Jaccard Similarity
Computation has been widely used to measure the distance between two profiles
or sets respectively owned by two users. Yet, one semi-honest user with
unpredictable knowledge may also deduce the private or sensitive information
(e.g., the existence of a single element in the original sets) of the other
user via the shared similarity. In this paper, we aim at solving the privacy
issues in Jaccard similarity computation with strict differential privacy
guarantees. To achieve this, we first define the Conditional \(\epsilon\)-DPSO, a
relaxed differential privacy definition regarding set operations, and prove
that the MinHash-based Jaccard Similarity Computation (MH-JSC) satisfies this
definition. Then for achieving strict differential privacy in MH-JSC, we
propose the PrivMin algorithm, which consists of two private operations: 1) the
Private MinHash Value Generation that works by introducing the Exponential
noise to the generation of MinHash signature. 2) the Randomized MinHashing
Steps Selection that works by adopting Randomized Response technique to
privately select several steps within the MinHashing phase that are deployed
with the Exponential mechanism. Experiments on real datasets demonstrate that
the proposed PrivMin algorithm can successfully retain the utility of the
computed similarity while preserving privacy.