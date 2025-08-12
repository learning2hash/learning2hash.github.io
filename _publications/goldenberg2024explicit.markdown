---
layout: publication
title: Explicit Good Codes Approaching Distance 1 In Ulam Metric
authors: Elazar Goldenberg, Mursalin Habib, Karthik C. S
conference: IEEE Transactions on Information Theory
year: 2025
bibkey: goldenberg2024explicit
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.17235'}]
tags: ["Compact Codes", "Distance Metric Learning"]
short_authors: Elazar Goldenberg, Mursalin Habib, Karthik C. S
---
The Ulam distance of two permutations on \\([n]\\) is \\(n\\) minus the length of
their longest common subsequence. In this paper, we show that for every
\\(\epsilon>0\\), there exists some \\(\alpha>0\\), and an infinite set
\\(\Gamma\subseteq \mathbb\{N\}\\), such that for all \\(n\in\Gamma\\), there is an
explicit set \\(C_n\\) of \\((n!)^\{\alpha\}\\) many permutations on \\([n]\\), such that
every pair of permutations in \\(C_n\\) has pairwise Ulam distance at least
\\((1-\epsilon)\cdot n\\). Moreover, we can compute the \\(i^\{\text\{th\}\}\\)
permutation in \\(C_n\\) in poly\\((n)\\) time and can also decode in poly\\((n)\\) time, a
permutation \\(\pi\\) on \\([n]\\) to its closest permutation \\(\pi^*\\) in \\(C_n\\), if the
Ulam distance of \\(\pi\\) and \\(\pi^*\\) is less than \\( \frac\{(1-\epsilon)\cdot
n\}\{4\} \\).
  Previously, it was implicitly known by combining works of Goldreich and
Wigderson [Israel Journal of Mathematics'23] and Farnoud, Skachek, and
Milenkovic [IEEE Transactions on Information Theory'13] in a black-box manner,
that it is possible to explicitly construct \\((n!)^\{Ω(1)\}\\) many
permutations on \\([n]\\), such that every pair of them have pairwise Ulam distance
at least \\(\frac\{n\}\{6\}\cdot (1-\epsilon)\\), for any \\(\epsilon>0\\), and the
bound on the distance can be improved to \\(\frac\{n\}\{4\}\cdot (1-\epsilon)\\) if
the construction of Goldreich and Wigderson is directly analyzed in the Ulam
metric.