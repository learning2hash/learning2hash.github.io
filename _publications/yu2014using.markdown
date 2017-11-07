---
layout: publication
title: "Circulant Binary Embedding"
authors: F. Yu, S. Kumar, Y. Gong, S. Chang
conference: ICML
year: 2014
bibkey: yu2014using
additional_links:
   - {name: "PDF", url: "http://www.ee.columbia.edu/ln/dvmm/publications/14/yu2014_cbe.pdf"}
   - {name: "Code", url: "https://github.com/felixyu/cbe"}
---
Binary embedding of high-dimensional data requires
long codes to preserve the discriminative
power of the input space. Traditional binary coding
methods often suffer from very high computation
and storage costs in such a scenario. To
address this problem, we propose Circulant Binary
Embedding (CBE) which generates binary
codes by projecting the data with a circulant matrix.
The circulant structure enables the use of
Fast Fourier Transformation to speed up the computation.
Compared to methods that use unstructured
matrices, the proposed method improves
the time complexity from O(d^2
) to O(d log d),
and the space complexity from O(d^2) to O(d)
where d is the input dimensionality. We also
propose a novel time-frequency alternating optimization
to learn data-dependent circulant projections,
which alternatively minimizes the objective
in original and Fourier domains. We show
by extensive experiments that the proposed approach
gives much better performance than the
state-of-the-art approaches for fixed time, and
provides much faster computation with no performance
degradation for fixed number of bits.
