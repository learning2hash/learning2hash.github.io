---
layout: publication
title: Self-supervised Cross-modal Text-image Time Series Retrieval In Remote Sensing
authors: "Genc Hoxha, Oliv\xE9r Angyal, Beg\xFCm Demir"
conference: IEEE Transactions on Geoscience and Remote Sensing
year: 2025
bibkey: hoxha2025self
citations: 0
additional_links: [{name: Code, url: 'https://git.tu-berlin.de/rsim/cross-modal-text-tsir'},
  {name: Paper, url: 'https://arxiv.org/abs/2501.19043'}]
tags: ["Efficiency", "Evaluation", "Self-Supervised", "Supervised"]
short_authors: "Genc Hoxha, Oliv\xE9r Angyal, Beg\xFCm Demir"
---
The development of image time series retrieval (ITSR) methods is a growing
research interest in remote sensing (RS). Given a user-defined image time
series (i.e., the query time series), the ITSR methods search and retrieve from
large archives the image time series that have similar content to the query
time series. The existing ITSR methods in RS are designed for unimodal
retrieval problems, limiting their usability and versatility. To overcome this
issue, as a first time in RS we introduce the task of cross-modal text-ITSR. In
particular, we present a self-supervised cross-modal text-image time series
retrieval (text-ITSR) method that enables the retrieval of image time series
using text sentences as queries, and vice versa. In detail, we focus our
attention on text-ITSR in pairs of images (i.e., bitemporal images). The
proposed text-ITSR method consists of two key components: 1) modality-specific
encoders to model the semantic content of bitemporal images and text sentences
with discriminative features; and 2) modality-specific projection heads to
align textual and image representations in a shared embedding space. To
effectively model the temporal information within the bitemporal images, we
introduce two fusion strategies: i) global feature fusion (GFF) strategy that
combines global image features through simple yet effective operators; and ii)
transformer-based feature fusion (TFF) strategy that leverages transformers for
fine-grained temporal integration. Extensive experiments conducted on two
benchmark RS archives demonstrate the effectiveness of the proposed method in
accurately retrieving semantically relevant bitemporal images (or text
sentences) to a query text sentence (or bitemporal image). The code of this
work is publicly available at
https://git.tu-berlin.de/rsim/cross-modal-text-tsir.