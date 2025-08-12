---
layout: publication
title: Load-balancing Succinct B Trees
authors: "Tomohiro I, Dominik K\xF6ppl"
conference: Arxiv
year: 2021
bibkey: i2021load
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.08751'}]
tags: ["Efficiency", "Scalability", "Tree Based ANN"]
short_authors: "Tomohiro I, Dominik K\xF6ppl"
---
We propose a B tree representation storing \(n\) keys, each of \(k\) bits, in
either (a) \(nk + O(nk / \lg n)\) bits or (b) \(nk + O(nk \lg \lg n/ \lg n)\) bits
of space supporting all B tree operations in either (a) \(O(\lg n )\) time or (b)
\(O(\lg n / \lg \lg n)\) time, respectively. We can augment each node with an
aggregate value such as the minimum value within its subtree, and maintain
these aggregate values within the same space and time complexities. Finally, we
give the sparse suffix tree as an application, and present a linear-time
algorithm computing the sparse longest common prefix array from the suffix AVL
tree of Irving et al. [JDA'2003].