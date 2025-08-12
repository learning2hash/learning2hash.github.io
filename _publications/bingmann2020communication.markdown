---
layout: publication
title: Communication-efficient String Sorting
authors: Timo Bingmann, Peter Sanders, Matthias Schimek
conference: 2020 IEEE International Parallel and Distributed Processing Symposium
  (IPDPS)
year: 2020
bibkey: bingmann2020communication
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.08516'}]
tags: ["Efficiency", "Memory Efficiency", "Scalability"]
short_authors: Timo Bingmann, Peter Sanders, Matthias Schimek
---
There has been surprisingly little work on algorithms for sorting strings on
distributed-memory parallel machines. We develop efficient algorithms for this
problem based on the multi-way merging principle. These algorithms inspect only
characters that are needed to determine the sorting order. Moreover,
communication volume is reduced by also communicating (roughly) only those
characters and by communicating repetitions of the same prefixes only once.
Experiments on up to 1280 cores reveal that these algorithm are often more than
five times faster than previous algorithms.