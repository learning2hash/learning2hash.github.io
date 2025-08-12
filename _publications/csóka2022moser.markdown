---
layout: publication
title: Moser-tardos Algorithm With Small Number Of Random Bits
authors: "Endre Cs\xF3ka, \u0141ukasz Grabowski, Andr\xE1s M\xE1th\xE9, Oleg Pikhurko,\
  \ Konstantinos Tyros"
conference: Arxiv
year: 2022
bibkey: "cs\xF3ka2022moser"
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.05888'}]
tags: ["Efficiency"]
short_authors: "Cs\xF3ka et al."
---
We study a variant of the parallel Moser-Tardos Algorithm. We prove that if
we restrict attention to a class of problems whose dependency graphs have
subexponential growth, then the expected total number of random bits used by
the algorithm is constant; in particular, it is independent from the number of
variables. This is achieved by using the same random bits to resample variables
which are far enough in the dependency graph.
  There are two corollaries. First, we obtain a deterministic algorithm for
finding a satisfying assignment, which for any class of problems as in the
previous paragraph runs in time O(n), where n is the number of variables.
Second, we present a Borel version of the Lov\'asz Local Lemma.