---
layout: publication
title: On Kernelization Of Supervised Mahalanobis Distance Learners
authors: Ratthachat Chatpatanasiri, Teesid Korsrilabutr, Pasakorn Tangchanachaianan,
  Boonserm Kijsirikul
conference: Arxiv
year: 2008
bibkey: chatpatanasiri2008kernelization
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/0804.1441'}]
tags: ["Supervised"]
short_authors: Chatpatanasiri et al.
---
This paper focuses on the problem of kernelizing an existing supervised
Mahalanobis distance learner. The following features are included in the paper.
Firstly, three popular learners, namely, "neighborhood component analysis",
"large margin nearest neighbors" and "discriminant neighborhood embedding",
which do not have kernel versions are kernelized in order to improve their
classification performances. Secondly, an alternative kernelization framework
called "KPCA trick" is presented. Implementing a learner in the new framework
gains several advantages over the standard framework, e.g. no mathematical
formulas and no reprogramming are required for a kernel implementation, the
framework avoids troublesome problems such as singularity, etc. Thirdly, while
the truths of representer theorems are just assumptions in previous papers
related to ours, here, representer theorems are formally proven. The proofs
validate both the kernel trick and the KPCA trick in the context of Mahalanobis
distance learning. Fourthly, unlike previous works which always apply brute
force methods to select a kernel, we investigate two approaches which can be
efficiently adopted to construct an appropriate kernel for a given dataset.
Finally, numerical results on various real-world datasets are presented.