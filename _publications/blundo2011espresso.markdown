---
layout: publication
title: 'Espresso: Efficient Privacy-preserving Evaluation Of Sample Set Similarity'
authors: Carlo Blundo, Emiliano de Cristofaro, Paolo Gasti
conference: Journal of Computer Security
year: 2011
bibkey: blundo2011espresso
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1111.5062'}]
tags: ["Datasets", "Evaluation", "Locality-Sensitive-Hashing"]
short_authors: Carlo Blundo, Emiliano de Cristofaro, Paolo Gasti
---
Electronic information is increasingly often shared among entities without
complete mutual trust. To address related security and privacy issues, a few
cryptographic techniques have emerged that support privacy-preserving
information sharing and retrieval. One interesting open problem in this context
involves two parties that need to assess the similarity of their datasets, but
are reluctant to disclose their actual content. This paper presents an
efficient and provably-secure construction supporting the privacy-preserving
evaluation of sample set similarity, where similarity is measured as the
Jaccard index. We present two protocols: the first securely computes the
(Jaccard) similarity of two sets, and the second approximates it, using MinHash
techniques, with lower complexities. We show that our novel protocols are
attractive in many compelling applications, including document/multimedia
similarity, biometric authentication, and genetic tests. In the process, we
demonstrate that our constructions are appreciably more efficient than prior
work.