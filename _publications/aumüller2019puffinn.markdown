---
layout: publication
title: 'PUFFINN: Parameterless And Universally Fast Finding Of Nearest Neighbors'
authors: "Aum\xFCller et al."
conference: 2022 29th International Conference on Systems, Signals and Image Processing
  (IWSSIP)
year: 2019
bibkey: "aum\xFCller2019puffinn"
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.12211'}]
---
We present PUFFINN, a parameterless LSH-based index for solving the
\\(k\\)-nearest neighbor problem with probabilistic guarantees. By parameterless we
mean that the user is only required to specify the amount of memory the index
is supposed to use and the result quality that should be achieved. The index
combines several heuristic ideas known in the literature. By small adaptions to
the query algorithm, we make heuristics rigorous. We perform experiments on
real-world and synthetic inputs to evaluate implementation choices and show
that the implementation satisfies the quality guarantees while being
competitive with other state-of-the-art approaches to nearest neighbor search.
  We describe a novel synthetic data set that is difficult to solve for almost
all existing nearest neighbor search approaches, and for which PUFFINN
significantly outperform previous methods.