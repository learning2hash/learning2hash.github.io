---
layout: publication
title: 'PANDORA: A Parallel Dendrogram Construction Algorithm For Single Linkage Clustering
  On GPU'
authors: "Piyush Sao, Andrey Prokopenko, Damien Lebrun-Grandi\xE9"
conference: Arxiv
year: 2024
bibkey: sao2024pandora
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.06089'}]
tags: ["Efficiency"]
short_authors: "Piyush Sao, Andrey Prokopenko, Damien Lebrun-Grandi\xE9"
---
This paper presents \pandora, a novel parallel algorithm for efficiently
constructing dendrograms for single-linkage hierarchical clustering, including
\hdbscan. Traditional dendrogram construction methods from a minimum spanning
tree (MST), such as agglomerative or divisive techniques, often fail to
efficiently parallelize, especially with skewed dendrograms common in
real-world data.
  \pandora addresses these challenges through a unique recursive tree
contraction method, which simplifies the tree for initial dendrogram
construction and then progressively reconstructs the complete dendrogram. This
process makes \pandora asymptotically work-optimal, independent of dendrogram
skewness. All steps in \pandora are fully parallel and suitable for massively
threaded accelerators such as GPUs.
  Our implementation is written in Kokkos, providing support for both CPUs and
multi-vendor GPUs (e.g., Nvidia, AMD). The multithreaded version of \pandora is
2.2\(\times\) faster than the current best-multithreaded implementation, while
the GPU \pandora implementation achieved 6-20\(\times\) on \amdgpu and
10-37\(\times\) on \nvidiagpu speed-up over multithreaded \pandora. These
advancements lead to up to a 6-fold speedup for \hdbscan on GPUs over the
current best, which only offload MST construction to GPUs and perform
multithreaded dendrogram construction.