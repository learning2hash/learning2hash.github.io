---
layout: publication
title: Efficient Approximate Search For Sets Of Vectors
authors: Leybovich Michael, Shmueli Oded
conference: "Arxiv"
year: 2021
bibkey: leybovich2021efficient
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2107.06817"}
tags: ['ARXIV', 'Graph', 'Independent', 'LSH', 'Quantisation']
---
We consider a similarity measure between two sets \{&#37; raw &#37;\}\\(A\\)\{&#37; endraw &#37;\} and \{&#37; raw &#37;\}\\(B\\)\{&#37; endraw &#37;\} of vectors, that balances the average and maximum cosine distance between pairs of vectors, one from set \{&#37; raw &#37;\}\\(A\\)\{&#37; endraw &#37;\} and one from set \{&#37; raw &#37;\}\\(B\\)\{&#37; endraw &#37;\}. As a motivation for this measure, we present lineage tracking in a database. To practically realize this measure, we need an approximate search algorithm that given a set of vectors \{&#37; raw &#37;\}\\(A\\)\{&#37; endraw &#37;\} and sets of vectors \{&#37; raw &#37;\}\\(B\_1,...,B\_n\\)\{&#37; endraw &#37;\}, the algorithm quickly locates the set \{&#37; raw &#37;\}\\(B\_i\\)\{&#37; endraw &#37;\} that maximizes the similarity measure. For the case where all sets are singleton sets, essentially each is a single vector, there are known efficient approximate search algorithms, e.g., approximated versions of tree search algorithms, locality-sensitive hashing (LSH), vector quantization (VQ) and proximity graph algorithms. In this work, we present approximate search algorithms for the general case. The underlying idea in these algorithms is encoding a set of vectors via a long single vector. The proposed approximate approach achieves significant performance gains over an optimized, exact search on vector sets.
