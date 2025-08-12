---
layout: publication
title: Gapped Indexing For Consecutive Occurrences
authors: "Philip Bille, Inge Li G\xF8rtz, Max Rish\xF8j Pedersen, Teresa Anna Steiner"
conference: Algorithmica
year: 2022
bibkey: bille2021gapped
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.02505'}]
tags: ["Efficiency"]
short_authors: Bille et al.
---
The classic string indexing problem is to preprocess a string S into a
compact data structure that supports efficient pattern matching queries.
Typical queries include existential queries (decide if the pattern occurs in
S), reporting queries (return all positions where the pattern occurs), and
counting queries (return the number of occurrences of the pattern). In this
paper we consider a variant of string indexing, where the goal is to compactly
represent the string such that given two patterns P1 and P2 and a gap range
[\alpha,\beta] we can quickly find the consecutive occurrences of P1 and P2
with distance in [\alpha,\beta], i.e., pairs of occurrences immediately
following each other and with distance within the range. We present data
structures that use \~O(n) space and query time \~O(|P1|+|P2|+n^(2/3)) for
existence and counting and \~O(|P1|+|P2|+n^(2/3)*occ^(1/3)) for reporting. We
complement this with a conditional lower bound based on the set intersection
problem showing that any solution using \~O(n) space must use
\tilde\{Ω\}\}(|P1|+|P2|+\sqrt\{n\}) query time. To obtain our results we
develop new techniques and ideas of independent interest including a new suffix
tree decomposition and hardness of a variant of the set intersection problem.