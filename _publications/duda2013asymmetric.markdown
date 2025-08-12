---
layout: publication
title: 'Asymmetric Numeral Systems: Entropy Coding Combining Speed Of Huffman Coding
  With Compression Rate Of Arithmetic Coding'
authors: Jarek Duda
conference: Arxiv
year: 2013
bibkey: duda2013asymmetric
citations: 125
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1311.2540'}]
tags: ["Efficiency", "Memory Efficiency"]
short_authors: Jarek Duda
---
The modern data compression is mainly based on two approaches to entropy
coding: Huffman (HC) and arithmetic/range coding (AC). The former is much
faster, but approximates probabilities with powers of 2, usually leading to
relatively low compression rates. The latter uses nearly exact probabilities -
easily approaching theoretical compression rate limit (Shannon entropy), but at
cost of much larger computational cost.
  Asymmetric numeral systems (ANS) is a new approach to accurate entropy
coding, which allows to end this trade-off between speed and rate: the recent
implementation [1] provides about \(50%\) faster decoding than HC for 256 size
alphabet, with compression rate similar to provided by AC. This advantage is
due to being simpler than AC: using single natural number as the state, instead
of two to represent a range. Beside simplifying renormalization, it allows to
put the entire behavior for given probability distribution into a relatively
small table: defining entropy coding automaton. The memory cost of such table
for 256 size alphabet is a few kilobytes. There is a large freedom while
choosing a specific table - using pseudorandom number generator initialized
with cryptographic key for this purpose allows to simultaneously encrypt the
data.
  This article also introduces and discusses many other variants of this new
entropy coding approach, which can provide direct alternatives for standard AC,
for large alphabet range coding, or for approximated quasi arithmetic coding.