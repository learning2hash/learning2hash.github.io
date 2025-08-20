---
layout: publication
title: Image-text Pre-training For Logo Recognition
authors: Mark Hubenthal, Suren Kumar
conference: 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2023
bibkey: hubenthal2023image
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.10206'}]
tags: [Few-shot & Zero-shot, Distance Metric Learning, Datasets, Evaluation]
short_authors: Mark Hubenthal, Suren Kumar
---
Open-set logo recognition is commonly solved by first detecting possible logo
regions and then matching the detected parts against an ever-evolving dataset
of cropped logo images. The matching model, a metric learning problem, is
especially challenging for logo recognition due to the mixture of text and
symbols in logos. We propose two novel contributions to improve the matching
model's performance: (a) using image-text paired samples for pre-training, and
(b) an improved metric learning loss function. A standard paradigm of
fine-tuning ImageNet pre-trained models fails to discover the text sensitivity
necessary to solve the matching problem effectively. This work demonstrates the
importance of pre-training on image-text pairs, which significantly improves
the performance of a visual embedder trained for the logo retrieval task,
especially for more text-dominant classes. We construct a composite public logo
dataset combining LogoDet3K, OpenLogo, and FlickrLogos-47 deemed
OpenLogoDet3K47. We show that the same vision backbone pre-trained on
image-text data, when fine-tuned on OpenLogoDet3K47, achieves \(98.6%\)
recall@1, significantly improving performance over pre-training on Imagenet1K
(\(97.6%\)). We generalize the ProxyNCA++ loss function to propose ProxyNCAHN++
which incorporates class-specific hard negative images. The proposed method
sets new state-of-the-art on five public logo datasets considered, with a
\(3.5%\) zero-shot recall@1 improvement on LogoDet3K test, \(4%\) on OpenLogo,
\(6.5%\) on FlickrLogos-47, \(6.2%\) on Logos In The Wild, and \(0.6%\) on
BelgaLogo.