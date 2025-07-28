---
layout: publication
title: 'Falconn++: A Locality-sensitive Filtering Approach For Approximate Nearest
  Neighbor Search'
authors: Ninh Pham, Tao Liu
conference: Arxiv
year: 2022
bibkey: pham2022falconn
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.01382'}]
tags: ["Efficiency", "Hashing Methods"]
short_authors: Ninh Pham, Tao Liu
---
We present Falconn++, a novel locality-sensitive filtering approach for
approximate nearest neighbor search on angular distance. Falconn++ can filter
out potential far away points in any hash bucket \textit\{before\} querying,
which results in higher quality candidates compared to other hashing-based
solutions. Theoretically, Falconn++ asymptotically achieves lower query time
complexity than Falconn, an optimal locality-sensitive hashing scheme on
angular distance. Empirically, Falconn++ achieves higher recall-speed tradeoffs
than Falconn on many real-world data sets. Falconn++ is also competitive with
HNSW, an efficient representative of graph-based solutions on high search
recall regimes.