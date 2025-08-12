---
layout: publication
title: 'Lossless Image Compression Using Multi-level Dictionaries: Binary Images'
authors: Samar Agnihotri, Renu Rameshan, Ritwik Ghosal
conference: Arxiv
year: 2024
bibkey: agnihotri2024lossless
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.03087'}]
tags: []
short_authors: Samar Agnihotri, Renu Rameshan, Ritwik Ghosal
---
Lossless image compression is required in various applications to reduce
storage or transmission costs of images, while requiring the reconstructed
images to have zero information loss compared to the original. Existing
lossless image compression methods either have simple design but poor
compression performance, or complex design, better performance, but with no
performance guarantees. In our endeavor to develop a lossless image compression
method with low complexity and guaranteed performance, we argue that
compressibility of a color image is essentially derived from the patterns in
its spatial structure, intensity variations, and color variations. Thus, we
divide the overall design of a lossless image compression scheme into three
parts that exploit corresponding redundancies. We further argue that the
binarized version of an image captures its fundamental spatial structure. In
this first part of our work, we propose a scheme for lossless compression of
binary images.
  The proposed scheme first learns dictionaries of \(16\times16\), \(8\times8\),
\(4\times4\), and \(2\times 2\) square pixel patterns from various datasets of
binary images. It then uses these dictionaries to encode binary images. These
dictionaries have various interesting properties that are further exploited to
construct an efficient and scalable scheme. Our preliminary results show that
the proposed scheme consistently outperforms existing conventional and learning
based lossless compression approaches, and provides, on average, as much as
\(1.5\times\) better performance than a common general purpose lossless
compression scheme (WebP), more than \(3\times\) better performance than a state
of the art learning based scheme, and better performance than a specialized
scheme for binary image compression (JBIG2).