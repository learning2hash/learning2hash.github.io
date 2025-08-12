---
layout: publication
title: Unsupervised Cross-domain Image Retrieval Via Prototypical Optimal Transport
authors: Bin Li, Ye Shi, Qian Yu, Jingya Wang
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2024
bibkey: li2024unsupervised
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.18411'}]
tags: ["AAAI", "Image Retrieval", "Unsupervised"]
short_authors: Li et al.
---
Unsupervised cross-domain image retrieval (UCIR) aims to retrieve images
sharing the same category across diverse domains without relying on labeled
data. Prior approaches have typically decomposed the UCIR problem into two
distinct tasks: intra-domain representation learning and cross-domain feature
alignment. However, these segregated strategies overlook the potential
synergies between these tasks. This paper introduces ProtoOT, a novel Optimal
Transport formulation explicitly tailored for UCIR, which integrates
intra-domain feature representation learning and cross-domain alignment into a
unified framework. ProtoOT leverages the strengths of the K-means clustering
method to effectively manage distribution imbalances inherent in UCIR. By
utilizing K-means for generating initial prototypes and approximating class
marginal distributions, we modify the constraints in Optimal Transport
accordingly, significantly enhancing its performance in UCIR scenarios.
Furthermore, we incorporate contrastive learning into the ProtoOT framework to
further improve representation learning. This encourages local semantic
consistency among features with similar semantics, while also explicitly
enforcing separation between features and unmatched prototypes, thereby
enhancing global discriminativeness. ProtoOT surpasses existing
state-of-the-art methods by a notable margin across benchmark datasets.
Notably, on DomainNet, ProtoOT achieves an average P@200 enhancement of 18.17%,
and on Office-Home, it demonstrates a P@15 improvement of 3.83%.