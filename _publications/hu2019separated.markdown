---
layout: publication
title: Separated Variational Hashing Networks For Cross-modal Retrieval
authors: Peng Hu, Wang, Zhen, Peng
conference: Proceedings of the 27th ACM International Conference on Multimedia
year: 2019
bibkey: hu2019separated
citations: 30
additional_links: [{name: Paper, url: 'https://dl.acm.org/citation.cfm?id=3351078'}]
tags: [Memory Efficiency, Multimodal Retrieval, Efficiency, Hashing Methods, Compact
    Codes, Similarity Search, Evaluation]
short_authors: Hu et al.
---
Cross-modal hashing, due to its low storage cost and high query speed, has been successfully used for similarity search in multimedia retrieval applications. It projects high-dimensional data into a shared isomorphic Hamming space with similar binary codes for semantically-similar data. In some applications, all modalities may not be obtained or trained simultaneously for some reasons, such as privacy, secret, storage limitation, and computational resource limitation. However, most existing cross-modal hashing methods need all modalities to jointly learn the common Hamming space, thus hindering them from handling these problems. In this paper, we propose a novel approach called Separated Variational Hashing Networks (SVHNs) to overcome the above challenge. Firstly, it adopts a label network (LabNet) to exploit available and nonspecific label annotations to learn a latent common Hamming space by projecting each semantic label into a common binary representation. Then, each modality-specific network can separately map the samples of the corresponding modality into their binary semantic codes learned by LabNet. We achieve it by conducting variational inference to match the aggregated posterior of the hashing code of LabNet with an arbitrary prior distribution. The effectiveness and efficiency of our SVHNs are verified by extensive experiments carried out on four widely-used multimedia databases, in comparison with 11 state-of-the-art approaches.