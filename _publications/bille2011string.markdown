---
layout: publication
title: String Indexing For Patterns With Wildcards
authors: "Philip Bille, Inge Li Goertz, Hjalte Wedel Vildh\xF8j, S\xF8ren Vind"
conference: Theory of Computing Systems
year: 2013
bibkey: bille2011string
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1110.5236'}]
tags: ["Efficiency"]
short_authors: Bille et al.
---
We consider the problem of indexing a string \\(t\\) of length \\(n\\) to report the
occurrences of a query pattern \\(p\\) containing \\(m\\) characters and \\(j\\) wildcards.
Let \\(occ\\) be the number of occurrences of \\(p\\) in \\(t\\), and \\(\sigma\\) the size of
the alphabet. We obtain the following results.
  - A linear space index with query time \\(O(m+\sigma^j log log n + occ)\\).
This significantly improves the previously best known linear space index by Lam
et al. [ISAAC 2007], which requires query time \\(\Theta(jn)\\) in the worst case.
  - An index with query time \\(O(m+j+occ)\\) using space \\(O(\sigma^\{k^2\} n log^k
log n)\\), where \\(k\\) is the maximum number of wildcards allowed in the pattern.
This is the first non-trivial bound with this query time.
  - A time-space trade-off, generalizing the index by Cole et al. [STOC 2004].
  We also show that these indexes can be generalized to allow variable length
gaps in the pattern. Our results are obtained using a novel combination of
well-known and new techniques, which could be of independent interest.