---
layout: publication
title: On Top-\(k\) Weighted SUM Aggregate Nearest And Farthest Neighbors In The \(L_1\)
  Plane
authors: Haitao Wang, Wuzhou Zhang
conference: Arxiv
year: 2012
bibkey: wang2012top
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1211.5084'}]
tags: ["Efficiency"]
short_authors: Haitao Wang, Wuzhou Zhang
---
In this paper, we study top-\\(k\\) aggregate (or group) nearest neighbor queries
using the weighted SUM operator under the \\(L_1\\) metric in the plane. Given a
set \\(P\\) of \\(n\\) points, for any query consisting of a set \\(Q\\) of \\(m\\) weighted
points and an integer \\(k\\), \\( 1 \le k \le n\\), the top-\\(k\\) aggregate nearest
neighbor query asks for the \\(k\\) points of \\(P\\) whose aggregate distances to \\(Q\\)
are the smallest, where the aggregate distance of each point \\(p\\) of \\(P\\) to \\(Q\\)
is the sum of the weighted distances from \\(p\\) to all points of \\(Q\\). We build an
\\(O(nlog nloglog n)\\)-size data structure in \\(O(nlog n loglog n)\\) time,
such that each top-\\(k\\) query can be answered in \\(O(mlog m+(k+m)log^2 n)\\)
time. We also obtain other results with trade-off between preprocessing and
query. Even for the special case where \\(k=1\\), our results are better than the
previously best method (in PODS 2012), which requires \\(O(nlog^2 n)\\)
preprocessing time, \\(O(nlog^2 n)\\) space, and \\(O(m^2log^3 n)\\) query time. In
addition, for the one-dimensional version of this problem, our approach can
build an \\(O(n)\\)-size data structure in \\(O(nlog n)\\) time that can support
\\(O(\min\\{k,log m\\}\cdot m+k+log n)\\) time queries. Further, we extend our
techniques to the top-\\(k\\) aggregate farthest neighbor queries, with the same
bounds.