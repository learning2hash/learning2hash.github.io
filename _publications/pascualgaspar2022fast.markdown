---
layout: publication
title: Fast On-line Signature Recognition Based On VQ With Time Modeling
authors: Juan-Manuel Pascual-Gaspar, Marcos Faundez-Zanuy, Carlos Vivaracho
conference: Engineering Applications of Artificial Intelligence
year: 2022
bibkey: pascualgaspar2022fast
citations: 42
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.12104'}]
tags: [Quantization]
short_authors: Juan-Manuel Pascual-Gaspar, Marcos Faundez-Zanuy, Carlos Vivaracho
---
This paper proposes a multi-section vector quantization approach for on-line
signature recognition. We have used the MCYT database, which consists of 330
users and 25 skilled forgeries per person performed by 5 different impostors.
This database is larger than those typically used in the literature.
Nevertheless, we also provide results from the SVC database.
  Our proposed system outperforms the winner of SVC with a reduced
computational requirement, which is around 47 times lower than DTW. In
addition, our system improves the database storage requirements due to vector
compression, and is more privacy-friendly as it is not possible to recover the
original signature using the codebooks. Experimental results with MCYT provide
a 99.76% identification rate and 2.46% EER (skilled forgeries and individual
threshold). Experimental results with SVC are 100% of identification rate and
0% (individual threshold) and 0.31% (general threshold) when using a
two-section VQ approach.