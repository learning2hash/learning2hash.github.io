---
layout: publication
title: 'Bytenet: Rethinking Multimedia File Fragment Classification Through Visual
  Perspectives'
authors: Wenyang Liu, Kejun Wu, Tianyi Liu, Yi Wang, Kim-Hui Yap, Lap-Pui Chau
conference: Arxiv
year: 2024
bibkey: liu2024bytenet
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.20855'}]
tags: []
short_authors: Liu et al.
---
Multimedia file fragment classification (MFFC) aims to identify file fragment
types, e.g., image/video, audio, and text without system metadata. It is of
vital importance in multimedia storage and communication. Existing MFFC methods
typically treat fragments as 1D byte sequences and emphasize the relations
between separate bytes (interbytes) for classification. However, the more
informative relations inside bytes (intrabytes) are overlooked and seldom
investigated. By looking inside bytes, the bit-level details of file fragments
can be accessed, enabling a more accurate classification. Motivated by this, we
first propose Byte2Image, a novel visual representation model that incorporates
previously overlooked intrabyte information into file fragments and
reinterprets these fragments as 2D grayscale images. This model involves a
sliding byte window to reveal the intrabyte information and a rowwise stacking
of intrabyte ngrams for embedding fragments into a 2D space. Thus, complex
interbyte and intrabyte correlations can be mined simultaneously using powerful
vision networks. Additionally, we propose an end-to-end dual-branch network
ByteNet to enhance robust correlation mining and feature representation.
ByteNet makes full use of the raw 1D byte sequence and the converted 2D image
through a shallow byte branch feature extraction (BBFE) and a deep image branch
feature extraction (IBFE) network. In particular, the BBFE, composed of a
single fully-connected layer, adaptively recognizes the co-occurrence of
several some specific bytes within the raw byte sequence, while the IBFE, built
on a vision Transformer, effectively mines the complex interbyte and intrabyte
correlations from the converted image. Experiments on the two representative
benchmarks, including 14 cases, validate that our proposed method outperforms
state-of-the-art approaches on different cases by up to 12.2%.