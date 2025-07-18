---
layout: publication
title: High-dimensional Simplexes For Supermetric Search
authors: Connor Richard, Vadicamo Lucia, Rabitti Fausto
conference: Lecture Notes in Computer Science
year: 2017
bibkey: connor2017high
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.08370'}]
tags: [Alt, Similarity Search, Evaluation]
---
In 1953, Blumenthal showed that every semi-metric space that is isometrically
embeddable in a Hilbert space has the n-point property; we have previously
called such spaces supermetric spaces. Although this is a strictly stronger
property than triangle inequality, it is nonetheless closely related and many
useful metric spaces possess it. These include Euclidean, Cosine and
Jensen-Shannon spaces of any dimension. A simple corollary of the n-point
property is that, for any (n+1) objects sampled from the space, there exists an
n-dimensional simplex in Euclidean space whose edge lengths correspond to the
distances among the objects. We show how the construction of such simplexes in
higher dimensions can be used to give arbitrarily tight lower and upper bounds
on distances within the original space. This allows the construction of an
n-dimensional Euclidean space, from which lower and upper bounds of the
original space can be calculated, and which is itself an indexable space with
the n-point property. For similarity search, the engineering tradeoffs are
good: we show significant reductions in data size and metric cost with little
loss of accuracy, leading to a significant overall improvement in search
performance.