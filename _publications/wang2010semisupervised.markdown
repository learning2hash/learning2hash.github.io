---
layout: publication
title: "Semi-supervised hashing for scalable image retrieval"
authors: J. Wang, S. Kumar, and S. Chang
conference: CVPR
year: 2010
bibkey: wang2010semisupervised
additional_links:
   - {name: "PDF", url: "http://www.sanjivk.com/SSH_CVPR10.pdf"}
   - {name: "Talk", url: "http://www.ee.columbia.edu/~jwang/cvprpresentations/PosterSpotlight_SSH.ppt"}
   - {name: "Poster", url: "http://www.ee.columbia.edu/~jwang/cvprpresentations/SSH_CVPR2010_poster.pdf"}
---
Large scale image search has recently attracted considerable
attention due to easy availability of huge amounts of
data. Several hashing methods have been proposed to allow
approximate but highly efficient search. Unsupervised
hashing methods show good performance with metric distances
but, in image search, semantic similarity is usually
given in terms of labeled pairs of images. There exist supervised
hashing methods that can handle such semantic similarity
but they are prone to overfitting when labeled data
is small or noisy. Moreover, these methods are usually very
slow to train. In this work, we propose a semi-supervised
hashing method that is formulated as minimizing empirical
error on the labeled data while maximizing variance
and independence of hash bits over the labeled and unlabeled
data. The proposed method can handle both metric as
well as semantic similarity. The experimental results on two
large datasets (up to one million samples) demonstrate its
superior performance over state-of-the-art supervised and
unsupervised methods.
