---
layout: publication
title: An In-place Framework For Exact And Approximate Shortest Unique Substring Queries
authors: Wing-Kai Hon, Sharma V. Thankachan, Bojian Xu
conference: Lecture Notes in Computer Science
year: 2015
bibkey: hon2015place
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1512.00378'}]
tags: []
short_authors: Wing-Kai Hon, Sharma V. Thankachan, Bojian Xu
---
We revisit the exact shortest unique substring (SUS) finding problem, and
propose its approximate version where mismatches are allowed, due to its
applications in subfields such as computational biology. We design a generic
in-place framework that fits to solve both the exact and approximate
\(k\)-mismatch SUS finding, using the minimum \(2n\) memory words plus \(n\) bytes
space, where \(n\) is the input string size. By using the in-place framework, we
can find the exact and approximate \(k\)-mismatch SUS for every string position
using a total of \(O(n)\) and \(O(n^2)\) time, respectively, regardless of the
value of \(k\). Our framework does not involve any compressed or succinct data
structures and thus is practical and easy to implement.