---
layout: publication
title: An Approximate Algorithm For Maximum Inner Product Search Over Streaming Sparse
  Vectors
authors: Sebastian Bruch, Franco Maria Nardini, Amir Ingber, Edo Liberty
conference: ACM Transactions on Information Systems
year: 2023
bibkey: bruch2023an
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.10622'}]
tags: ["Evaluation", "Memory Efficiency", "Similarity Search"]
short_authors: Bruch et al.
---
Maximum Inner Product Search or top-k retrieval on sparse vectors is
well-understood in information retrieval, with a number of mature algorithms
that solve it exactly. However, all existing algorithms are tailored to text
and frequency-based similarity measures. To achieve optimal memory footprint
and query latency, they rely on the near stationarity of documents and on laws
governing natural languages. We consider, instead, a setup in which collections
are streaming -- necessitating dynamic indexing -- and where indexing and
retrieval must work with arbitrarily distributed real-valued vectors. As we
show, existing algorithms are no longer competitive in this setup, even against
naive solutions. We investigate this gap and present a novel approximate
solution, called Sinnamon, that can efficiently retrieve the top-k results for
sparse real valued vectors drawn from arbitrary distributions. Notably,
Sinnamon offers levers to trade-off memory consumption, latency, and accuracy,
making the algorithm suitable for constrained applications and systems. We give
theoretical results on the error introduced by the approximate nature of the
algorithm, and present an empirical evaluation of its performance on two
hardware platforms and synthetic and real-valued datasets. We conclude by
laying out concrete directions for future research on this general top-k
retrieval problem over sparse vectors.