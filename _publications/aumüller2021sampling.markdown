---
layout: publication
title: Sampling A Near Neighbor In High Dimensions -- Who Is The Fairest Of Them All
authors: Aumüller Martin, Har-peled Sariel, Mahabadi Sepideh, Pagh Rasmus, Silvestri Francesco
conference: "Arxiv"
year: 2021
bibkey: aumüller2021sampling
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2101.10905"}
tags: ['ARXIV', 'Independent', 'LSH']
---
Similarity search is a fundamental algorithmic primitive, widely used in many computer science disciplines. Given a set of points \{&#37; raw &#37;\}\\(S\\)\{&#37; endraw &#37;\} and a radius parameter \{&#37; raw &#37;\}\\(r>0\\)\{&#37; endraw &#37;\}, the \{&#37; raw &#37;\}\\(r\\)\{&#37; endraw &#37;\}-near neighbor (\{&#37; raw &#37;\}\\(r\\)\{&#37; endraw &#37;\}-NN) problem asks for a data structure that, given any query point \{&#37; raw &#37;\}\\(q\\)\{&#37; endraw &#37;\}, returns a point \{&#37; raw &#37;\}\\(p\\)\{&#37; endraw &#37;\} within distance at most \{&#37; raw &#37;\}\\(r\\)\{&#37; endraw &#37;\} from \{&#37; raw &#37;\}\\(q\\)\{&#37; endraw &#37;\}. In this paper, we study the \{&#37; raw &#37;\}\\(r\\)\{&#37; endraw &#37;\}-NN problem in the light of individual fairness and providing equal opportunities: all points that are within distance \{&#37; raw &#37;\}\\(r\\)\{&#37; endraw &#37;\} from the query should have the same probability to be returned. In the low-dimensional case, this problem was first studied by Hu, Qiao, and Tao (PODS 2014). Locality sensitive hashing (LSH), the theoretically strongest approach to similarity search in high dimensions, does not provide such a fairness guarantee. In this work, we show that LSH based algorithms can be made fair, without a significant loss in efficiency. We propose several efficient data structures for the exact and approximate variants of the fair NN problem. Our approach works more generally for sampling uniformly from a sub-collection of sets of a given collection and can be used in a few other applications. We also develop a data structure for fair similarity search under inner product that requires nearly-linear space and exploits locality sensitive filters. The paper concludes with an experimental evaluation that highlights the inherent unfairness of NN data structures and shows the performance of our algorithms on real-world datasets.
