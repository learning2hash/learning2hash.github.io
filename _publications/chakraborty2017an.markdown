---
layout: publication
title: An Improved Video Analysis Using Context Based Extension Of LSH
authors: Angana Chakraborty, Sanghamitra Bandyopadhyay
conference: Arxiv
year: 2017
bibkey: chakraborty2017an
citations: 0
additional_links: [{name: Code, url: 'http://www.isical.ac.in/~bioinfo_miu/conLSH/conLSH.html'},
  {name: Paper, url: 'https://arxiv.org/abs/1705.03933'}]
tags: [Hashing Methods, Locality Sensitive Hashing, Video Retrieval, Datasets]
short_authors: Angana Chakraborty, Sanghamitra Bandyopadhyay
---
Locality Sensitive Hashing (LSH) based algorithms have already shown their
promise in finding approximate nearest neighbors in high dimen- sional data
space. However, there are certain scenarios, as in sequential data, where the
proximity of a pair of points cannot be captured without considering their
surroundings or context. In videos, as for example, a particular frame is
meaningful only when it is seen in the context of its preceding and following
frames. LSH has no mechanism to handle the con- texts of the data points. In
this article, a novel scheme of Context based Locality Sensitive Hashing
(conLSH) has been introduced, in which points are hashed together not only
based on their closeness, but also because of similar context. The contribution
made in this article is three fold. First, conLSH is integrated with a recently
proposed fast optimal sequence alignment algorithm (FOGSAA) using a layered
approach. The resultant method is applied to video retrieval for extracting
similar sequences. The pro- posed algorithm yields more than 80% accuracy on an
average in different datasets. It has been found to save 36.3% of the total
time, consumed by the exhaustive search. conLSH reduces the search space to
approximately 42% of the entire dataset, when compared with an exhaustive
search by the aforementioned FOGSAA, Bag of Words method and the standard LSH
implementations. Secondly, the effectiveness of conLSH is demon- strated in
action recognition of the video clips, which yields an average gain of 12.83%
in terms of classification accuracy over the state of the art methods using
STIP descriptors. The last but of great significance is that this article
provides a way of automatically annotating long and composite real life videos.
The source code of conLSH is made available at
http://www.isical.ac.in/~bioinfo_miu/conLSH/conLSH.html