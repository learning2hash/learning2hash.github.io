---
layout: publication
title: 'Swivel: Improving Embeddings By Noticing What''s Missing'
authors: Noam Shazeer, Ryan Doherty, Colin Evans, Chris Waterson
conference: Arxiv
year: 2016
bibkey: shazeer2016swivel
citations: 56
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.02215'}]
tags: [Uncategorized]
short_authors: Shazeer et al.
---
We present Submatrix-wise Vector Embedding Learner (Swivel), a method for
generating low-dimensional feature embeddings from a feature co-occurrence
matrix. Swivel performs approximate factorization of the point-wise mutual
information matrix via stochastic gradient descent. It uses a piecewise loss
with special handling for unobserved co-occurrences, and thus makes use of all
the information in the matrix. While this requires computation proportional to
the size of the entire matrix, we make use of vectorized multiplication to
process thousands of rows and columns at once to compute millions of predicted
values. Furthermore, we partition the matrix into shards in order to
parallelize the computation across many nodes. This approach results in more
accurate embeddings than can be achieved with methods that consider only
observed co-occurrences, and can scale to much larger corpora than can be
handled with sampling methods.