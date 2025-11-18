---
layout: publication
title: 'HERS: Homomorphically Encrypted Representation Search'
authors: Joshua J. Engelsma, Anil K. Jain, Vishnu Naresh Boddeti
conference: IEEE Transactions on Biometrics, Behavior, and Identity Science
year: 2020
bibkey: engelsma2020hers
citations: 46
additional_links: [{name: Code, url: 'https://github.com/human-analysis/hers-encrypted-image-search'},
  {name: Paper, url: 'https://arxiv.org/abs/2003.12197'}]
tags: ["Compact Codes", "Datasets", "Image Retrieval", "Privacy & Security"]
short_authors: Joshua J. Engelsma, Anil K. Jain, Vishnu Naresh Boddeti
---
We present a method to search for a probe (or query) image representation
against a large gallery in the encrypted domain. We require that the probe and
gallery images be represented in terms of a fixed-length representation, which
is typical for representations obtained from learned networks. Our encryption
scheme is agnostic to how the fixed-length representation is obtained and can
therefore be applied to any fixed-length representation in any application
domain. Our method, dubbed HERS (Homomorphically Encrypted Representation
Search), operates by (i) compressing the representation towards its estimated
intrinsic dimensionality with minimal loss of accuracy (ii) encrypting the
compressed representation using the proposed fully homomorphic encryption
scheme, and (iii) efficiently searching against a gallery of encrypted
representations directly in the encrypted domain, without decrypting them.
Numerical results on large galleries of face, fingerprint, and object datasets
such as ImageNet show that, for the first time, accurate and fast image search
within the encrypted domain is feasible at scale (500 seconds; \(275\times\)
speed up over state-of-the-art for encrypted search against a gallery of 100
million). Code is available at
https://github.com/human-analysis/hers-encrypted-image-search