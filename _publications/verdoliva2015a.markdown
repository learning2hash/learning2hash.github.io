---
layout: publication
title: A reliable order-statistics-based approximate nearest neighbor search algorithm
authors: Verdoliva Luisa, Cozzolino Davide, Poggi Giovanni
conference: "Arxiv"
year: 2015
bibkey: verdoliva2015a
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1509.03453"}
tags: ['ARXIV']
---
We propose a new algorithm for fast approximate nearest neighbor search based on the properties of ordered vectors. Data vectors are classified based on the index and sign of their largest components, thereby partitioning the space in a number of cones centered in the origin. The query is itself classified, and the search starts from the selected cone and proceeds to neighboring ones. Overall, the proposed algorithm corresponds to locality sensitive hashing in the space of directions, with hashing based on the order of components. Thanks to the statistical features emerging through ordering, it deals very well with the challenging case of unstructured data, and is a valuable building block for more complex techniques dealing with structured data. Experiments on both simulated and real-world data prove the proposed algorithm to provide a state-of-the-art performance.
