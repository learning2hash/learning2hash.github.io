---
layout: publication
title: Parallel Implementations For Computing The Minimum Distance Of A Random Linear
  Code On Multicomputers
authors: "Gregorio Quintana-Ort\xED, Fernando Hernando, Francisco D. Igual"
conference: Arxiv
year: 2019
bibkey: "quintanaort\xED2019parallel"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.08963'}]
tags: ["Distance Metric Learning", "Efficiency", "Scalability"]
short_authors: "Gregorio Quintana-Ort\xED, Fernando Hernando, Francisco D. Igual"
---
The minimum distance of a linear code is a key concept in information theory.
Therefore, the time required by its computation is very important to many
problems in this area. In this paper, we introduce a family of implementations
of the Brouwer-Zimmermann algorithm for distributed-memory architectures for
computing the minimum distance of a random linear code over F2. Both current
commercial and public-domain software only work on either unicore architectures
or shared-memory architectures, which are limited in the number of
cores/processors employed in the computation. Our implementations focus on
distributed-memory architectures, thus being able to employ hundreds or even
thousands of cores in the computation of the minimum distance. Our experimental
results show that our implementations are much faster, even up to several
orders of magnitude, than current implementations widely used nowadays.