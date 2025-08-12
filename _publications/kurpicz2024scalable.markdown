---
layout: publication
title: Scalable Distributed String Sorting
authors: Florian Kurpicz, Pascal Mehnert, Peter Sanders, Matthias Schimek
conference: Arxiv
year: 2024
bibkey: kurpicz2024scalable
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.16517'}]
tags: ["Efficiency", "Scalability"]
short_authors: Kurpicz et al.
---
String sorting is an important part of tasks such as building index data
structures. Unfortunately, current string sorting algorithms do not scale to
massively parallel distributed-memory machines since they either have latency
(at least) proportional to the number of processors \(p\) or communicate the data
a large number of times (at least logarithmic). We present practical and
efficient algorithms for distributed-memory string sorting that scale to large
\(p\). Similar to state-of-the-art sorters for atomic objects, the algorithms
have latency of about \(p^\{1/k\}\) when allowing the data to be communicated \(k\)
times. Experiments indicate good scaling behavior on a wide range of inputs on
up to 49152 cores. Overall, we achieve speedups of up to 5 over the current
state-of-the-art distributed string sorting algorithms.