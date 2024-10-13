---
layout: publication
title: Falconn++ A Locality-sensitive Filtering Approach For Approximate Nearest Neighbor Search
authors: Ninh Pham, Tao Liu
conference: "Neural Information Processing Systems"
year: 2022
bibkey: pham2022locality
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper_files/paper/2022/hash/ca2963d1cfb25e93362e86fb427a9524-Abstract-Conference.html"}
tags: ['Graph', 'NEURIPS']
---
<p>We present Falconn++, a novel locality-sensitive filtering (LSF)
approach for approximate nearest neighbor search on angular distance.
Falconn++ can filter out potential far away points in any hash bucket
before querying, which results in higher quality candidates compared to
other hashing-based solutions. Theoretically, Falconn++ asymptotically
achieves lower query time complexity than Falconn, an optimal
locality-sensitive hashing scheme on angular distance. Empirically,
Falconn++ achieves a higher recall-speed tradeoff than Falconn on many
real-world data sets. Falconn++ is also competitive with HNSW, an
efficient representative of graph-based solutions on high search recall
regimes.</p>
