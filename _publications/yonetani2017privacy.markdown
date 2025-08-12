---
layout: publication
title: Privacy-preserving Visual Learning Using Doubly Permuted Homomorphic Encryption
authors: Ryo Yonetani, Vishnu Naresh Boddeti, Kris M. Kitani, Yoichi Sato
conference: 2017 IEEE International Conference on Computer Vision (ICCV)
year: 2017
bibkey: yonetani2017privacy
citations: 69
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.02203'}]
tags: ["ICCV"]
short_authors: Yonetani et al.
---
We propose a privacy-preserving framework for learning visual classifiers by
leveraging distributed private image data. This framework is designed to
aggregate multiple classifiers updated locally using private data and to ensure
that no private information about the data is exposed during and after its
learning procedure. We utilize a homomorphic cryptosystem that can aggregate
the local classifiers while they are encrypted and thus kept secret. To
overcome the high computational cost of homomorphic encryption of
high-dimensional classifiers, we (1) impose sparsity constraints on local
classifier updates and (2) propose a novel efficient encryption scheme named
doubly-permuted homomorphic encryption (DPHE) which is tailored to sparse
high-dimensional data. DPHE (i) decomposes sparse data into its constituent
non-zero values and their corresponding support indices, (ii) applies
homomorphic encryption only to the non-zero values, and (iii) employs double
permutations on the support indices to make them secret. Our experimental
evaluation on several public datasets shows that the proposed approach achieves
comparable performance against state-of-the-art visual recognition methods
while preserving privacy and significantly outperforms other privacy-preserving
methods.