---
layout: publication
title: 'Content-based Image Retrieval For Multi-class Volumetric Radiology Images:
  A Benchmark Study'
authors: Farnaz Khun Jush, Steffen Vogler, Tuan Truong, Matthias Lenga
conference: Arxiv
year: 2024
bibkey: jush2024content
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.09334'}]
tags: [Evaluation, Supervised, Image Retrieval, Re-ranking, Efficiency, Datasets,
  Unsupervised, Hybrid ANN Methods]
short_authors: Jush et al.
---
While content-based image retrieval (CBIR) has been extensively studied in
natural image retrieval, its application to medical images presents ongoing
challenges, primarily due to the 3D nature of medical images. Recent studies
have shown the potential use of pre-trained vision embeddings for CBIR in the
context of radiology image retrieval. However, a benchmark for the retrieval of
3D volumetric medical images is still lacking, hindering the ability to
objectively evaluate and compare the efficiency of proposed CBIR approaches in
medical imaging. In this study, we extend previous work and establish a
benchmark for region-based and localized multi-organ retrieval using the
TotalSegmentator dataset (TS) with detailed multi-organ annotations. We
benchmark embeddings derived from pre-trained supervised models on medical
images against embeddings derived from pre-trained unsupervised models on
non-medical images for 29 coarse and 104 detailed anatomical structures in
volume and region levels. For volumetric image retrieval, we adopt a late
interaction re-ranking method inspired by text matching. We compare it against
the original method proposed for volume and region retrieval and achieve a
retrieval recall of 1.0 for diverse anatomical regions with a wide size range.
The findings and methodologies presented in this paper provide insights and
benchmarks for further development and evaluation of CBIR approaches in the
context of medical imaging.