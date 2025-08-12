---
layout: publication
title: Faster Approximate(d) Text-to-pattern L1 Distance
authors: "Przemys\u0142aw Uzna\u0144ski"
conference: Arxiv
year: 2018
bibkey: "uzna\u0144ski2018faster"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.09159'}]
tags: ["Distance Metric Learning", "Efficiency", "Hashing Methods", "Locality Sensitive Hashing", "Similarity Search"]
short_authors: "Przemys\u0142aw Uzna\u0144ski"
---
The problem of finding *distance* between *pattern* of length \(m\)
and *text* of length \(n\) is a typical way of generalizing pattern matching
to incorporate dissimilarity score. For both Hamming and \(L_1\) distances only a
super linear upper bound \(\widetilde\{O\}(n\sqrt\{m\})\) are known, which prompts
the question of relaxing the problem: either by asking for \((1 \pm
\epsilon)\) approximate distance (every distance is reported up to a
multiplicative factor), or \(k\)-approximated distance (distances exceeding \(k\)
are reported as \(\infty\)). We focus on \(L_1\) distance, for which we show new
algorithms achieving complexities respectively \(\widetilde\{O\}(\epsilon^\{-1\}
n)\) and \(\widetilde\{O\}((m+k\sqrt\{m\}) \cdot n/m)\). This is a significant
improvement upon previous algorithms with runtime
\(\widetilde\{O\}(\epsilon^\{-2\} n)\) of Lipsky and Porat [Algorithmica 2011] and
\(\widetilde\{O\}(n\sqrt\{k\})\) of Amir, Lipsky, Porat and Umanski [CPM 2005].