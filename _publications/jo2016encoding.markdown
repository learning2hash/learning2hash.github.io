---
layout: publication
title: Encoding Two-dimensional Range Top-k Queries
authors: Seungbum Jo, Srinivasa Rao Satti
conference: Arxiv
year: 2016
bibkey: jo2016encoding
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.07067'}]
tags: ["Similarity Search"]
short_authors: Seungbum Jo, Srinivasa Rao Satti
---
We consider the problem of encoding two-dimensional arrays, whose elements
come from a total order, for answering \topk\{\} queries. The aim is to obtain
encodings that use space close to the information-theoretic lower bound, which
can be constructed efficiently. For an \(m \times n\) array, with \(m \le n\), we
first propose an encoding for answering 1-sided \topk\{\} queries, whose query
range is restricted to \([1 \dots m][1 \dots a]\), for \(1 \le a \le n\). Next, we
propose an encoding for answering for the general (4-sided) \topk\{\} queries
that takes \((m\lg\{\{(k+1)n \choose n\}\}+2nm(m-1)+o(n))\) bits, which generalizes
the \textit\{joint Cartesian tree\} of Golin et al. [TCS 2016]. Compared with
trivial \(O(nm\lg\{n\})\)-bit encoding, our encoding takes less space when \(m =
o(\lg\{n\})\). In addition to the upper bound results for the encodings, we also
give lower bounds on encodings for answering \(1\) and \(4\)-sided \topk\{\} queries,
which show that our upper bound results are almost optimal.