---
layout: publication
title: 'Fmtree: A Fast Locating Algorithm Of Fm-indexes For Genomic Data'
authors: Haoyu Cheng, Ming Wu, Yun Xu
conference: Bioinformatics
year: 2017
bibkey: cheng2017fmtree
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.04615'}]
tags: ["Evaluation"]
short_authors: Haoyu Cheng, Ming Wu, Yun Xu
---
Motivation: As a fundamental task in bioinformatics, searching for massive
short patterns over a long text is widely accelerated by various compressed
full-text indexes. These indexes are able to provide similar searching
functionalities to classical indexes, e.g., suffix trees and suffix arrays,
while requiring less space. For genomic data, a well-known family of compressed
full-text index, called FM-indexes, presents unmatched performance in practice.
One major drawback of FM-indexes is that their locating operations, which
report all occurrence positions of patterns in a given text, are particularly
slow, especially for the patterns with many occurrences.
  Results: In this paper, we introduce a novel locating algorithm, FMtree, to
fast retrieve all occurrence positions of any pattern via FM-indexes. When
searching for a pattern over a given text, FMtree organizes the search space of
the locating operation into a conceptual quadtree. As a result, multiple
occurrence positions of this pattern can be retrieved simultaneously by
traversing the quadtree. Compared with the existing locating algorithms, our
tree-based algorithm reduces large numbers of redundant operations and presents
better data locality. Experimental results show that FMtree is usually one
order of magnitude faster than the state-of-the-art algorithms, and still
memory-efficient.