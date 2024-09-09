---
layout: publication
title: "Balanced Allocations and Double Hashing"
authors: Mitzenmacher Michael
conference: Arxiv
year: 2012
bibkey: mitzenmacher2012balanced
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1209.5360"}
tags: ['ARXIV', 'TIP']
---
Double hashing has recently found more common usage in schemes that use multiple hash functions. In double hashing, for an item \$x\$, one generates two hash values \$f(x)\$ and \$g(x)\$, and then uses combinations \$(f(x) +k g(x)) \bmod n\$ for \$k=0,1,2,...\$ to generate multiple hash values from the initial two. We first perform an empirical study showing that, surprisingly, the performance difference between double hashing and fully random hashing appears negligible in the standard balanced allocation paradigm, where each item is placed in the least loaded of \$d\$ choices, as well as several related variants. We then provide theoretical results that explain the behavior of double hashing in this context.