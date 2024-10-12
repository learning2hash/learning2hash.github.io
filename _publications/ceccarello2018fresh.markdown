---
layout: publication
title: FRESH Frechet Similarity With Hashing
authors: Ceccarello Matteo, Driemel Anne, Silvestri Francesco
conference: "Proc. of Algorithms and Data Structures Symposium"
year: 2018
bibkey: ceccarello2018fresh
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1809.02350"}
tags: ['Independent']
---
This paper studies the \{&#37; raw &#37;\}\\(r\\)\{&#37; endraw &#37;\}-range search problem for curves under the continuous Fr\'echet distance: given a dataset \{&#37; raw &#37;\}\\(S\\)\{&#37; endraw &#37;\} of \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} polygonal curves and a threshold \{&#37; raw &#37;\}\\(r>0\\)\{&#37; endraw &#37;\}, construct a data structure that, for any query curve \{&#37; raw &#37;\}\\(q\\)\{&#37; endraw &#37;\}, efficiently returns all entries in \{&#37; raw &#37;\}\\(S\\)\{&#37; endraw &#37;\} with distance at most \{&#37; raw &#37;\}\\(r\\)\{&#37; endraw &#37;\} from \{&#37; raw &#37;\}\\(q\\)\{&#37; endraw &#37;\}. We propose FRESH, an approximate and randomized approach for \{&#37; raw &#37;\}\\(r\\)\{&#37; endraw &#37;\}-range search, that leverages on a locality sensitive hashing scheme for detecting candidate near neighbors of the query curve, and on a subsequent pruning step based on a cascade of curve simplifications. We experimentally compare \fresh to exact and deterministic solutions, and we show that high performance can be reached by suitably relaxing precision and recall.
