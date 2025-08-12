---
layout: publication
title: Hardness-preserving Reductions Via Cuckoo Hashing
authors: Itay Berman, Iftach Haitner, Ilan Komargodski, Moni Naor
conference: Lecture Notes in Computer Science
year: 2013
bibkey: berman2013hardness
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.01409'}]
tags: ["Hashing Methods"]
short_authors: Berman et al.
---
The focus of this work is *hardness-preserving* transformations of
somewhat limited pseudorandom functions families (PRFs) into ones with more
versatile characteristics. Consider the problem of *domain extension* of
pseudorandom functions: given a PRF that takes as input elements of some domain
\(U\), we would like to come up with a PRF over a larger domain. Can we do it
with little work and without significantly impacting the security of the
system? One approach is to first hash the larger domain into the smaller one
and then apply the original PRF. Such a reduction, however, is vulnerable to a
"birthday attack": after \(\sqrt\{\size\{U\}\}\) queries to the resulting PRF, a
collision (\ie two distinct inputs having the same hash value) is very likely
to occur. As a consequence, the resulting PRF is *insecure* against an
attacker making this number of queries. In this work we show how to go beyond
the aforementioned birthday attack barrier by replacing the above simple
hashing approach with a variant of \textit\{cuckoo hashing\}, a hashing paradigm
that resolves collisions in a table by using two hash functions and two tables,
cleverly assigning each element to one of the two tables. We use this approach
to obtain: (i) a domain extension method that requires \{\em just two calls\} to
the original PRF, can withstand as many queries as the original domain size,
and has a distinguishing probability that is exponentially small in the amount
of non-cryptographic work; and (ii) a \{\em security-preserving\} reduction from
non-adaptive to adaptive PRFs.