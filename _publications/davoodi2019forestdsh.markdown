---
layout: publication
title: Forestdsh A Universal Hash Design For Discrete Probability Distributions
authors: Davoodi Arash Gholami et al.
conference: DAMI
year: 2019
citations: 0
bibkey: davoodi2019forestdsh
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.04559'}]
tags: [LSH, Supervised]
---
In this paper, we consider the problem of classification of \\(M\\) high
dimensional queries \\(y^1,\cdots,y^M\in B^S\\) to \\(N\\) high dimensional classes
\\(x^1,\cdots,x^N\in A^S\\) where \\(A\\) and \\(B\\) are discrete alphabets and the
probabilistic model that relates data to the classes \\(P(x,y)\\) is known. This
problem has applications in various fields including the database search
problem in mass spectrometry. The problem is analogous to the nearest neighbor
search problem, where the goal is to find the data point in a database that is
the most similar to a query point. The state of the art method for solving an
approximate version of the nearest neighbor search problem in high dimensions
is locality sensitive hashing (LSH). LSH is based on designing hash functions
that map near points to the same buckets with a probability higher than random
(far) points. To solve our high dimensional classification problem, we
introduce distribution sensitive hashes that map jointly generated pairs
\\((x,y)\sim P\\) to the same bucket with probability higher than random pairs
\\(x\sim P^A\\) and \\(y\sim P^B\\), where \\(P^A\\) and \\(P^B\\) are the marginal probability
distributions of \\(P\\). We design distribution sensitive hashes using a forest of
decision trees and we show that the complexity of search grows with
\\(O(N^\{\lambda^*(P)\})\\) where \\(\lambda^*(P)\\) is expressed in an analytical form.
We further show that the proposed hashes perform faster than state of the art
approximate nearest neighbor search methods for a range of probability
distributions, in both theory and simulations. Finally, we apply our method to
the spectral library search problem in mass spectrometry, and show that it is
an order of magnitude faster than the state of the art methods.