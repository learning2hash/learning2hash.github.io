---
layout: publication
title: Simplified Tight Bounds For Monotone Minimal Perfect Hashing
authors: Dmitry Kosolobov
conference: Arxiv
year: 2024
bibkey: kosolobov2024simplified
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.07760'}]
tags: ["Hashing Methods"]
short_authors: Dmitry Kosolobov
---
Given an increasing sequence of integers \(x_1,\ldots,x_n\) from a universe
\(\\{0,\ldots,u-1\\}\), the monotone minimal perfect hash function (MMPHF) for this
sequence is a data structure that answers the following rank queries: \(rank(x)
= i\) if \(x = x_i\), for \(i\in \\{1,\ldots,n\\}\), and \(rank(x)\) is arbitrary
otherwise. Assadi, Farach-Colton, and Kuszmaul recently presented at SODA'23 a
proof of the lower bound \(Ω(n \min\\{logloglog u, log n\\})\) for the
bits of space required by MMPHF, provided \(u \ge n 2^\{2^\{\sqrt\{loglog n\}\}\}\),
which is tight since there is a data structure for MMPHF that attains this
space bound (and answers the queries in \(O(log u)\) time). In this paper, we
close the remaining gap by proving that, for \(u \ge (1+\epsilon)n\), where
\(\epsilon > 0\) is any constant, the tight lower bound is \(Ω(n
\min\\{logloglog \frac\{u\}\{n\}, log n\\})\), which is also attainable; we
observe that, for all reasonable cases when \(n < u < (1+\epsilon)n\), known
facts imply tight bounds, which virtually settles the problem. Along the way we
substantially simplify the proof of Assadi et al. replacing a part of their
heavy combinatorial machinery by trivial observations. However, an important
part of the proof still remains complicated. This part of our paper repeats
arguments of Assadi et al. and is not novel. Nevertheless, we include it, for
completeness, offering a somewhat different perspective on these arguments.