---
layout: publication
title: A Fast Algorithm For Permutation Pattern Matching Based On Alternating Runs
authors: Marie-louise Bruner, Martin Lackner
conference: Algorithmica
year: 2015
bibkey: bruner2012fast
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1204.5224'}]
tags: ["Efficiency"]
short_authors: Marie-louise Bruner, Martin Lackner
---
The NP-complete Permutation Pattern Matching problem asks whether a
\\(k\\)-permutation \\(P\\) is contained in a \\(n\\)-permutation \\(T\\) as a pattern. This is
the case if there exists an order-preserving embedding of \\(P\\) into \\(T\\). In this
paper, we present a fixed-parameter algorithm solving this problem with a
worst-case runtime of \\(\mathcal\{O\}(1.79^\{\mathsf\{run\}(T)\}\cdot n\cdot k)\\),
where \\(\mathsf\{run\}(T)\\) denotes the number of alternating runs of \\(T\\). This
algorithm is particularly well-suited for instances where \\(T\\) has few runs,
i.e., few ups and downs. Moreover, since \\(\mathsf\{run\}(T)<n\\), this can be seen
as a \\(\mathcal\{O\}(1.79^\{n\}\cdot n\cdot k)\\) algorithm which is the first to beat
the exponential \\(2^n\\) runtime of brute-force search. Furthermore, we prove that
under standard complexity theoretic assumptions such a fixed-parameter
tractability result is not possible for \\(\mathsf\{run\}(P)\\).