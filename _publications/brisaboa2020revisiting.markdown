---
layout: publication
title: Revisiting Compact RDF Stores Based On K2-trees
authors: "Nieves R. Brisaboa, Ana Cerdeira-Pena, Guillermo de Bernardo, Antonio Fari\xF1\
  a"
conference: 2020 Data Compression Conference (DCC)
year: 2020
bibkey: brisaboa2020revisiting
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.11622'}]
tags: ["Efficiency"]
short_authors: Brisaboa et al.
---
We present a new compact representation to efficiently store and query large
RDF datasets in main memory. Our proposal, called BMatrix, is based on the
k2-tree, a data structure devised to represent binary matrices in a compressed
way, and aims at improving the results of previous state-of-the-art
alternatives, especially in datasets with a relatively large number of
predicates. We introduce our technique, together with some improvements on the
basic k2-tree that can be applied to our solution in order to boost
compression. Experimental results in the flagship RDF dataset DBPedia show that
our proposal achieves better compression than existing alternatives, while
yielding competitive query times, particularly in the most frequent triple
patterns and in queries with unbound predicate, in which we outperform existing
solutions.