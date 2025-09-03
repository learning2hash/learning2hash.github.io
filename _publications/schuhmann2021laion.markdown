---
layout: publication
title: 'LAION-400M: Open Dataset Of Clip-filtered 400 Million Image-text Pairs'
authors: Christoph Schuhmann, Richard Vencu, Romain Beaumont, Robert Kaczmarczyk,
  Clayton Mullis, Aarush Katta, Theo Coombes, Jenia Jitsev, Aran Komatsuzaki
conference: Arxiv
year: 2021
bibkey: schuhmann2021laion
citations: 323
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.02114'}]
tags: ["Datasets", "Few Shot & Zero Shot", "Similarity Search"]
short_authors: Schuhmann et al.
---
Multi-modal language-vision models trained on hundreds of millions of
image-text pairs (e.g. CLIP, DALL-E) gained a recent surge, showing remarkable
capability to perform zero- or few-shot learning and transfer even in absence
of per-sample labels on target image data. Despite this trend, to date there
has been no publicly available datasets of sufficient scale for training such
models from scratch. To address this issue, in a community effort we build and
release for public LAION-400M, a dataset with CLIP-filtered 400 million
image-text pairs, their CLIP embeddings and kNN indices that allow efficient
similarity search.