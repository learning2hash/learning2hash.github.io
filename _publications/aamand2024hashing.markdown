---
layout: publication
title: 'Hashing For Sampling-based Estimation'
authors: Anders Aamand, Ioana O. Bercea, Jakob Bæk Tejs Houen, Jonas Klausen, Mikkel Thorup
conference: "Arxiv"
year: 2024
citations: 0
bibkey: aamand2024hashing
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2411.19394'}
tags: ['Unsupervised', 'Cross-Modal', 'Shallow', 'Hashing']
---
Hash-based sampling and estimation are common themes in computing. Using
hashing for sampling gives us the coordination needed to compare samples from
different sets. Hashing is also used when we want to count distinct elements.
The quality of the estimator for, say, the Jaccard similarity between two sets,
depends on the concentration of the number of sampled elements from their
intersection. Often we want to compare one query set against many stored sets
to find one of the most similar sets, so we need strong concentration and low
error-probability. In this paper, we provide strong explicit concentration
bounds for Tornado Tabulation hashing [Bercea, Beretta, Klausen, Houen, and
Thorup, FOCS'23] which is a realistic constant time hashing scheme. Previous
concentration bounds for fast hashing were off by orders of magnitude, in the
sample size needed to guarantee the same concentration. The true power of our
result appears when applied in the local uniformity framework by [Dahlgaard,
Knudsen, Rotenberg, and Thorup, STOC'15].
