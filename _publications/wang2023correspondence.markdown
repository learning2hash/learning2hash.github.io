---
layout: publication
title: Correspondence-free Domain Alignment For Unsupervised Cross-domain Image Retrieval
authors: Xu Wang, Dezhong Peng, Ming Yan, Peng Hu
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2023
bibkey: wang2023correspondence
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.06081'}]
tags: ["AAAI", "Datasets", "Evaluation", "Image Retrieval", "Unsupervised"]
short_authors: Wang et al.
---
Cross-domain image retrieval aims at retrieving images across different
domains to excavate cross-domain classificatory or correspondence
relationships. This paper studies a less-touched problem of cross-domain image
retrieval, i.e., unsupervised cross-domain image retrieval, considering the
following practical assumptions: (i) no correspondence relationship, and (ii)
no category annotations. It is challenging to align and bridge distinct domains
without cross-domain correspondence. To tackle the challenge, we present a
novel Correspondence-free Domain Alignment (CoDA) method to effectively
eliminate the cross-domain gap through In-domain Self-matching Supervision
(ISS) and Cross-domain Classifier Alignment (CCA). To be specific, ISS is
presented to encapsulate discriminative information into the latent common
space by elaborating a novel self-matching supervision mechanism. To alleviate
the cross-domain discrepancy, CCA is proposed to align distinct domain-specific
classifiers. Thanks to the ISS and CCA, our method could encode the
discrimination into the domain-invariant embedding space for unsupervised
cross-domain image retrieval. To verify the effectiveness of the proposed
method, extensive experiments are conducted on four benchmark datasets compared
with six state-of-the-art methods.