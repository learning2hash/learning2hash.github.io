---
layout: publication
title: Locality-sensitive Hashing Of Curves
authors: Driemel Anne, Silvestri Francesco
conference: "Arxiv"
year: 2017
bibkey: driemel2017locality
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1703.04040"}
tags: ['ARXIV']
---
We study data structures for storing a set of polygonal curves in \{&#37; raw &#37;\}\\(\{\rm R\}^d\\)\{&#37; endraw &#37;\} such that, given a query curve, we can efficiently retrieve similar curves from the set, where similarity is measured using the discrete Fr\'echet distance or the dynamic time warping distance. To this end we devise the first locality-sensitive hashing schemes for these distance measures. A major challenge is posed by the fact that these distance measures internally optimize the alignment between the curves. We give solutions for different types of alignments including constrained and unconstrained versions. For unconstrained alignments, we improve over a result by Indyk from 2002 for short curves. Let \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} be the number of input curves and let \{&#37; raw &#37;\}\\(m\\)\{&#37; endraw &#37;\} be the maximum complexity of a curve in the input. In the particular case where $m \leq \frac\{\alpha\}\{4d\} \log n\{&#37; raw &#37;\}\\(, for some fixed \\)\{&#37; endraw &#37;\}\alpha>0$, our solutions imply an approximate near-neighbor data structure for the discrete Fr\'echet distance that uses space in \{&#37; raw &#37;\}\\(O(n^\{1+\alpha\}\log n)\\)\{&#37; endraw &#37;\} and achieves query time in \{&#37; raw &#37;\}\\(O(n^\{\alpha\}\log^2 n)\\)\{&#37; endraw &#37;\} and constant approximation factor. Furthermore, our solutions provide a trade-off between approximation quality and computational performance: for any parameter \{&#37; raw &#37;\}\\(k \in [m]\\)\{&#37; endraw &#37;\}, we can give a data structure that uses space in $O(2^\{2k\}m^\{k-1\} n \log n + nm)\{&#37; raw &#37;\}\\(, answers queries in \\)\{&#37; endraw &#37;\}O( 2^\{2k\} m^\{k\}\log n)$ time and achieves approximation factor in \{&#37; raw &#37;\}\\(O(m/k)\\)\{&#37; endraw &#37;\}.
