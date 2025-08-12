---
layout: publication
title: Fast Low-level Pattern Matching Algorithm
authors: Janja Paliska Soldo, Ana Sovic Krzic, And Damir Sersic
conference: Arxiv
year: 2016
bibkey: soldo2016fast
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.06115'}]
tags: []
short_authors: Janja Paliska Soldo, Ana Sovic Krzic, And Damir Sersic
---
This paper focuses on pattern matching in the DNA sequence. It was inspired
by a previously reported method that proposes encoding both pattern and
sequence using prime numbers. Although fast, the method is limited to rather
small pattern lengths, due to computing precision problem. Our approach
successfully deals with large patterns, due to our implementation that uses
modular arithmetic. In order to get the results very fast, the code was adapted
for multithreading and parallel implementations. The method is reduced to
assembly language level instructions, thus the final result shows significant
time and memory savings compared to the reference algorithm.