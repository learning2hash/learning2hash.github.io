---
layout: publication
title: Maximal Closed Substrings
authors: Golnaz Badkobeh, Alessandro de Luca, Gabriele Fici, Simon Puglisi
conference: Lecture Notes in Computer Science
year: 2022
bibkey: badkobeh2022maximal
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.00271'}]
tags: []
short_authors: Badkobeh et al.
---
A string is closed if it has length 1 or has a nonempty border without
internal occurrences. In this paper we introduce the definition of a
*maximal closed substring* (MCS), which is an occurrence of a closed
substring that cannot be extended to the left nor to the right into a longer
closed substring. MCSs with exponent at least \(2\) are commonly called
*runs*; those with exponent smaller than \(2\), instead, are particular
cases of *maximal gapped repeats*. We provide an algorithm that, given a
string of length \(n\) locates all MCSs the string contains in \(\mathcal O(nlog
n)\) time.