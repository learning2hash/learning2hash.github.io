---
layout: publication
title: Subspace Approximation For Approximate Nearest Neighbor Search In NLP
authors: Wang Jing
conference: "Arxiv"
year: 2017
bibkey: wang2017subspace
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1708.07775"}
tags: ['ARXIV', 'Supervised']
---
Most natural language processing tasks can be formulated as the approximated nearest neighbor search problem, such as word analogy, document similarity, machine translation. Take the question-answering task as an example, given a question as the query, the goal is to search its nearest neighbor in the training dataset as the answer. However, existing methods for approximate nearest neighbor search problem may not perform well owing to the following practical challenges: 1) there are noise in the data; 2) the large scale dataset yields a huge retrieval space and high search time complexity. In order to solve these problems, we propose a novel approximate nearest neighbor search framework which i) projects the data to a subspace based spectral analysis which eliminates the influence of noise; ii) partitions the training dataset to different groups in order to reduce the search space. Specifically, the retrieval space is reduced from \{&#37; raw &#37;\}\\(O(n)\\)\{&#37; endraw &#37;\} to \{&#37; raw &#37;\}\\(O(\log n)\\)\{&#37; endraw &#37;\} (where \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} is the number of data points in the training dataset). We prove that the retrieved nearest neighbor in the projected subspace is the same as the one in the original feature space. We demonstrate the outstanding performance of our framework on real-world natural language processing tasks.
