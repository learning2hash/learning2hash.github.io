---
layout: publication
title: Efficient Online String Matching Based On Characters Distance Text Sampling
authors: Simone Faro, Arianna Pavone, Francesco Pio Marino
conference: Algorithmica
year: 2020
bibkey: faro2019efficient
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.05930'}]
tags: ["Efficiency"]
short_authors: Simone Faro, Arianna Pavone, Francesco Pio Marino
---
Searching for all occurrences of a pattern in a text is a fundamental problem
in computer science with applications in many other fields, like natural
language processing, information retrieval and computational biology. Sampled
string matching is an efficient approach recently introduced in order to
overcome the prohibitive space requirements of an index construction, on the
one hand, and drastically reduce searching time for the online solutions, on
the other hand. In this paper we present a new algorithm for the sampled string
matching problem, based on a characters distance sampling approach. The main
idea is to sample the distances between consecutive occurrences of a given
pivot character and then to search online the sampled data for any occurrence
of the sampled pattern, before verifying the original text. From a theoretical
point of view we prove that, under suitable conditions, our solution can
achieve both linear worst-case time complexity and optimal average-time
complexity. From a practical point of view it turns out that our solution shows
a sub-linear behaviour in practice and speeds up online searching by a factor
of up to 9, using limited additional space whose amount goes from 11% to 2.8%
of the text size, with a gain up to 50% if compared with previous solutions.