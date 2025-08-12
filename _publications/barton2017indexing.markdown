---
layout: publication
title: 'Indexing Weighted Sequences: Neat And Efficient'
authors: Carl Barton, Tomasz Kociumaka, Chang Liu, Solon P. Pissis, Jakub Radoszewski
conference: Information and Computation
year: 2019
bibkey: barton2017indexing
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.07625'}]
tags: ["Efficiency"]
short_authors: Barton et al.
---
In a *weighted sequence*, for every position of the sequence and every
letter of the alphabet a probability of occurrence of this letter at this
position is specified. Weighted sequences are commonly used to represent
imprecise or uncertain data, for example, in molecular biology where they are
known under the name of Position-Weight Matrices. Given a probability threshold
\\(\frac1z\\), we say that a string \\(P\\) of length \\(m\\) occurs in a weighted sequence
\\(X\\) at position \\(i\\) if the product of probabilities of the letters of \\(P\\) at
positions \\(i,\ldots,i+m-1\\) in \\(X\\) is at least \\(\frac1z\\). In this article, we
consider an *indexing* variant of the problem, in which we are to
preprocess a weighted sequence to answer multiple pattern matching queries. We
present an \\(O(nz)\\)-time construction of an \\(O(nz)\\)-sized index for a weighted
sequence of length \\(n\\) over a constant-sized alphabet that answers pattern
matching queries in optimal, \\(O(m+Occ)\\) time, where \\(Occ\\) is the number of
occurrences reported. The cornerstone of our data structure is a novel
construction of a family of \\(\lfloor z \rfloor\\) special strings that carries
the information about all the strings that occur in the weighted sequence with
a sufficient probability. We obtain a weighted index with the same complexities
as in the most efficient previously known index by Barton et al. (CPM 2016),
but our construction is significantly simpler. The most complex algorithmic
tool required in the basic form of our index is the suffix tree which we use to
develop a new, more straightforward index for the so-called property matching
problem. We provide an implementation of our data structure. Our construction
allows us also to obtain a significant improvement over the complexities of the
approximate variant of the weighted index presented by Biswas et al. (EDBT
2016) and an improvement of the space complexity of their general index.