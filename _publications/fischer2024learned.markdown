---
layout: publication
title: Learned Image Compression For He-stained Histopathological Images Via Stain
  Deconvolution
authors: "Maximilian Fischer, Peter Neher, Tassilo Wald, Silvia Dias Almeida, Shuhan\
  \ Xiao, Peter Sch\xFCffler, Rickmer Braren, Michael G\xF6tz, Alexander Muckenhuber,\
  \ Jens Kleesiek, Marco Nolden, Klaus Maier-hein"
conference: Lecture Notes in Computer Science
year: 2025
bibkey: fischer2024learned
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.12623'}]
tags: ["Evaluation"]
short_authors: Fischer et al.
---
Processing histopathological Whole Slide Images (WSI) leads to massive
storage requirements for clinics worldwide. Even after lossy image compression
during image acquisition, additional lossy compression is frequently possible
without substantially affecting the performance of deep learning-based (DL)
downstream tasks. In this paper, we show that the commonly used JPEG algorithm
is not best suited for further compression and we propose Stain Quantized
Latent Compression (SQLC ), a novel DL based histopathology data compression
approach. SQLC compresses staining and RGB channels before passing it through a
compression autoencoder (CAE ) in order to obtain quantized latent
representations for maximizing the compression. We show that our approach
yields superior performance in a classification downstream task, compared to
traditional approaches like JPEG, while image quality metrics like the
Multi-Scale Structural Similarity Index (MS-SSIM) is largely preserved. Our
method is online available.