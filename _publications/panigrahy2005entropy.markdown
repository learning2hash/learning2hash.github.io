---
layout: publication
title: Entropy Based Nearest Neighbor Search In High Dimensions
authors: Panigrahy Rina
conference: "Arxiv"
year: 2005
bibkey: panigrahy2005entropy
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/cs/0510019"}
tags: ['ARXIV', 'Independent']
---
In this paper we study the problem of finding the approximate nearest
neighbor of a query point in the high dimensional space, focusing on the
Euclidean space. The earlier approaches use locality-preserving hash functions
(that tend to map nearby points to the same value) to construct several hash
tables to ensure that the query point hashes to the same bucket as its nearest
neighbor in at least one table. Our approach is different -- we use one (or a
few) hash table and hash several randomly chosen points in the neighborhood of
the query point showing that at least one of them will hash to the bucket
containing its nearest neighbor. We show that the number of randomly chosen
points in the neighborhood of the query point \\{q\\} required depends on the
entropy of the hash value \\{h(p)\\} of a random point \\{p\\} at the same distance
from \\{q\\} at its nearest neighbor, given \\{q\\} and the locality preserving hash
function \\{h\\} chosen randomly from the hash family. Precisely, we show that if
the entropy \\{I(h(p)|q,h) = M\\} and \\{g\\} is a bound on the probability that two
far-off points will hash to the same bucket, then we can find the approximate
nearest neighbor in \\{O(n^\rho)\\} time and near linear \\{\tilde O(n)\\} space where
\\{\rho = M/log(1/g)\\}. Alternatively we can build a data structure of size
\\{\tilde O(n^{1/(1-\rho)})\\} to answer queries in \\{\tilde O(d)\\} time. By applying
this analysis to the locality preserving hash functions in and adjusting the
parameters we show that the \\{c\\} nearest neighbor can be computed in time
\\{\tilde O(n^\rho)\\} and near linear space where \\{\rho \approx 2.06/c\\} as \\{c\\}
becomes large.
