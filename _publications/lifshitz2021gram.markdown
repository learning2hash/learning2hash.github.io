---
layout: publication
title: Gram Barcodes For Histopathology Tissue Texture Retrieval
authors: Shalev Lifshitz, Abtin Riasatian, H. R. Tizhoosh
conference: Arxiv
year: 2021
bibkey: lifshitz2021gram
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.15519'}]
tags: [Datasets, Image Retrieval]
short_authors: Shalev Lifshitz, Abtin Riasatian, H. R. Tizhoosh
---
Recent advances in digital pathology have led to the need for Histopathology
Image Retrieval (HIR) systems that search through databases of biopsy images to
find similar cases to a given query image. These HIR systems allow pathologists
to effortlessly and efficiently access thousands of previously diagnosed cases
in order to exploit the knowledge in the corresponding pathology reports. Since
HIR systems may have to deal with millions of gigapixel images, the extraction
of compact and expressive image features must be available to allow for
efficient and accurate retrieval. In this paper, we propose the application of
Gram barcodes as image features for HIR systems. Unlike most feature generation
schemes, Gram barcodes are based on high-order statistics that describe tissue
texture by summarizing the correlations between different feature maps in
layers of convolutional neural networks. We run HIR experiments on three public
datasets using a pre-trained VGG19 network for Gram barcode generation and
showcase highly competitive results.