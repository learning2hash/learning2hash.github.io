---
layout: publication
title: Diversity-aware \(k\)-maximum Inner Product Search Revisited
authors: Qiang Huang, Yanhao Wang, Yiqun Sun, Anthony K. H. Tung
conference: Arxiv
year: 2024
bibkey: huang2024diversity
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.13858'}]
tags: [Similarity Search, Recommender Systems, Efficiency]
short_authors: Huang et al.
---
The \(k\)-Maximum Inner Product Search (\(k\)MIPS) serves as a foundational
component in recommender systems and various data mining tasks. However, while
most existing \(k\)MIPS approaches prioritize the efficient retrieval of highly
relevant items for users, they often neglect an equally pivotal facet of search
results: *diversity*. To bridge this gap, we revisit and refine the
diversity-aware \(k\)MIPS (D\(k\)MIPS) problem by incorporating two well-known
diversity objectives -- minimizing the average and maximum pairwise item
similarities within the results -- into the original relevance objective. This
enhancement, inspired by Maximal Marginal Relevance (MMR), offers users a
controllable trade-off between relevance and diversity. We introduce
\textsc\{Greedy\} and \textsc\{DualGreedy\}, two linear scan-based algorithms
tailored for D\(k\)MIPS. They both achieve data-dependent approximations and,
when aiming to minimize the average pairwise similarity, \textsc\{DualGreedy\}
attains an approximation ratio of \(1/4\) with an additive term for
regularization. To further improve query efficiency, we integrate a lightweight
Ball-Cone Tree (BC-Tree) index with the two algorithms. Finally, comprehensive
experiments on ten real-world data sets demonstrate the efficacy of our
proposed methods, showcasing their capability to efficiently deliver diverse
and relevant search results to users.