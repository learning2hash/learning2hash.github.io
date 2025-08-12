---
layout: publication
title: Efficient Tree-structured Categorical Retrieval
authors: Djamal Belazzougui, Gregory Kucherov
conference: Arxiv
year: 2020
bibkey: belazzougui2020efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.01825'}]
tags: ["Efficiency", "Text Retrieval"]
short_authors: Djamal Belazzougui, Gregory Kucherov
---
We study a document retrieval problem in the new framework where \(D\) text
documents are organized in a \{\em category tree\} with a pre-defined number \(h\)
of categories. This situation occurs e.g. with taxomonic trees in biology or
subject classification systems for scientific literature. Given a string
pattern \(p\) and a category (level in the category tree), we wish to efficiently
retrieve the \(t\) *categorical units* containing this pattern and belonging
to the category. We propose several efficient solutions for this problem. One
of them uses \(n(log\sigma(1+o(1))+log D+O(h)) + O(\Delta)\) bits of space and
\(O(|p|+t)\) query time, where \(n\) is the total length of the documents, \(\sigma\)
the size of the alphabet used in the documents and \(\Delta\) is the total number
of nodes in the category tree. Another solution uses
\(n(log\sigma(1+o(1))+O(log D))+O(\Delta)+O(Dlog n)\) bits of space and
\(O(|p|+tlog D)\) query time. We finally propose other solutions which are more
space-efficient at the expense of a slight increase in query time.