---
layout: publication
title: Locally Linear Hashing for Extracting Non-Linear Manifolds
authors: Irie G., Li, Wu, Chang
conference: 2014 IEEE Conference on Computer Vision and Pattern Recognition
year: 2014
bibkey: irie2025locally
citations: 94
additional_links: [{name: Paper, url: 'http://www.ee.columbia.edu/~zgli/papers/CVPR-2014-LLH.pdf'}]
tags: ["Hashing-Methods", "Quantization", "CVPR"]
short_authors: Irie et al.
---
Previous efforts in hashing intend to preserve data variance
or pairwise affinity, but neither is adequate in capturing
the manifold structures hidden in most visual data. In
this paper, we tackle this problem by reconstructing the locally
linear structures of manifolds in the binary Hamming
space, which can be learned by locality-sensitive sparse
coding. We cast the problem as a joint minimization of
reconstruction error and quantization loss, and show that,
despite its NP-hardness, a local optimum can be obtained
efficiently via alternative optimization. Our method distinguishes
itself from existing methods in its remarkable ability
to extract the nearest neighbors of the query from the
same manifold, instead of from the ambient space. On extensive
experiments on various image benchmarks, our results
improve previous state-of-the-art by 28-74% typically,
and 627% on the Yale face data.