---
layout: publication
title: 'From Average Embeddings To Nearest Neighbor Search'
authors: Alexandr Andoni, David Cheikhi
conference: "Arxiv"
year: 2021
citations: 0
bibkey: andoni2021from
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2105.05761'}
tags: ['Hashing Fundamentals', 'Hashing Methods', 'ANN Search', 'Approximate Nearest Neighbor Search']
---
In this note, we show that one can use average embeddings, introduced
recently in [Naor'20, arXiv:1905.01280], to obtain efficient algorithms for
approximate nearest neighbor search. In particular, a metric \\(X\\) embeds into
\\(ℓ₂\\) on average, with distortion \\(D\\), if, for any distribution \\(\mu\\) on
\\(X\\), the embedding is \\(D\\) Lipschitz and the (square of) distance does not
decrease on average (wrt \\(\mu\\)). In particular existence of such an embedding
(assuming it is efficient) implies a \\(O(D^3)\\) approximate nearest neighbor
search under \\(X\\). This can be seen as a strengthening of the classic
(bi-Lipschitz) embedding approach to nearest neighbor search, and is another
application of data-dependent hashing paradigm.
