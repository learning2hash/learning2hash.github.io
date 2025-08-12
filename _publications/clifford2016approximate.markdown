---
layout: publication
title: Approximate Hamming Distance In A Stream
authors: Raphael Clifford, Tatiana Starikovskaya
conference: Arxiv
year: 2016
bibkey: clifford2016approximate
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.07241'}]
tags: ["Distance Metric Learning", "Efficiency", "Hashing Methods", "Locality Sensitive Hashing", "Scalability"]
short_authors: Raphael Clifford, Tatiana Starikovskaya
---
We consider the problem of computing a \((1+\epsilon)\)-approximation of the
Hamming distance between a pattern of length \(n\) and successive substrings of a
stream. We first look at the one-way randomised communication complexity of
this problem, giving Alice the first half of the stream and Bob the second
half. We show the following: (1) If Alice and Bob both share the pattern then
there is an \(O(\epsilon^\{-4\} log^2 n)\) bit randomised one-way communication
protocol. (2) If only Alice has the pattern then there is an
\(O(\epsilon^\{-2\}\sqrt\{n\}log n)\) bit randomised one-way communication protocol.
  We then go on to develop small space streaming algorithms for
\((1+\epsilon)\)-approximate Hamming distance which give worst case running time
guarantees per arriving symbol. (1) For binary input alphabets there is an
\(O(\epsilon^\{-3\} \sqrt\{n\} log^\{2\} n)\) space and \(O(\epsilon^\{-2\} log\{n\})\)
time streaming \((1+\epsilon)\)-approximate Hamming distance algorithm. (2) For
general input alphabets there is an \(O(\epsilon^\{-5\} \sqrt\{n\} log^\{4\} n)\)
space and \(O(\epsilon^\{-4\} log^3 \{n\})\) time streaming
\((1+\epsilon)\)-approximate Hamming distance algorithm.