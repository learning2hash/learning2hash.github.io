---
layout: publication
title: The Fast Johnson-lindenstrauss Transform Is Even Faster
authors: "Ora Nova Fandina, Mikael M\xF8ller H\xF8gsgaard, Kasper Green Larsen"
conference: Arxiv
year: 2022
bibkey: fandina2022fast
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.01800'}]
tags: ["Efficiency", "Hashing Methods", "Scalability"]
short_authors: "Ora Nova Fandina, Mikael M\xF8ller H\xF8gsgaard, Kasper Green Larsen"
---
The seminal Fast Johnson-Lindenstrauss (Fast JL) transform by Ailon and
Chazelle (SICOMP'09) embeds a set of \(n\) points in \(d\)-dimensional Euclidean
space into optimal \(k=O(\epsilon^\{-2\} \ln n)\) dimensions, while preserving
all pairwise distances to within a factor \((1 \pm \epsilon)\). The Fast JL
transform supports computing the embedding of a data point in \(O(d \ln d +k
\ln^2 n)\) time, where the \(d \ln d\) term comes from multiplication with a \(d
\times d\) Hadamard matrix and the \(k \ln^2 n\) term comes from multiplication
with a sparse \(k \times d\) matrix. Despite the Fast JL transform being more
than a decade old, it is one of the fastest dimensionality reduction techniques
for many tradeoffs between \(\epsilon, d\) and \(n\).
  In this work, we give a surprising new analysis of the Fast JL transform,
showing that the \(k \ln^2 n\) term in the embedding time can be improved to \((k
\ln^2 n)/\alpha\) for an \(\alpha =
Ω(\min\\{\epsilon^\{-1\}\ln(1/\epsilon), \ln n\\})\). The improvement
follows by using an even sparser matrix. We also complement our improved
analysis with a lower bound showing that our new analysis is in fact tight.