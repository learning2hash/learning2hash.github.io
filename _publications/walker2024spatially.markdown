---
layout: publication
title: Spatially-adaptive Hash Encodings For Neural Surface Reconstruction
authors: Thomas Walker, Octave Mariotti, Amir Vaxman, Hakan Bilen
conference: Arxiv
year: 2024
bibkey: walker2024spatially
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.05179'}]
tags: []
short_authors: Walker et al.
---
Positional encodings are a common component of neural scene reconstruction
methods, and provide a way to bias the learning of neural fields towards
coarser or finer representations. Current neural surface reconstruction methods
use a "one-size-fits-all" approach to encoding, choosing a fixed set of
encoding functions, and therefore bias, across all scenes. Current
state-of-the-art surface reconstruction approaches leverage grid-based
multi-resolution hash encoding in order to recover high-detail geometry. We
propose a learned approach which allows the network to choose its encoding
basis as a function of space, by masking the contribution of features stored at
separate grid resolutions. The resulting spatially adaptive approach allows the
network to fit a wider range of frequencies without introducing noise. We test
our approach on standard benchmark surface reconstruction datasets and achieve
state-of-the-art performance on two benchmark datasets.