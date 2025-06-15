---
layout: publication
title: 'Sequential Hypothesis Tests For Adaptive Locality Sensitive Hashing'
authors: Aniket Chakrabarti, Srinivasan Parthasarathy
conference: "Arxiv"
year: 2014
citations: 8
bibkey: chakrabarti2014sequential
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1412.3103'}
tags: ['Independent', 'Efficiency', 'Unimodal', 'Retrieval Models', 'Shallow', 'Hashing']
---
All pairs similarity search is a problem where a set of data objects is given
and the task is to find all pairs of objects that have similarity above a
certain threshold for a given similarity measure-of-interest. When the number
of points or dimensionality is high, standard solutions fail to scale
gracefully. Approximate solutions such as Locality Sensitive Hashing (LSH) and
its Bayesian variants (BayesLSH and BayesLSHLite) alleviate the problem to some
extent and provides substantial speedup over traditional index based
approaches. BayesLSH is used for pruning the candidate space and computation of
approximate similarity, whereas BayesLSHLite can only prune the candidates, but
similarity needs to be computed exactly on the original data. Thus where ever
the explicit data representation is available and exact similarity computation
is not too expensive, BayesLSHLite can be used to aggressively prune candidates
and provide substantial speedup without losing too much on quality. However,
the loss in quality is higher in the BayesLSH variant, where explicit data
representation is not available, rather only a hash sketch is available and
similarity has to be estimated approximately. In this work we revisit the LSH
problem from a Frequentist setting and formulate sequential tests for composite
hypothesis (similarity greater than or less than threshold) that can be
leveraged by such LSH algorithms for adaptively pruning candidates
aggressively. We propose a vanilla sequential probability ration test (SPRT)
approach based on this idea and two novel variants. We extend these variants to
the case where approximate similarity needs to be computed using fixed-width
sequential confidence interval generation technique.
