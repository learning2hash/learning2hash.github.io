---
layout: publication
title: 'Latent Fingerprint Recognition: Fusion Of Local And Global Embeddings'
authors: Steven A. Grosz, Anil K. Jain
conference: IEEE Transactions on Information Forensics and Security
year: 2023
bibkey: grosz2023latent
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.13800'}]
tags: [Datasets, Evaluation]
short_authors: Steven A. Grosz, Anil K. Jain
---
One of the most challenging problems in fingerprint recognition continues to
be establishing the identity of a suspect associated with partial and smudgy
fingerprints left at a crime scene (i.e., latent prints or fingermarks).
Despite the success of fixed-length embeddings for rolled and slap fingerprint
recognition, the features learned for latent fingerprint matching have mostly
been limited to local minutiae-based embeddings and have not directly leveraged
global representations for matching. In this paper, we combine global
embeddings with local embeddings for state-of-the-art latent to rolled matching
accuracy with high throughput. The combination of both local and global
representations leads to improved recognition accuracy across NIST SD 27, NIST
SD 302, MSP, MOLF DB1/DB4, and MOLF DB2/DB4 latent fingerprint datasets for
both closed-set (84.11%, 54.36%, 84.35%, 70.43%, 62.86% rank-1 retrieval rate,
respectively) and open-set (0.50, 0.74, 0.44, 0.60, 0.68 FNIR at FPIR=0.02,
respectively) identification scenarios on a gallery of 100K rolled
fingerprints. Not only do we fuse the complimentary representations, we also
use the local features to guide the global representations to focus on
discriminatory regions in two fingerprint images to be compared. This leads to
a multi-stage matching paradigm in which subsets of the retrieved candidate
lists for each probe image are passed to subsequent stages for further
processing, resulting in a considerable reduction in latency (requiring just
0.068 ms per latent to rolled comparison on a AMD EPYC 7543 32-Core Processor,
roughly 15K comparisons per second). Finally, we show the generalizability of
the fused representations for improving authentication accuracy across several
rolled, plain, and contactless fingerprint datasets.