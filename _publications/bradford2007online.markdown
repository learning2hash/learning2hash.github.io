---
layout: publication
title: An Online Algorithm For Generating Fractal Hash Chains Applied To Digital Chains
  Of Custody
authors: Phillip G. Bradford, Daniel A. Ray
conference: Arxiv
year: 2007
bibkey: bradford2007online
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/0705.2876'}]
tags: ["Hashing Methods"]
short_authors: Phillip G. Bradford, Daniel A. Ray
---
This paper gives an online algorithm for generating Jakobsson's fractal hash
chains. Our new algorithm compliments Jakobsson's fractal hash chain algorithm
for preimage traversal since his algorithm assumes the entire hash chain is
precomputed and a particular list of Ceiling(log n) hash elements or pebbles
are saved. Our online algorithm for hash chain traversal incrementally
generates a hash chain of n hash elements without knowledge of n before it
starts. For any n, our algorithm stores only the Ceiling(log n) pebbles which
are precisely the inputs for Jakobsson's amortized hash chain preimage
traversal algorithm. This compact representation is useful to generate,
traverse, and store a number of large digital hash chains on a small and
constrained device. We also give an application using both Jakobsson's and our
new algorithm applied to digital chains of custody for validating dynamically
changing forensics data.