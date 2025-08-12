---
layout: publication
title: Weaponizing Unicodes With Deep Learning -- Identifying Homoglyphs With Weakly
  Labeled Data
authors: Perry Deng, Cooper Linsky, Matthew Wright
conference: 2020 IEEE International Conference on Intelligence and Security Informatics
  (ISI)
year: 2020
bibkey: deng2020weaponizing
citations: 4
additional_links: [{name: Code, url: 'https://github.com/PerryXDeng/weaponizing_unicode'},
  {name: Paper, url: 'https://arxiv.org/abs/2010.04382'}]
tags: []
short_authors: Perry Deng, Cooper Linsky, Matthew Wright
---
Visually similar characters, or homoglyphs, can be used to perform social
engineering attacks or to evade spam and plagiarism detectors. It is thus
important to understand the capabilities of an attacker to identify homoglyphs
-- particularly ones that have not been previously spotted -- and leverage them
in attacks. We investigate a deep-learning model using embedding learning,
transfer learning, and augmentation to determine the visual similarity of
characters and thereby identify potential homoglyphs. Our approach uniquely
takes advantage of weak labels that arise from the fact that most characters
are not homoglyphs. Our model drastically outperforms the Normalized
Compression Distance approach on pairwise homoglyph identification, for which
we achieve an average precision of 0.97. We also present the first attempt at
clustering homoglyphs into sets of equivalence classes, which is more efficient
than pairwise information for security practitioners to quickly lookup
homoglyphs or to normalize confusable string encodings. To measure clustering
performance, we propose a metric (mBIOU) building on the classic
Intersection-Over-Union (IOU) metric. Our clustering method achieves 0.592
mBIOU, compared to 0.430 for the naive baseline. We also use our model to
predict over 8,000 previously unknown homoglyphs, and find good early
indications that many of these may be true positives. Source code and list of
predicted homoglyphs are uploaded to Github:
https://github.com/PerryXDeng/weaponizing_unicode