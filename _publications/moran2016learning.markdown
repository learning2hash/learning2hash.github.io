---
layout: publication
title: Learning To Project And Binarise For Hashing-based Approximate Nearest Neighbour
  Search
authors: S. Moran
conference: Proceedings of the 39th International ACM SIGIR conference on Research
  and Development in Information Retrieval
year: 2016
bibkey: moran2016learning
citations: 1
additional_links: [{name: Paper, url: 'https://dl.acm.org/citation.cfm?id=2914766'}]
tags: [Hashing Methods, SIGIR, Similarity Search, Datasets]
short_authors: S. Moran
---
In this paper we focus on improving the effectiveness of hashing-based approximate nearest neighbour search. Generating similarity preserving hashcodes for images has been shown to be an effective and efficient method for searching through large datasets. Hashcode generation generally involves two steps: bucketing the input feature space with a set of hyperplanes, followed by quantising the projection of the data-points onto the normal vectors to those hyperplanes. This procedure results in the makeup of the hashcodes depending on the positions of the data-points with respect to the hyperplanes in the feature space, allowing a degree of locality to be encoded into the hashcodes. In this paper we study the effect of learning both the hyperplanes and the thresholds as part of the same model. Most previous research either learn the hyperplanes assuming a fixed set of thresholds, or vice-versa. In our experiments over two standard image datasets we find statistically significant increases in retrieval effectiveness versus a host of state-of-the-art data-dependent and independent hashing models.