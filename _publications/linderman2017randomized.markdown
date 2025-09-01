---
layout: publication
title: Randomized Near Neighbor Graphs, Giant Components, And Applications In Data
  Science
authors: George C. Linderman, Gal Mishne, Yuval Kluger, Stefan Steinerberger
conference: Journal of Applied Probability
year: 2020
bibkey: linderman2017randomized
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.04712'}]
tags: ["Efficiency"]
short_authors: Linderman et al.
---
If we pick \(n\) random points uniformly in \([0,1]^d\) and connect each point to
its \(k-\)nearest neighbors, then it is well known that there exists a giant
connected component with high probability. We prove that in \([0,1]^d\) it
suffices to connect every point to \( c_\{d,1\} log\{log\{n\}\}\) points chosen
randomly among its \( c_\{d,2\} log\{n\}-\)nearest neighbors to ensure a giant
component of size \(n - o(n)\) with high probability. This construction yields a
much sparser random graph with \(\sim n loglog\{n\}\) instead of \(\sim n log\{n\}\)
edges that has comparable connectivity properties. This result has nontrivial
implications for problems in data science where an affinity matrix is
constructed: instead of picking the \(k-\)nearest neighbors, one can often pick
\(k' \ll k\) random points out of the \(k-\)nearest neighbors without sacrificing
efficiency. This can massively simplify and accelerate computation, we
illustrate this with several numerical examples.