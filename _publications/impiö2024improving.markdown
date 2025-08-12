---
layout: publication
title: Improving Taxonomic Image-based Out-of-distribution Detection With DNA Barcodes
authors: "Mikko Impi\xF6, Jenni Raitoharju"
conference: 2024 32nd European Signal Processing Conference (EUSIPCO)
year: 2024
bibkey: "impi\xF62024improving"
citations: 1
additional_links: [{name: Code, url: 'https://github.com/mikkoim/dnaimg-ood'}, {name: Paper,
    url: 'https://arxiv.org/abs/2406.18999'}]
tags: ["Image Retrieval"]
short_authors: "Mikko Impi\xF6, Jenni Raitoharju"
---
Image-based species identification could help scaling biodiversity monitoring
to a global scale. Many challenges still need to be solved in order to
implement these systems in real-world applications. A reliable image-based
monitoring system must detect out-of-distribution (OOD) classes it has not been
presented before. This is challenging especially with fine-grained classes.
Emerging environmental monitoring techniques, DNA metabarcoding and eDNA, can
help by providing information on OOD classes that are present in a sample. In
this paper, we study if DNA barcodes can also support in finding the outlier
images based on the outlier DNA sequence's similarity to the seen classes. We
propose a re-ordering approach that can be easily applied on any pre-trained
models and existing OOD detection methods. We experimentally show that the
proposed approach improves taxonomic OOD detection compared to all common
baselines. We also show that the method works thanks to a correlation between
visual similarity and DNA barcode proximity. The code and data are available at
https://github.com/mikkoim/dnaimg-ood.