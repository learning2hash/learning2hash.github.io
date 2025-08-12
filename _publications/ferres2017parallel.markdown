---
layout: publication
title: Parallel Construction Of Compact Planar Embeddings
authors: "Leo Ferres, Jos\xE9 Fuentes-Sep\xFAlveda, Travis Gagie, Meng He, Gonzalo\
  \ Navarro"
conference: Arxiv
year: 2017
bibkey: ferres2017parallel
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.00415'}]
tags: []
short_authors: Ferres et al.
---
The sheer sizes of modern datasets are forcing data-structure designers to
consider seriously both parallel construction and compactness. To achieve those
goals we need to design a parallel algorithm with good scalability and with low
memory consumption. An algorithm with good scalability improves its performance
when the number of available cores increases, and an algorithm with low memory
consumption uses memory proportional to the space used by the dataset in
uncompact form. In this work, we discuss the engineering of a parallel
algorithm with linear work and logarithmic span for the construction of the
compact representation of planar embeddings. We also provide an experimental
study of our implementation and prove experimentally that it has good
scalability and low memory consumption. Additionally, we describe and test
experimentally queries supported by the compact representation.