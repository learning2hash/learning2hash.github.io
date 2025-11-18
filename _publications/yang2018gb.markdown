---
layout: publication
title: 'GB-KMV: An Augmented KMV Sketch For Approximate Containment Similarity Search'
authors: Yang Yang, Ying Zhang, Wenjie Zhang, Zengfeng Huang
conference: 2019 IEEE 35th International Conference on Data Engineering (ICDE)
year: 2018
bibkey: yang2018gb
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.00458'}]
tags: ["Datasets", "Locality-Sensitive-Hashing", "Similarity Search", "Tools & Libraries"]
short_authors: Yang et al.
---
In this paper, we study the problem of approximate containment similarity
search. Given two records Q and X, the containment similarity between Q and X
with respect to Q is |Q intersect X|/ |Q|. Given a query record Q and a set of
records S, the containment similarity search finds a set of records from S
whose containment similarity regarding Q are not less than the given threshold.
This problem has many important applications in commercial and scientific
fields such as record matching and domain search. Existing solution relies on
the asymmetric LSH method by transforming the containment similarity to
well-studied Jaccard similarity. In this paper, we use a different framework by
transforming the containment similarity to set intersection. We propose a novel
augmented KMV sketch technique, namely GB-KMV, which is data-dependent and can
achieve a good trade-off between the sketch size and the accuracy. We provide a
set of theoretical analysis to underpin the proposed augmented KMV sketch
technique, and show that it outperforms the state-of-the-art technique LSH-E in
terms of estimation accuracy under practical assumption. Our comprehensive
experiments on real-life datasets verify that GB-KMV is superior to LSH-E in
terms of the space-accuracy trade-off, time-accuracy trade-off, and the sketch
construction time. For instance, with similar estimation accuracy (F-1 score),
GB-KMV is over 100 times faster than LSH-E on some real-life dataset.