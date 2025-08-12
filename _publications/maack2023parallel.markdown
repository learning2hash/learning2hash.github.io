---
layout: publication
title: Parallel Computation Of Piecewise Linear Morse-smale Segmentations
authors: Robin G. C. Maack, Jonas Lukasczyk, Julien Tierny, Hans Hagen, Ross MacIejewski,
  Christoph Garth
conference: IEEE Transactions on Visualization and Computer Graphics
year: 2023
bibkey: maack2023parallel
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.15491'}]
tags: []
short_authors: Maack et al.
---
This paper presents a well-scaling parallel algorithm for the computation of
Morse-Smale (MS) segmentations, including the region separators and region
boundaries. The segmentation of the domain into ascending and descending
manifolds, solely defined on the vertices, improves the computational time
using path compression and fully segments the border region. Region boundaries
and region separators are generated using a multi-label marching tetrahedra
algorithm. This enables a fast and simple solution to find optimal parameter
settings in preliminary exploration steps by generating an MS complex preview.
It also poses a rapid option to generate a fast visual representation of the
region geometries for immediate utilization. Two experiments demonstrate the
performance of our approach with speedups of over an order of magnitude in
comparison to two publicly available implementations. The example section shows
the similarity to the MS complex, the useability of the approach, and the
benefits of this method with respect to the presented datasets. We provide our
implementation with the paper.