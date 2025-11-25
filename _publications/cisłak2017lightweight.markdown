---
layout: publication
title: Lightweight Fingerprints For Fast Approximate Keyword Matching Using Bitwise
  Operations
authors: "Aleksander Cis\u0142ak, Szymon Grabowski"
conference: Arxiv
year: 2017
bibkey: "cis\u0142ak2017lightweight"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.08475'}]
tags: ["Efficiency", "Hashing Methods", "Similarity Search"]
short_authors: "Aleksander Cis\u0142ak, Szymon Grabowski"
---
We aim to speed up approximate keyword matching by storing a lightweight,
fixed-size block of data for each string, called a fingerprint. These work in a
similar way to hash values; however, they can be also used for matching with
errors. They store information regarding symbol occurrences using individual
bits, and they can be compared against each other with a constant number of
bitwise operations. In this way, certain strings can be deduced to be at least
within the distance \(k\) from each other (using Hamming or Levenshtein distance)
without performing an explicit verification. We show experimentally that for a
preprocessed collection of strings, fingerprints can provide substantial
speedups for \(k = 1\), namely over \(2.5\) times for the Hamming distance and over
\(10\) times for the Levenshtein distance. Tests were conducted on synthetic and
real-world English and URL data.