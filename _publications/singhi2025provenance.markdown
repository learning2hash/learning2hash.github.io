---
layout: publication
title: 'Provenance Detection For Ai-generated Images: Combining Perceptual Hashing,
  Homomorphic Encryption, And AI Detection Models'
authors: Singhi et al.
conference: 2023 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW)
year: 2025
bibkey: singhi2025provenance
citations: 35
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.11195'}]
tags: [ICCV, Tools & Libraries, Hashing Methods, Robustness]
---
As AI-generated sensitive images become more prevalent, identifying their
source is crucial for distinguishing them from real images. Conventional image
watermarking methods are vulnerable to common transformations like filters,
lossy compression, and screenshots, often applied during social media sharing.
Watermarks can also be faked or removed if models are open-sourced or leaked
since images can be rewatermarked. We have developed a three-part framework for
secure, transformation-resilient AI content provenance detection, to address
these limitations. We develop an adversarially robust state-of-the-art
perceptual hashing model, DinoHash, derived from DINOV2, which is robust to
common transformations like filters, compression, and crops. Additionally, we
integrate a Multi-Party Fully Homomorphic Encryption~(MP-FHE) scheme into our
proposed framework to ensure the protection of both user queries and registry
privacy. Furthermore, we improve previous work on AI-generated media detection.
This approach is useful in cases where the content is absent from our registry.
DinoHash significantly improves average bit accuracy by 12% over
state-of-the-art watermarking and perceptual hashing methods while maintaining
superior true positive rate (TPR) and false positive rate (FPR) tradeoffs
across various transformations. Our AI-generated media detection results show a
25% improvement in classification accuracy on commonly used real-world AI image
generators over existing algorithms. By combining perceptual hashing, MP-FHE,
and an AI content detection model, our proposed framework provides better
robustness and privacy compared to previous work.