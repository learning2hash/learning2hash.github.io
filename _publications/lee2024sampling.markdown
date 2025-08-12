---
layout: publication
title: Sampling Space-saving Set Sketches
authors: Homin K. Lee, Charles Masson
conference: Arxiv
year: 2024
bibkey: lee2024sampling
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.08604'}]
tags: ["Efficiency", "Memory Efficiency", "Scalability"]
short_authors: Homin K. Lee, Charles Masson
---
Large, distributed data streams are now ubiquitous. High-accuracy sketches
with low memory overhead have become the de facto method for analyzing this
data. For instance, if we wish to group data by some label and report the
largest counts using fixed memory, we need to turn to mergeable heavy hitter
sketches that can provide highly accurate approximate counts. Similarly, if we
wish to keep track of the number of distinct items in a single set spread
across several streams using fixed memory, we can turn to mergeable count
distinct sketches that can provide highly accurate set cardinalities.
  If we were to try to keep track of the cardinality of multiple sets and
report only on the largest ones, maintaining individual count distinct sketches
for each set can grow unwieldy, especially if the number of sets is not known
in advance. We consider the natural combination of the heavy hitters problem
with the count distinct problem, the heavy distinct hitters problem: given a
stream of \((\ell, x)\) pairs, find all the labels \(\ell\) that are paired with a
large number of distinct items \(x\) using only constant memory.
  No previous work on heavy distinct hitters has managed to be of practical use
in the large, distributed data stream setting. We propose a new algorithm, the
Sampling Space-Saving Set Sketch, which combines sketching and sampling
techniques and has all the desired properties for size, speed, accuracy,
mergeability, and invertibility. We compare our algorithm to several existing
solutions to the heavy distinct hitters problem, and provide experimental
results across several data sets showing the superiority of the new sketch.