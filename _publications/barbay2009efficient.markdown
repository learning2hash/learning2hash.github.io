---
layout: publication
title: Efficient Fully-compressed Sequence Representations
authors: Jeremy Barbay, Francisco Claude, Travis Gagie, Gonzalo Navarro, Yakov Nekrich
conference: Algorithmica
year: 2012
bibkey: barbay2009efficient
citations: 52
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/0911.4981'}]
tags: ["Compact Codes"]
short_authors: Barbay et al.
---
We present a data structure that stores a sequence \\(s[1..n]\\) over alphabet
\\([1..\sigma]\\) in \\(n\Ho(s) + o(n)(\Ho(s)\{+\}1)\\) bits, where \\(\Ho(s)\\) is the
zero-order entropy of \\(s\\). This structure supports the queries \access, \rank\
and \select, which are fundamental building blocks for many other compressed
data structures, in worst-case time \\(\Oh\{\lg\lg\sigma\}\\) and average time
\\(\Oh\{\lg \Ho(s)\}\\). The worst-case complexity matches the best previous results,
yet these had been achieved with data structures using \\(n\Ho(s)+o(n\lg\sigma)\\)
bits. On highly compressible sequences the \\(o(n\lg\sigma)\\) bits of the
redundancy may be significant compared to the the \\(n\Ho(s)\\) bits that encode
the data. Our representation, instead, compresses the redundancy as well.
Moreover, our average-case complexity is unprecedented. Our technique is based
on partitioning the alphabet into characters of similar frequency. The
subsequence corresponding to each group can then be encoded using fast
uncompressed representations without harming the overall compression ratios,
even in the redundancy. The result also improves upon the best current
compressed representations of several other data structures. For example, we
achieve \\((i)\\) compressed redundancy, retaining the best time complexities, for
the smallest existing full-text self-indexes; \\((ii)\\) compressed permutations
\\(\pi\\) with times for \\(\pi()\\) and \\(\pii()\\) improved to loglogarithmic; and
\\((iii)\\) the first compressed representation of dynamic collections of disjoint
sets. We also point out various applications to inverted indexes, suffix
arrays, binary relations, and data compressors. ...