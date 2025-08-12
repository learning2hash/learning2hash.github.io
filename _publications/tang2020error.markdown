---
layout: publication
title: Error-correcting Codes For Noisy Duplication Channels
authors: Yuanyuan Tang, Farzad Farnoud
conference: IEEE Transactions on Information Theory
year: 2021
bibkey: tang2020error
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.08174'}]
tags: ["Compact Codes"]
short_authors: Yuanyuan Tang, Farzad Farnoud
---
Because of its high data density and longevity, DNA is emerging as a
promising candidate for satisfying increasing data storage needs. Compared to
conventional storage media, however, data stored in DNA is subject to a wider
range of errors resulting from various processes involved in the data storage
pipeline. In this paper, we consider correcting duplication errors for both
exact and noisy tandem duplications of a given length k. An exact duplication
inserts a copy of a substring of length k of the sequence immediately after
that substring, e.g., ACGT to ACGACGT, where k = 3, while a noisy duplication
inserts a copy suffering from substitution noise, e.g., ACGT to ACGATGT.
Specifically, we design codes that can correct any number of exact duplication
and one noisy duplication errors, where in the noisy duplication case the copy
is at Hamming distance 1 from the original. Our constructions rely upon
recovering the duplication root of the stored codeword. We characterize the
ways in which duplication errors manifest in the root of affected sequences and
design efficient codes for correcting these error patterns. We show that the
proposed construction is asymptotically optimal, in the sense that it has the
same asymptotic rate as optimal codes correcting exact duplications only.