---
layout: publication
title: 'Engineering Minimal K-perfect Hash Functions'
authors: Stefan Hermann, Sebastian Kirmayer, Hans-peter Lehmann, Peter Sanders, Stefan Walzer
conference: "Arxiv"
year: 2025
citations: 0
bibkey: hermann2025engineering
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2504.20001'}
tags: ['Hashing Fundamentals', 'Evaluation Metrics', 'Hashing Methods', 'Applications']
---
Given a set S of n keys, a k-perfect hash function (kPHF) is a data structure
that maps the keys to the first m integers, where each output integer can be
hit by at most k input keys. When m=n/k, the resulting function is called a
minimal k-perfect hash function (MkPHF). Applications of kPHFs can be found in
external memory data structures or to create efficient 1-perfect hash
functions, which in turn have a wide range of applications from databases to
bioinformatics. Several papers from the 1980s look at external memory data
structures with small internal memory indexes. However, actual k-perfect hash
functions are surprisingly rare, and the area has not seen a lot of research
recently. At the same time, recent research in 1-perfect hashing shows that
there is a lack of efficient kPHFs. In this paper, we revive the area of
k-perfect hashing, presenting four new constructions. Our implementations
simultaneously dominate older approaches in space consumption, construction
time, and query time. We see this paper as a possible starting point of an
active line of research, similar to the area of 1-perfect hashing.
