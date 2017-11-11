---
layout: publication
title: "Deep Semantic Ranking Based Hashing for Multi-Label Image Retrieval"
authors: F. Zhao, Y. Huang, L. Wang, and T. Tan
conference: CVPR
year: 2015
bibkey: zhao2015deep
additional_links:
   - {name: "PDF", url: "http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Zhao_Deep_Semantic_Ranking_2015_CVPR_paper.pdf"}
---
With the rapid growth of web images, hashing has received
increasing interests in large scale image retrieval.
Research efforts have been devoted to learning compact binary
codes that preserve semantic similarity based on labels.
However, most of these hashing methods are designed
to handle simple binary similarity. The complex multilevel
semantic structure of images associated with multiple labels
have not yet been well explored. Here we propose a deep
semantic ranking based method for learning hash functions
that preserve multilevel semantic similarity between multilabel
images. In our approach, deep convolutional neural
network is incorporated into hash functions to jointly
learn feature representations and mappings from them to
hash codes, which avoids the limitation of semantic representation
power of hand-crafted features. Meanwhile, a
ranking list that encodes the multilevel similarity information
is employed to guide the learning of such deep hash
functions. An effective scheme based on surrogate loss is
used to solve the intractable optimization problem of nonsmooth
and multivariate ranking measures involved in the
learning procedure. Experimental results show the superiority
of our proposed approach over several state-of-theart
hashing methods in term of ranking evaluation metrics
when tested on multi-label image datasets.
