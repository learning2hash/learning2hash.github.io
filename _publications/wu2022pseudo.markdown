---
layout: publication
title: Pseudo-pair Based Self-similarity Learning For Unsupervised Person Re-identification
authors: Lin Wu, Deyin Liu, Wenying Zhang, Dapeng Chen, Zongyuan Ge, Farid Boussaid,
  Mohammed Bennamoun, Jialie Shen
conference: IEEE Transactions on Image Processing
year: 2022
bibkey: wu2022pseudo
citations: 58
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.13035'}]
tags: ["Self-Supervised", "Unsupervised"]
short_authors: Wu et al.
---
Person re-identification (re-ID) is of great importance to video surveillance
systems by estimating the similarity between a pair of cross-camera person
shorts. Current methods for estimating such similarity require a large number
of labeled samples for supervised training. In this paper, we present a
pseudo-pair based self-similarity learning approach for unsupervised person
re-ID without human annotations. Unlike conventional unsupervised re-ID methods
that use pseudo labels based on global clustering, we construct patch surrogate
classes as initial supervision, and propose to assign pseudo labels to images
through the pairwise gradient-guided similarity separation. This can cluster
images in pseudo pairs, and the pseudos can be updated during training. Based
on pseudo pairs, we propose to improve the generalization of similarity
function via a novel self-similarity learning:it learns local discriminative
features from individual images via intra-similarity, and discovers the patch
correspondence across images via inter-similarity. The intra-similarity
learning is based on channel attention to detect diverse local features from an
image. The inter-similarity learning employs a deformable convolution with a
non-local block to align patches for cross-image similarity. Experimental
results on several re-ID benchmark datasets demonstrate the superiority of the
proposed method over the state-of-the-arts.