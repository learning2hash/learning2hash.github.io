---
layout: publication
title: Adaptively Learning The Crowd Kernel
authors: Omer Tamuz, Ce Liu, Serge Belongie, Ohad Shamir, Adam Tauman Kalai
conference: The 28th International Conference on Machine Learning 2011
year: 2011
bibkey: tamuz2011adaptively
citations: 146
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1105.1033'}]
tags: ["Uncategorized"]
short_authors: Tamuz et al.
---
We introduce an algorithm that, given n objects, learns a similarity matrix
over all n^2 pairs, from crowdsourced data alone. The algorithm samples
responses to adaptively chosen triplet-based relative-similarity queries. Each
query has the form "is object 'a' more similar to 'b' or to 'c'?" and is chosen
to be maximally informative given the preceding responses. The output is an
embedding of the objects into Euclidean space (like MDS); we refer to this as
the "crowd kernel." SVMs reveal that the crowd kernel captures prominent and
subtle features across a number of domains, such as "is striped" among neckties
and "vowel vs. consonant" among letters.