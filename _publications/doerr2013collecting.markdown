---
layout: publication
title: Collecting Coupons With Random Initial Stake
authors: Benjamin Doerr, Carola Doerr
conference: Algorithmica 75 (2016) 529-553
year: 2013
bibkey: doerr2013collecting
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1308.6384'}]
tags: []
short_authors: Benjamin Doerr, Carola Doerr
---
Motivated by a problem in the theory of randomized search heuristics, we give
a very precise analysis for the coupon collector problem where the collector
starts with a random set of coupons (chosen uniformly from all sets).
  We show that the expected number of rounds until we have a coupon of each
type is \(nH_\{n/2\} - 1/2 \pm o(1)\), where \(H_\{n/2\}\) denotes the \((n/2)\)th
harmonic number when \(n\) is even, and \(H_\{n/2\}:= (1/2) H_\{\lfloor n/2 \rfloor\}
+ (1/2) H_\{\lceil n/2 \rceil\}\) when \(n\) is odd. Consequently, the coupon
collector with random initial stake is by half a round faster than the one
starting with exactly \(n/2\) coupons (apart from additive \(o(1)\) terms).
  This result implies that classic simple heuristic called *randomized
local search* needs an expected number of \(nH_\{n/2\} - 1/2 \pm o(1)\) iterations
to find the optimum of any monotonic function defined on bit-strings of length
\(n\).