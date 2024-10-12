---
layout: publication
title: Improved Fast Similarity Search In Dictionaries
authors: Karch Daniel, Luxen Dennis, Sanders Peter
conference: "Arxiv"
year: 2010
bibkey: karch2010improved
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1008.1191"}
tags: ['ARXIV']
---
We engineer an algorithm to solve the approximate dictionary matching problem. Given a list of words \{&#37; raw &#37;\}\\(\mathcal\{W\}\\)\{&#37; endraw &#37;\}, maximum distance \{&#37; raw &#37;\}\\(d\\)\{&#37; endraw &#37;\} fixed at preprocessing time and a query word \{&#37; raw &#37;\}\\(q\\)\{&#37; endraw &#37;\}, we would like to retrieve all words from \{&#37; raw &#37;\}\\(\mathcal\{W\}\\)\{&#37; endraw &#37;\} that can be transformed into \{&#37; raw &#37;\}\\(q\\)\{&#37; endraw &#37;\} with \{&#37; raw &#37;\}\\(d\\)\{&#37; endraw &#37;\} or less edit operations. We present data structures that support fault tolerant queries by generating an index. On top of that, we present a generalization of the method that eases memory consumption and preprocessing time significantly. At the same time, running times of queries are virtually unaffected. We are able to match in lists of hundreds of thousands of words and beyond within microseconds for reasonable distances.
