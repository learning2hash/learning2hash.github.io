---
layout: publication
title: Local Decodability Of The Burrows-wheeler Transform
authors: Sandip Sinha, Omri Weinstein
conference: Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing
year: 2019
bibkey: sinha2018local
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.03978'}]
tags: []
short_authors: Sandip Sinha, Omri Weinstein
---
The Burrows-Wheeler Transform (BWT) is among the most influential discoveries
in text compression and DNA storage. It is a reversible preprocessing step that
rearranges an \\(n\\)-letter string into runs of identical characters (by
exploiting context regularities), resulting in highly compressible strings, and
is the basis of the \texttt\{bzip\} compression program. Alas, the decoding
process of BWT is inherently sequential and requires \\(Ω(n)\\) time even to
retrieve a *single* character.
  We study the succinct data structure problem of locally decoding short
substrings of a given text under its *compressed* BWT, i.e., with small
additive redundancy \\(r\\) over the *Move-To-Front* (\texttt\{bzip\})
compression. The celebrated BWT-based FM-index (FOCS '00), as well as other
related literature, yield a trade-off of \\(r=\tilde\{O\}(n/\sqrt\{t\})\\) bits, when a
single character is to be decoded in \\(O(t)\\) time. We give a near-quadratic
improvement \\(r=\tilde\{O\}(n\lg(t)/t)\\). As a by-product, we obtain an
*exponential* (in \\(t\\)) improvement on the redundancy of the FM-index for
counting pattern-matches on compressed text. In the interesting regime where
the text compresses to \\(n^\{1-o(1)\}\\) bits, these results provide an \\(\exp(t)\\)
*overall* space reduction. For the local decoding problem of BWT, we also
prove an \\(Ω(n/t^2)\\) cell-probe lower bound for "symmetric" data
structures.
  We achieve our main result by designing a compressed partial-sums (Rank) data
structure over BWT. The key component is a *locally-decodable*
Move-to-Front (MTF) code: with only \\(O(1)\\) extra bits per block of length
\\(n^\{Ω(1)\}\\), the decoding time of a single character can be decreased from
\\(Ω(n)\\) to \\(O(\lg n)\\). This result is of independent interest in
algorithmic information theory.