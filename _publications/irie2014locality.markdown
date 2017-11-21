---
layout: publication
title: "Locally Linear Hashing for Extracting Non-Linear Manifolds"
authors: G. Irie, Z. Li, X. Wu, S. Chang 
conference: CVPR
year: 2014
bibkey: irie2014locality
additional_links:
   - {name: "PDF", url: "http://www.ee.columbia.edu/~zgli/papers/CVPR-2014-LLH.pdf"}
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