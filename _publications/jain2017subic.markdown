---
layout: publication
title: 'SUBIC: A Supervised, Structured Binary Code For Image Search'
authors: "Himalaya Jain, Joaquin Zepeda, Patrick P\xE9rez, R\xE9mi Gribonval"
conference: 2017 IEEE International Conference on Computer Vision (ICCV)
year: 2017
bibkey: jain2017subic
citations: 61
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.02932'}]
tags: ["Compact Codes", "Hashing Methods", "ICCV", "Image Retrieval", "Neural Hashing", "Quantization", "Scalability", "Supervised", "Unsupervised"]
short_authors: Jain et al.
---
For large-scale visual search, highly compressed yet meaningful
representations of images are essential. Structured vector quantizers based on
product quantization and its variants are usually employed to achieve such
compression while minimizing the loss of accuracy. Yet, unlike binary hashing
schemes, these unsupervised methods have not yet benefited from the
supervision, end-to-end learning and novel architectures ushered in by the deep
learning revolution. We hence propose herein a novel method to make deep
convolutional neural networks produce supervised, compact, structured binary
codes for visual search. Our method makes use of a novel block-softmax
non-linearity and of batch-based entropy losses that together induce structure
in the learned encodings. We show that our method outperforms state-of-the-art
compact representations based on deep hashing or structured quantization in
single and cross-domain category retrieval, instance retrieval and
classification. We make our code and models publicly available online.