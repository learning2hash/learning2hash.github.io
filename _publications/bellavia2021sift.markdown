---
layout: publication
title: SIFT Matching By Context Exposed
authors: Fabio Bellavia
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2022
bibkey: bellavia2021sift
citations: 41
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.09584'}]
tags: []
short_authors: Fabio Bellavia
---
This paper investigates how to step up local image descriptor matching by
exploiting matching context information. Two main contexts are identified,
originated respectively from the descriptor space and from the keypoint space.
The former is generally used to design the actual matching strategy while the
latter to filter matches according to the local spatial consistency. On this
basis, a new matching strategy and a novel local spatial filter, named
respectively blob matching and Delaunay Triangulation Matching (DTM) are
devised. Blob matching provides a general matching framework by merging
together several strategies, including rank-based pre-filtering as well as
many-to-many and symmetric matching, enabling to achieve a global improvement
upon each individual strategy. DTM alternates between Delaunay triangulation
contractions and expansions to figure out and adjust keypoint neighborhood
consistency. Experimental evaluation shows that DTM is comparable or better
than the state-of-the-art in terms of matching accuracy and robustness.
Evaluation is carried out according to a new benchmark devised for analyzing
the matching pipeline in terms of correct correspondences on both planar and
non-planar scenes, including several state-of-the-art methods as well as the
common SIFT matching approach for reference. This evaluation can be of
assistance for future research in this field.