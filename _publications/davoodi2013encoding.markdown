---
layout: publication
title: Encoding Range Minimum Queries
authors: Pooya Davoodi, Gonzalo Navarro, Rajeev Raman, S. Srinivasa Rao
conference: Arxiv
year: 2013
bibkey: davoodi2013encoding
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1311.4394'}]
tags: ["Efficiency"]
short_authors: Davoodi et al.
---
We consider the problem of encoding range minimum queries (RMQs): given an
array A[1..n] of distinct totally ordered values, to pre-process A and create a
data structure that can answer the query RMQ(i,j), which returns the index
containing the smallest element in A[i..j], without access to the array A at
query time. We give a data structure whose space usage is 2n + o(n) bits, which
is asymptotically optimal for worst-case data, and answers RMQs in O(1)
worst-case time. This matches the previous result of Fischer and Heun [SICOMP,
2011], but is obtained in a more natural way. Furthermore, our result can
encode the RMQs of a random array A in 1.919n + o(n) bits in expectation, which
is not known to hold for Fischer and Heun's result. We then generalize our
result to the encoding range top-2 query (RT2Q) problem, which is like the
encoding RMQ problem except that the query RT2Q(i,j) returns the indices of
both the smallest and second-smallest elements of A[i..j]. We introduce a data
structure using 3.272n+o(n) bits that answers RT2Qs in constant time, and also
give lower bounds on the effective entropy\} of RT2Q.