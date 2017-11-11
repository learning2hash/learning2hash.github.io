---
layout: publication
title: "Multidimensional Spectral Hashing"
authors: Y. Weiss, R. Fergus, A. Torralba
conference: ECCV
year: 2012
bibkey: weiss2012multi
additional_links:
   - {name: "PDF", url: "http://people.csail.mit.edu/torralba/publications/msh_eccv12.pdf"}
   - {name: "Supplementary PDF", url: "http://www.cs.huji.ac.il/~yweiss/hashingWithKernelTrick.pdf
"}
   - {name: "Code", url: "http://www.cs.huji.ac.il/~yweiss/export2.tar"}
---
en a surge of interest in methods based on “semantic hashing”,
i.e. compact binary codes of data-points so that the Hamming distance
between codewords correlates with similarity. In reviewing and
comparing existing methods, we show that their relative performance can
change drastically depending on the definition of ground-truth neighbors.
Motivated by this finding, we propose a new formulation for learning binary
codes which seeks to reconstruct the affinity between datapoints,
rather than their distances. We show that this criterion is intractable
to solve exactly, but a spectral relaxation gives an algorithm where the
bits correspond to thresholded eigenvectors of the affinity matrix, and
as the number of datapoints goes to infinity these eigenvectors converge
to eigenfunctions of Laplace-Beltrami operators, similar to the recently
proposed Spectral Hashing (SH) method. Unlike SH whose performance
may degrade as the number of bits increases, the optimal code using
our formulation is guaranteed to faithfully reproduce the affinities as
the number of bits increases. We show that the number of eigenfunctions
needed may increase exponentially with dimension, but introduce a “kernel
trick” to allow us to compute with an exponentially large number of
bits but using only memory and computation that grows linearly with
dimension. Experiments shows that MDSH outperforms the state-of-the
art, especially in the challenging regime of small distance thresholds.
