---
layout: publication
title: When A Dollar Makes A BWT
authors: "Sara Giuliani, Zsuzsanna Lipt\xE1k, Francesco Masillo, Romeo Rizzi"
conference: Theoretical Computer Science 857 123-146 (2021)
year: 2019
bibkey: giuliani2019when
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.09125'}]
tags: []
short_authors: Giuliani et al.
---
The Burrows-Wheeler-Transform (BWT) is a reversible string transformation
which plays a central role in text compression and is fundamental in many
modern bioinformatics applications. The BWT is a permutation of the characters,
which is in general better compressible and allows to answer several different
query types more efficiently than the original string.
  It is easy to see that not every string is a BWT image, and exact
characterizations of BWT images are known. We investigate a related
combinatorial question. In many applications, a sentinel character dollar is
added to mark the end of the string, and thus the BWT of a string ending with
dollar contains exactly one dollar-character. Given a string w, we ask in which
positions, if any, the dollar-character can be inserted to turn w into the BWT
image of a word ending with dollar. We show that this depends only on the
standard permutation of w and present a O(n log n)-time algorithm for
identifying all such positions, improving on the naive quadratic time
algorithm. We also give a combinatorial characterization of such positions and
develop bounds on their number and value. This is an extended version of
[Giuliani et al. ICTCS 2019].