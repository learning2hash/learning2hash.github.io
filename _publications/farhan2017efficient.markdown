---
layout: publication
title: Efficient Approximation Algorithms For String Kernel Based Sequence Classification
authors: Muhammad Farhan, Juvaria Tariq, Arif Zaman, Mudassir Shabbir, Imdad Ullah
  Khan
conference: Arxiv
year: 2017
bibkey: farhan2017efficient
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.04264'}]
tags: ["Scalability"]
short_authors: Farhan et al.
---
Sequence classification algorithms, such as SVM, require a definition of
distance (similarity) measure between two sequences. A commonly used notion of
similarity is the number of matches between \(k\)-mers (\(k\)-length subsequences)
in the two sequences. Extending this definition, by considering two \(k\)-mers to
match if their distance is at most \(m\), yields better classification
performance. This, however, makes the problem computationally much more
complex. Known algorithms to compute this similarity have computational
complexity that render them applicable only for small values of \(k\) and \(m\). In
this work, we develop novel techniques to efficiently and accurately estimate
the pairwise similarity score, which enables us to use much larger values of
\(k\) and \(m\), and get higher predictive accuracy. This opens up a broad avenue
of applying this classification approach to audio, images, and text sequences.
Our algorithm achieves excellent approximation performance with theoretical
guarantees. In the process we solve an open combinatorial problem, which was
posed as a major hindrance to the scalability of existing solutions. We give
analytical bounds on quality and runtime of our algorithm and report its
empirical performance on real world biological and music sequences datasets.