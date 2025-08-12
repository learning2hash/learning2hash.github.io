---
layout: publication
title: Fast Low-rank Shared Dictionary Learning For Image Classification
authors: Tiep Vu, Vishal Monga
conference: IEEE Transactions on Image Processing
year: 2017
bibkey: vu2016fast
citations: 183
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.08606'}]
tags: []
short_authors: Tiep Vu, Vishal Monga
---
Despite the fact that different objects possess distinct class-specific
features, they also usually share common patterns. This observation has been
exploited partially in a recently proposed dictionary learning framework by
separating the particularity and the commonality (COPAR). Inspired by this, we
propose a novel method to explicitly and simultaneously learn a set of common
patterns as well as class-specific features for classification with more
intuitive constraints. Our dictionary learning framework is hence characterized
by both a shared dictionary and particular (class-specific) dictionaries. For
the shared dictionary, we enforce a low-rank constraint, i.e. claim that its
spanning subspace should have low dimension and the coefficients corresponding
to this dictionary should be similar. For the particular dictionaries, we
impose on them the well-known constraints stated in the Fisher discrimination
dictionary learning (FDDL). Further, we develop new fast and accurate
algorithms to solve the subproblems in the learning step, accelerating its
convergence. The said algorithms could also be applied to FDDL and its
extensions. The efficiencies of these algorithms are theoretically and
experimentally verified by comparing their complexities and running time with
those of other well-known dictionary learning methods. Experimental results on
widely used image datasets establish the advantages of our method over
state-of-the-art dictionary learning methods.