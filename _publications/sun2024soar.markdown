---
layout: publication
title: SOAR Improved Indexing For Approximate Nearest Neighbor Search
authors: Sun Philip, Simcha David, Dopson Dave, Guo Ruiqi, Kumar Sanjiv
conference: "Advances in Neural Information Processing Systems"
year: 2024
bibkey: sun2024soar
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2404.00774"}
tags: ['Independent', 'NEURIPS']
---
<p>This paper introduces SOAR: Spilling with Orthogonality-Amplified
Residuals, a novel data indexing technique for approximate nearest
neighbor (ANN) search. SOAR extends upon previous approaches to ANN
search, such as spill trees, that utilize multiple redundant
representations while partitioning the data to reduce the probability of
missing a nearest neighbor during search. Rather than training and
computing these redundant representations independently, however, SOAR
uses an orthogonality-amplified residual loss, which optimizes each
representation to compensate for cases where other representations
perform poorly. This drastically improves the overall index quality,
resulting in state-of-the-art ANN benchmark performance while
maintaining fast indexing times and low memory consumption.</p>
