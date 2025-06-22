---
layout: publication
title: Regularised Cross-modal Hashing
authors: Moran S., Lavrenko
conference: Arxiv
year: 2024
citations: 14
bibkey: moran2024regularised
additional_links: [{name: Paper, url: 'http://seanjmoran.com/pdfs/cmh_sigir15.pdf'}]
tags: [Multi-Modal Hashing, Hashing Methods, ANN Search]
---
In this paper we propose Regularised Cross-Modal Hashing (RCMH) a new cross-modal hashing scheme that projects annotation and visual feature descriptors into a common Hamming space. RCMH optimises the intra-modality similarity of data-points in the annotation modality using an iterative three-step hashing algorithm: in the first step each training image is assigned a K-bit hashcode based on hyperplanes learnt at the previous iteration; in the second step the binary bits are smoothed by a formulation of graph regularisation so that similar data-points have similar bits; in the third step a set of binary classifiers are trained to predict the regularised bits with maximum margin. Visual descriptors are projected into the annotation Hamming space by a set of binary classifiers learnt using the bits of the corresponding annotations as labels. RCMH is shown to consistently improve retrieval effectiveness over state-of-the-art baselines.