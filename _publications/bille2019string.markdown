---
layout: publication
title: String Indexing With Compressed Patterns
authors: "Philip Bille, Inge Li G\xF8rtz, Teresa Anna Steiner"
conference: journal ACM Trans. Algorithms volume 19 pages 321-3219 year 2023
year: 2020
bibkey: bille2019string
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.11930'}]
tags: ["Efficiency"]
short_authors: "Philip Bille, Inge Li G\xF8rtz, Teresa Anna Steiner"
---
Given a string \\(S\\) of length \\(n\\), the classic string indexing problem is to
preprocess \\(S\\) into a compact data structure that supports efficient subsequent
pattern queries. In this paper we consider the basic variant where the pattern
is given in compressed form and the goal is to achieve query time that is fast
in terms of the compressed size of the pattern. This captures the common
client-server scenario, where a client submits a query and communicates it in
compressed form to a server. Instead of the server decompressing the query
before processing it, we consider how to efficiently process the compressed
query directly. Our main result is a novel linear space data structure that
achieves near-optimal query time for patterns compressed with the classic
Lempel-Ziv compression scheme. Along the way we develop several data structural
techniques of independent interest, including a novel data structure that
compactly encodes all LZ77 compressed suffixes of a string in linear space and
a general decomposition of tries that reduces the search time from logarithmic
in the size of the trie to logarithmic in the length of the pattern.