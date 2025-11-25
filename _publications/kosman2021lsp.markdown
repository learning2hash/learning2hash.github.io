---
layout: publication
title: 'LSP : Acceleration And Regularization Of Graph Neural Networks Via Locality
  Sensitive Pruning Of Graphs'
authors: Eitan Kosman, Joel Oren, Dotan di Castro
conference: Arxiv
year: 2021
bibkey: kosman2021lsp
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.05694'}]
tags: ["Efficiency", "Graph Based ANN", "Locality-Sensitive-Hashing"]
short_authors: Eitan Kosman, Joel Oren, Dotan di Castro
---
Graph Neural Networks (GNNs) have emerged as highly successful tools for
graph-related tasks. However, real-world problems involve very large graphs,
and the compute resources needed to fit GNNs to those problems grow rapidly.
Moreover, the noisy nature and size of real-world graphs cause GNNs to over-fit
if not regularized properly. Surprisingly, recent works show that large graphs
often involve many redundant components that can be removed without
compromising the performance too much. This includes node or edge removals
during inference through GNNs layers or as a pre-processing step that
sparsifies the input graph. This intriguing phenomenon enables the development
of state-of-the-art GNNs that are both efficient and accurate. In this paper,
we take a further step towards demystifying this phenomenon and propose a
systematic method called Locality-Sensitive Pruning (LSP) for graph pruning
based on Locality-Sensitive Hashing. We aim to sparsify a graph so that similar
local environments of the original graph result in similar environments in the
resulting sparsified graph, which is an essential feature for graph-related
tasks. To justify the application of pruning based on local graph properties,
we exemplify the advantage of applying pruning based on locality properties
over other pruning strategies in various scenarios. Extensive experiments on
synthetic and real-world datasets demonstrate the superiority of LSP, which
removes a significant amount of edges from large graphs without compromising
the performance, accompanied by a considerable acceleration.