---
layout: publication
title: Vectorized And Performance-portable Quicksort
authors: Mark Blacher, Joachim Giesen, Peter Sanders, Jan Wassenberg
conference: 'Software: Practice and Experience'
year: 2022
bibkey: blacher2022vectorized
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.05982'}]
tags: ["Efficiency"]
short_authors: Blacher et al.
---
Recent works showed that implementations of Quicksort using vector CPU
instructions can outperform the non-vectorized algorithms in widespread use.
However, these implementations are typically single-threaded, implemented for a
particular instruction set, and restricted to a small set of key types. We lift
these three restrictions: our proposed 'vqsort' algorithm integrates into the
state-of-the-art parallel sorter 'ips4o', with a geometric mean speedup of
1.59. The same implementation works on seven instruction sets (including SVE
and RISC-V V) across four platforms. It also supports floating-point and 16-128
bit integer keys. To the best of our knowledge, this is the fastest sort for
non-tuple keys on CPUs, up to 20 times as fast as the sorting algorithms
implemented in standard libraries. This paper focuses on the practical
engineering aspects enabling the speed and portability, which we have not yet
seen demonstrated for a Quicksort implementation. Furthermore, we introduce
compact and transpose-free sorting networks for in-register sorting of small
arrays, and a vector-friendly pivot sampling strategy that is robust against
adversarial input.