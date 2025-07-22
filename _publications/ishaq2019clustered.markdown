---
layout: publication
title: Clustered Hierarchical Entropy-scaling Search Of Astronomical And Biological
  Data
authors: Ishaq Najib, Student George, Daniels Noah M.
conference: 2019 IEEE International Conference on Big Data (Big Data)
year: 2019
bibkey: ishaq2019clustered
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.08551'}]
tags: ["Efficiency", "Tools-&-Libraries", "Hashing-Methods", "Survey-Paper"]
short_authors: Ishaq Najib, Student George, Daniels Noah M.
---
Both astronomy and biology are experiencing explosive growth of data,
resulting in a "big data" problem that stands in the way of a "big data"
opportunity for discovery. One common question asked of such data is that of
approximate search (\\(\rho-\\)nearest neighbors search). We present a hierarchical
search algorithm for such data sets that takes advantage of particular
geometric properties apparent in both astronomical and biological data sets,
namely the metric entropy and fractal dimensionality of the data. We present
CHESS (Clustered Hierarchical Entropy-Scaling Search), a search tool with
virtually no loss in specificity or sensitivity, demonstrating a \\(13.6\times\\)
speedup over linear search on the Sloan Digital Sky Survey's APOGEE data set
and a \\(68\times\\) speedup on the GreenGenes 16S metagenomic data set, as well as
asymptotically fewer distance comparisons on APOGEE when compared to the
FALCONN locality-sensitive hashing library. CHESS demonstrates an asymptotic
complexity not directly dependent on data set size, and is in practice at least
an order of magnitude faster than linear search by performing fewer distance
comparisons. Unlike locality-sensitive hashing approaches, CHESS can work with
any user-defined distance function. CHESS also allows for implicit data
compression, which we demonstrate on the APOGEE data set. We also discuss an
extension allowing for efficient k-nearest neighbors search.