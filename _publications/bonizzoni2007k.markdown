---
layout: publication
title: The \(k\)-anonymity Problem Is Hard
authors: Paola Bonizzoni, Gianluca Della Vedova, Riccardo Dondi
conference: Lecture Notes in Computer Science
year: 2009
bibkey: bonizzoni2007k
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/0707.0421'}]
tags: ["Privacy & Security"]
short_authors: Paola Bonizzoni, Gianluca Della Vedova, Riccardo Dondi
---
The problem of publishing personal data without giving up privacy is becoming
increasingly important. An interesting formalization recently proposed is the
k-anonymity. This approach requires that the rows in a table are clustered in
sets of size at least k and that all the rows in a cluster become the same
tuple, after the suppression of some records. The natural optimization problem,
where the goal is to minimize the number of suppressed entries, is known to be
NP-hard when the values are over a ternary alphabet, k = 3 and the rows length
is unbounded. In this paper we give a lower bound on the approximation factor
that any polynomial-time algorithm can achive on two restrictions of the
problem,namely (i) when the records values are over a binary alphabet and k =
3, and (ii) when the records have length at most 8 and k = 4, showing that
these restrictions of the problem are APX-hard.