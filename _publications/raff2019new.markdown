---
layout: publication
title: A New Burrows Wheeler Transform Markov Distance
authors: Edward Raff, Charles Nicholas, Mark Mclean
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2020
bibkey: raff2019new
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.13046'}]
tags: ["AAAI", "Distance Metric Learning"]
short_authors: Edward Raff, Charles Nicholas, Mark Mclean
---
Prior work inspired by compression algorithms has described how the Burrows
Wheeler Transform can be used to create a distance measure for bioinformatics
problems. We describe issues with this approach that were not widely known, and
introduce our new Burrows Wheeler Markov Distance (BWMD) as an alternative. The
BWMD avoids the shortcomings of earlier efforts, and allows us to tackle
problems in variable length DNA sequence clustering. BWMD is also more
adaptable to other domains, which we demonstrate on malware classification
tasks. Unlike other compression-based distance metrics known to us, BWMD works
by embedding sequences into a fixed-length feature vector. This allows us to
provide significantly improved clustering performance on larger malware
corpora, a weakness of prior methods.