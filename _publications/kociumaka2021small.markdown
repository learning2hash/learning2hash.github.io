---
layout: publication
title: Small Space And Streaming Pattern Matching With K Edits
authors: Tomasz Kociumaka, Ely Porat, Tatiana Starikovskaya
conference: 2021 IEEE 62nd Annual Symposium on Foundations of Computer Science (FOCS)
year: 2022
bibkey: kociumaka2021small
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.06037'}]
tags: []
short_authors: Tomasz Kociumaka, Ely Porat, Tatiana Starikovskaya
---
In this work, we revisit the fundamental and well-studied problem of
approximate pattern matching under edit distance. Given an integer \\(k\\), a
pattern \\(P\\) of length \\(m\\), and a text \\(T\\) of length \\(n \ge m\\), the task is to
find substrings of \\(T\\) that are within edit distance \\(k\\) from \\(P\\). Our main
result is a streaming algorithm that solves the problem in \\(\tilde\{O\}(k^5)\\)
space and \\(\tilde\{O\}(k^8)\\) amortised time per character of the text, providing
answers correct with high probability. (Hereafter, \\(\tilde\{O\}(\cdot)\\) hides a
\\(\mathrm\{poly\}(log n)\\) factor.) This answers a decade-old question: since the
discovery of a \\(\mathrm\{poly\}(klog n)\\)-space streaming algorithm for pattern
matching under Hamming distance by Porat and Porat [FOCS 2009], the existence
of an analogous result for edit distance remained open. Up to this work, no
\\(\mathrm\{poly\}(klog n)\\)-space algorithm was known even in the simpler
semi-streaming model, where \\(T\\) comes as a stream but \\(P\\) is available for
read-only access. In this model, we give a deterministic algorithm that
achieves slightly better complexity.
  In order to develop the fully streaming algorithm, we introduce a new edit
distance sketch parametrised by integers \\(n\ge k\\). For any string of length at
most \\(n\\), the sketch is of size \\(\tilde\{O\}(k^2)\\) and it can be computed with an
\\(\tilde\{O\}(k^2)\\)-space streaming algorithm. Given the sketches of two strings,
in \\(\tilde\{O\}(k^3)\\) time we can compute their edit distance or certify that it
is larger than \\(k\\). This result improves upon \\(\tilde\{O\}(k^8)\\)-size sketches of
Belazzougui and Zhu [FOCS 2016] and very recent \\(\tilde\{O\}(k^3)\\)-size sketches
of Jin, Nelson, and Wu [STACS 2021].