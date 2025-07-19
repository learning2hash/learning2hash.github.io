---
layout: publication
title: Scalable K-means Clustering For Large K Via Seeded Approximate Nearest-neighbor
  Search
authors: Spalding-jamieson Jack, Robson Eliot Wong, Zheng da Wei
conference: IEEE Transactions on Image Processing
year: 2025
bibkey: spaldingjamieson2025scalable
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.06163'}]
tags: [Similarity Search]
---
For very large values of \\(k\\), we consider methods for fast \\(k\\)-means
clustering of massive datasets with \\(10^7\sim10^9\\) points in high-dimensions
(\\(d\geq100\\)). All current practical methods for this problem have runtimes at
least \\(Ω(k^2)\\). We find that initialization routines are not a bottleneck
for this case. Instead, it is critical to improve the speed of Lloyd's
local-search algorithm, particularly the step that reassigns points to their
closest center. Attempting to improve this step naturally leads us to leverage
approximate nearest-neighbor search methods, although this alone is not enough
to be practical. Instead, we propose a family of problems we call "Seeded
Approximate Nearest-Neighbor Search", for which we propose "Seeded
Search-Graph" methods as a solution.