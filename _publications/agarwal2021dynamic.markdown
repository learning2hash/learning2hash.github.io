---
layout: publication
title: Dynamic Enumeration Of Similarity Joins
authors: Agarwal Pankaj K., Hu Xiao, Sintos Stavros, Yang Jun
conference: "Arxiv"
year: 2021
bibkey: agarwal2021dynamic
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2105.01818"}
tags: ['ARXIV', 'Independent', 'LSH']
---
This paper considers enumerating answers to similarity-join queries under dynamic updates: Given two sets of \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} points \{&#37; raw &#37;\}\\(A,B\\)\{&#37; endraw &#37;\} in \{&#37; raw &#37;\}\\(\mathbb\{R\}^d\\)\{&#37; endraw &#37;\}, a metric \{&#37; raw &#37;\}\\(\phi(\cdot)\\)\{&#37; endraw &#37;\}, and a distance threshold \{&#37; raw &#37;\}\\(r > 0\\)\{&#37; endraw &#37;\}, report all pairs of points \{&#37; raw &#37;\}\\((a, b) \in A \times B\\)\{&#37; endraw &#37;\} with \{&#37; raw &#37;\}\\(\phi(a,b) \le r\\)\{&#37; endraw &#37;\}. Our goal is to store \{&#37; raw &#37;\}\\(A,B\\)\{&#37; endraw &#37;\} into a dynamic data structure that, whenever asked, can enumerate all result pairs with worst-case delay guarantee, i.e., the time between enumerating two consecutive pairs is bounded. Furthermore, the data structure can be efficiently updated when a point is inserted into or deleted from \{&#37; raw &#37;\}\\(A\\)\{&#37; endraw &#37;\} or \{&#37; raw &#37;\}\\(B\\)\{&#37; endraw &#37;\}. We propose several efficient data structures for answering similarity-join queries in low dimension. For exact enumeration of similarity join, we present near-linear-size data structures for \{&#37; raw &#37;\}\\(\ell\_1, \ell\_\infty\\)\{&#37; endraw &#37;\} metrics with \{&#37; raw &#37;\}\\(\log^\{O(1)\} n\\)\{&#37; endraw &#37;\} update time and delay. We show that such a data structure is not feasible for the \{&#37; raw &#37;\}\\(\ell\_2\\)\{&#37; endraw &#37;\} metric for \{&#37; raw &#37;\}\\(d \ge 4\\)\{&#37; endraw &#37;\}. For approximate enumeration of similarity join, where the distance threshold is a soft constraint, we obtain a unified linear-size data structure for \{&#37; raw &#37;\}\\(\ell\_p\\)\{&#37; endraw &#37;\} metric, with \{&#37; raw &#37;\}\\(\log^\{O(1)\} n\\)\{&#37; endraw &#37;\} delay and update time. In high dimensions, we present an efficient data structure with worst-case delay-guarantee using locality sensitive hashing (LSH).
