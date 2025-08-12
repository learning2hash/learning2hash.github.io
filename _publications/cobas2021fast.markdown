---
layout: publication
title: A Fast And Small Subsampled R-index
authors: Dustin Cobas, Travis Gagie, Gonzalo Navarro
conference: Arxiv
year: 2021
bibkey: cobas2021fast
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.15329'}]
tags: []
short_authors: Dustin Cobas, Travis Gagie, Gonzalo Navarro
---
The \(r\)-index (Gagie et al., JACM 2020) represented a breakthrough in
compressed indexing of repetitive text collections, outperforming its
alternatives by orders of magnitude. Its space usage, \(\mathcal\{O\}(r)\) where
\(r\) is the number of runs in the Burrows-Wheeler Transform of the text, is
however larger than Lempel-Ziv and grammar-based indexes, and makes it
uninteresting in various real-life scenarios of milder repetitiveness. In this
paper we introduce the \(sr\)-index, a variant that limits the space to
\(\mathcal\{O\}(\min(r,n/s))\) for a text of length \(n\) and a given parameter \(s\),
at the expense of multiplying by \(s\) the time per occurrence reported. The
\(sr\)-index is obtained by carefully subsampling the text positions indexed by
the \(r\)-index, in a way that we prove is still able to support pattern matching
with guaranteed performance. Our experiments demonstrate that the \(sr\)-index
sharply outperforms virtually every other compressed index on repetitive texts,
both in time and space, even matching the performance of the \(r\)-index while
using 1.5--3.0 times less space. Only some Lempel-Ziv-based indexes achieve
better compression than the \(sr\)-index, using about half the space, but they
are an order of magnitude slower.