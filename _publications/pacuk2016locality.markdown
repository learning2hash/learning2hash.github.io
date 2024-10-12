---
layout: publication
title: Locality-sensitive Hashing Without False Negatives For L_p
authors: Pacuk Andrzej, Sankowski Piotr, Wegrzycki Karol, Wygocki Piotr
conference: "Computing and Combinatorics -"
year: 2016
bibkey: pacuk2016locality
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1611.09317"}
tags: ['Independent']
---
In this paper, we show a construction of locality-sensitive hash functions without false negatives, i.e., which ensure collision for every pair of points within a given radius \{&#37; raw &#37;\}\\(R\\)\{&#37; endraw &#37;\} in \{&#37; raw &#37;\}\\(d\\)\{&#37; endraw &#37;\} dimensional space equipped with \{&#37; raw &#37;\}\\(l\_p\\)\{&#37; endraw &#37;\} norm when \{&#37; raw &#37;\}\\(p \in [1,\infty]\\)\{&#37; endraw &#37;\}. Furthermore, we show how to use these hash functions to solve the \{&#37; raw &#37;\}\\(c\\)\{&#37; endraw &#37;\}-approximate nearest neighbor search problem without false negatives. Namely, if there is a point at distance \{&#37; raw &#37;\}\\(R\\)\{&#37; endraw &#37;\}, we will certainly report it and points at distance greater than \{&#37; raw &#37;\}\\(cR\\)\{&#37; endraw &#37;\} will not be reported for \{&#37; raw &#37;\}\\(c=\Omega(\sqrt\{d\},d^\{1-\frac\{1\}\{p\}\})\\)\{&#37; endraw &#37;\}. The constructed algorithms work: - with preprocessing time \{&#37; raw &#37;\}\\(\mathcal\{O\}(n \log(n))\\)\{&#37; endraw &#37;\} and sublinear expected query time, - with preprocessing time \{&#37; raw &#37;\}\\(\mathcal\{O\}(\mathrm\{poly\}(n))\\)\{&#37; endraw &#37;\} and expected query time \{&#37; raw &#37;\}\\(\mathcal\{O\}(\log(n))\\)\{&#37; endraw &#37;\}. Our paper reports progress on answering the open problem presented by Pagh [8] who considered the nearest neighbor search without false negatives for the Hamming distance.
