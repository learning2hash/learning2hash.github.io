---
layout: publication
title: b-bit Sketch Trie Scalable Similarity Search On Integer Sketches
authors: Kanda Shunsuke, Tabei Yasuo
conference: "Arxiv"
year: 2019
bibkey: kanda2019b
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1910.08278"}
tags: ['ARXIV', 'Independent']
---
Recently, randomly mapping vectorial data to strings of discrete symbols
(i.e., sketches) for fast and space-efficient similarity searches has become
popular. Such random mapping is called similarity-preserving hashing and
approximates a similarity metric by using the Hamming distance. Although many
efficient similarity searches have been proposed, most of them are designed for
binary sketches. Similarity searches on integer sketches are in their infancy.
In this paper, we present a novel space-efficient trie named \{b\}-bit sketch
trie on integer sketches for scalable similarity searches by leveraging the
idea behind succinct data structures (i.e., space-efficient data structures
while supporting various data operations in the compressed format) and a
favorable property of integer sketches as fixed-length strings. Our
experimental results obtained using real-world datasets show that a trie-based
index is built from integer sketches and efficiently performs similarity
searches on the index by pruning useless portions of the search space, which
greatly improves the search time and space-efficiency of the similarity search.
The experimental results show that our similarity search is at most one order
of magnitude faster than state-of-the-art similarity searches. Besides, our
method needs only 10 GiB of memory on a billion-scale database, while
state-of-the-art similarity searches need 29 GiB of memory.
