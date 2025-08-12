---
layout: publication
title: Faster Dynamic Compressed D-ary Relations
authors: Diego Arroyuelo, Guillermo de Bernardo, Travis Gagie, Gonzalo Navarro
conference: Lecture Notes in Computer Science
year: 2019
bibkey: arroyuelo2019faster
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.08971'}]
tags: []
short_authors: Arroyuelo et al.
---
The \(k^2\)-tree is a successful compact representation of binary relations
that exhibit sparseness and/or clustering properties. It can be extended to \(d\)
dimensions, where it is called a \(k^d\)-tree. The representation boils down to a
long bitvector. We show that interpreting the \(k^d\)-tree as a dynamic trie on
the Morton codes of the points, instead of as a dynamic representation of the
bitvector as done in previous work, yields operation times that are below the
lower bound of dynamic bitvectors and offers improved time performance in
practice.