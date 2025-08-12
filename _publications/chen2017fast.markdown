---
layout: publication
title: Fast Computation Of Graph Edit Distance
authors: Xiaoyang Chen, Hongwei Huo, Jun Huan, Jeffrey Scott Vitter
conference: Arxiv
year: 2017
bibkey: chen2017fast
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.10305'}]
tags: ["Efficiency", "Similarity Search"]
short_authors: Chen et al.
---
The graph edit distance (GED) is a well-established distance measure widely
used in many applications. However, existing methods for the GED computation
suffer from several drawbacks including oversized search space, huge memory
consumption, and lots of expensive backtracking. In this paper, we present
BSS_GED, a novel vertex-based mapping method for the GED computation. First, we
create a small search space by reducing the number of invalid and redundant
mappings involved in the GED computation. Then, we utilize beam-stack search
combined with two heuristics to efficiently compute GED, achieving a flexible
trade-off between available memory and expensive backtracking. Extensive
experiments demonstrate that BSS GED is highly efficient for the GED
computation on sparse as well as dense graphs and outperforms the
state-of-the-art GED methods. In addition, we also apply BSS_GED to the graph
similarity search problem and the practical results confirm its efficiency.