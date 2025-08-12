---
layout: publication
title: Towards An Optimal Space-and-query-time Index For Top-k Document Retrieval
authors: Wing-kai Hon, Rahul Shah, Sharma V. Thankachan
conference: Lecture Notes in Computer Science
year: 2012
bibkey: hon2011towards
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1108.0554'}]
tags: ["Efficiency"]
short_authors: Wing-kai Hon, Rahul Shah, Sharma V. Thankachan
---
Let \\(\D = \\)\\( \\{d_1,d_2,...d_D\\}\\) be a given set of \\(D\\) string documents of
total length \\(n\\), our task is to index \\(\D\\), such that the \\(k\\) most relevant
documents for an online query pattern \\(P\\) of length \\(p\\) can be retrieved
efficiently. We propose an index of size \\(|CSA|+nlog D(2+o(1))\\) bits and
\\(O(t_\{s\}(p)+kloglog n+polyloglog n)\\) query time for the basic relevance
metric *term-frequency*, where \\(|CSA|\\) is the size (in bits) of a
compressed full text index of \\(\D\\), with \\(O(t_s(p))\\) time for searching a
pattern of length \\(p\\) . We further reduce the space to \\(|CSA|+nlog D(1+o(1))\\)
bits, however the query time will be \\(O(t_s(p)+k(log \sigma loglog
n)^\{1+\epsilon\}+polyloglog n)\\), where \\(\sigma\\) is the alphabet size and
\\(\epsilon >0\\) is any constant.