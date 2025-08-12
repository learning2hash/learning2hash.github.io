---
layout: publication
title: Fourier Sliced-wasserstein Embedding For Multisets And Measures
authors: Tal Amir, Nadav Dym
conference: Arxiv
year: 2025
bibkey: amir2024fourier
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.16519'}]
tags: []
short_authors: Tal Amir, Nadav Dym
---
We present the Fourier Sliced-Wasserstein (FSW) embedding - a novel method to
embed multisets and measures over R^d into Euclidean space.
  Our proposed embedding approximately preserves the sliced Wasserstein
distance on distributions, thereby yielding geometrically meaningful
representations that better capture the structure of the input. Moreover, it is
injective on measures and bi-Lipschitz on multisets - a significant advantage
over prevalent methods based on sum- or max-pooling, which are provably not
bi-Lipschitz, and, in many cases, not even injective. The required output
dimension for these guarantees is near-optimal: roughly 2Nd, where N is the
maximal input multiset size.
  Furthermore, we prove that it is impossible to embed distributions over R^d
into Euclidean space in a bi-Lipschitz manner. Thus, the metric properties of
our embedding are, in a sense, the best possible.
  Through numerical experiments, we demonstrate that our method yields superior
multiset representations that improve performance in practical learning tasks.
Specifically, we show that (a) a simple combination of the FSW embedding with
an MLP achieves state-of-the-art performance in learning the (non-sliced)
Wasserstein distance; and (b) replacing max-pooling with the FSW embedding
makes PointNet significantly more robust to parameter reduction, with only
minor performance degradation even after a 40-fold reduction.