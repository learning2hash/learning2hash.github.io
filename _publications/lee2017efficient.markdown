---
layout: publication
title: Efficient Feature Matching By Progressive Candidate Search
authors: Sehyung Lee, Jongwoo Lim, Il Hong Suh
conference: Arxiv
year: 2017
bibkey: lee2017efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1701.05676'}]
tags: ["Efficiency"]
short_authors: Sehyung Lee, Jongwoo Lim, Il Hong Suh
---
We present a novel feature matching algorithm that systematically utilizes
the geometric properties of features such as position, scale, and orientation,
in addition to the conventional descriptor vectors. In challenging scenes with
the presence of repetitive patterns or with a large viewpoint change, it is
hard to find the correct correspondences using feature descriptors only, since
the descriptor distances of the correct matches may not be the least among the
candidates due to appearance changes. Assuming that the layout of the nearby
features does not changed much, we propose the bidirectional transfer measure
to gauge the geometric consistency of a pair of feature correspondences. The
feature matching problem is formulated as a Markov random field (MRF) which
uses descriptor distances and relative geometric similarities together. The
unmatched features are explicitly modeled in the MRF to minimize its negative
impact. For speed and stability, instead of solving the MRF on the entire
features at once, we start with a small set of confident feature matches, and
then progressively search the candidates in nearby features and expand the MRF
with them. Experimental comparisons show that the proposed algorithm finds
better feature correspondences, i.e. more matches with higher inlier ratio, in
many challenging scenes with much lower computational cost than the
state-of-the-art algorithms.