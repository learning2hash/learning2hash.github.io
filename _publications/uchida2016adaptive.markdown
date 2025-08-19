---
layout: publication
title: Adaptive Substring Extraction And Modified Local NBNN Scoring For Binary Feature-based
  Local Mobile Visual Search Without False Positives
authors: Yusuke Uchida, Shigeyuki Sakazawa, Shin'Ichi Satoh
conference: ITE Transactions on Media Technology and Applications
year: 2016
bibkey: uchida2016adaptive
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.06266'}]
tags: [Tools & Libraries, Image Retrieval]
short_authors: Yusuke Uchida, Shigeyuki Sakazawa, Shin'Ichi Satoh
---
In this paper, we propose a stand-alone mobile visual search system based on
binary features and the bag-of-visual words framework. The contribution of this
study is three-fold: (1) We propose an adaptive substring extraction method
that adaptively extracts informative bits from the original binary vector and
stores them in the inverted index. These substrings are used to refine visual
word-based matching. (2) A modified local NBNN scoring method is proposed in
the context of image retrieval, which considers the density of binary features
in scoring each feature matching. (3) In order to suppress false positives, we
introduce a convexity check step that imposes a convexity constraint on the
configuration of a transformed reference image. The proposed system improves
retrieval accuracy by 11% compared with a conventional method without
increasing the database size. Furthermore, our system with the convexity check
does not lead to false positive results.