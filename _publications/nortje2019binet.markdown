---
layout: publication
title: 'Binet: A Binary Inpainting Network For Deep Patch-based Image Compression'
authors: "Andr\xE9 Nortje, Willie Brink, Herman A. Engelbrecht, Herman Kamper"
conference: 'Signal Processing: Image Communication'
year: 2020
bibkey: nortje2019binet
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.05189'}]
tags: ["Compact Codes"]
short_authors: Nortje et al.
---
Recent deep learning models outperform standard lossy image compression
codecs. However, applying these models on a patch-by-patch basis requires that
each image patch be encoded and decoded independently. The influence from
adjacent patches is therefore lost, leading to block artefacts at low bitrates.
We propose the Binary Inpainting Network (BINet), an autoencoder framework
which incorporates binary inpainting to reinstate interdependencies between
adjacent patches, for improved patch-based compression of still images. When
decoding a patch, BINet additionally uses the binarised encodings from
surrounding patches to guide its reconstruction. In contrast to sequential
inpainting methods where patches are decoded based on previons reconstructions,
BINet operates directly on the binary codes of surrounding patches without
access to the original or reconstructed image data. Encoding and decoding can
therefore be performed in parallel. We demonstrate that BINet improves the
compression quality of a competitive deep image codec across a range of
compression levels.