---
layout: publication
title: Applying Graph Analysis For Unsupervised Fast Malware Fingerprinting
authors: Elmouatez Billah Karbab, Mourad Debbabi
conference: Arxiv
year: 2025
bibkey: karbab2025applying
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2510.12811'}]
tags: ["Efficiency", "Evaluation", "Hashing Methods", "Scalability", "Tools & Libraries", "Unsupervised"]
short_authors: Elmouatez Billah Karbab, Mourad Debbabi
---
Malware proliferation is increasing at a tremendous rate, with hundreds of thousands of new samples identified daily. Manual investigation of such a vast amount of malware is an unrealistic, time-consuming, and overwhelming task. To cope with this volume, there is a clear need to develop specialized techniques and efficient tools for preliminary filtering that can group malware based on semantic similarity. In this paper, we propose TrapNet, a novel, scalable, and unsupervised framework for malware fingerprinting and grouping. TrapNet employs graph community detection techniques for malware fingerprinting and family attribution based on static analysis, as follows: (1) TrapNet detects packed binaries and unpacks them using known generic packer tools. (2) From each malware sample, it generates a digest that captures the underlying semantics. Since the digest must be dense, efficient, and suitable for similarity checking, we designed FloatHash (FH), a novel numerical fuzzy hashing technique that produces a short real-valued vector summarizing the underlying assembly items and their order. FH is based on applying Principal Component Analysis (PCA) to ordered assembly items (e.g., opcodes, function calls) extracted from the malware's assembly code. (3) Representing malware with short numerical vectors enables high-performance, large-scale similarity computation, which allows TrapNet to build a malware similarity network. (4) Finally, TrapNet employs state-of-the-art community detection algorithms to identify dense communities, which represent groups of malware with similar semantics. Our extensive evaluation of TrapNet demonstrates its effectiveness in terms of the coverage and purity of the detected communities, while also highlighting its runtime efficiency, which outperforms other state-of-the-art solutions.