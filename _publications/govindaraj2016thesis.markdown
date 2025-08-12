---
layout: publication
title: 'Thesis: Multiple Kernel Learning For Object Categorization'
authors: Dinesh Govindaraj
conference: Arxiv
year: 2016
bibkey: govindaraj2016thesis
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.03247'}]
tags: []
short_authors: Dinesh Govindaraj
---
Object Categorization is a challenging problem, especially when the images
have clutter background, occlusions or different lighting conditions. In the
past, many descriptors have been proposed which aid object categorization even
in such adverse conditions. Each descriptor has its own merits and de-merits.
Some descriptors are invariant to transformations while the others are more
discriminative. Past research has shown that, employing multiple descriptors
rather than any single descriptor leads to better recognition. The problem of
learning the optimal combination of the available descriptors for a particular
classification task is studied. Multiple Kernel Learning (MKL) framework has
been developed for learning an optimal combination of descriptors for object
categorization. Existing MKL formulations often employ block l-1 norm
regularization which is equivalent to selecting a single kernel from a library
of kernels. Since essentially a single descriptor is selected, the existing
formulations maybe sub- optimal for object categorization. A MKL formulation
based on block l-infinity norm regularization has been developed, which chooses
an optimal combination of kernels as opposed to selecting a single kernel. A
Composite Multiple Kernel Learning(CKL) formulation based on mixed l-infinity
and l-1 norm regularization has been developed. These formulations end in
Second Order Cone Programs(SOCP). Other efficient alter- native algorithms for
these formulation have been implemented. Empirical results on benchmark
datasets show significant improvement using these new MKL formulations.