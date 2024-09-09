---
layout: publication
title: "A Similarity Measure of Histopathology Images by Deep Embeddings"
authors: Afshari Mehdi, Tizhoosh H. R.
conference: "Arxiv"
year: 2021
bibkey: afshari2021a
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2107.13703"}
tags: ['ARXIV']
---
Histopathology digital scans are large-size images that contain valuable
information at the pixel level. Content-based comparison of these images is a
challenging task. This study proposes a content-based similarity measure for
high-resolution gigapixel histopathology images. The proposed similarity measure
is an expansion of cosine vector similarity to a matrix. Each image is divided
into same-size patches with a meaningful amount of information (i.e., contained
enough tissue). The similarity is measured by the extraction of patch-level deep
embeddings of the last pooling layer of a pre-trained deep model at four
different magnification levels, namely, 1x, 2.5x, 5x, and 10x magnifications. In
addition, for faster measurement, embedding reduction is investigated. Finally,
to assess the proposed method, an image search method is implemented. Results
show that the similarity measure represents the slide labels with a maximum
accuracy of 93.18\% for top-5 search at 5x magnification.
