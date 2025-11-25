---
layout: publication
title: 'BIOMEDICA: An Open Biomedical Image-caption Archive, Dataset, And Vision-language
  Models Derived From Scientific Literature'
authors: Alejandro Lozano, Min Woo Sun, James Burgess, Liangyu Chen, Jeffrey J Nirschl,
  Jeffrey Gu, Ivan Lopez, Josiah Aklilu, Austin Wolfgang Katzer, Collin Chiu, Anita
  Rau, Xiaohan Wang, Yuhui Zhang, Alfred Seunghoon Song, Robert Tibshirani, Serena
  Yeung-Levy
conference: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2025
bibkey: lozano2025biomedica
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.07171'}]
tags: ["CVPR", "Datasets", "Scalability"]
short_authors: Lozano et al.
---
The development of vision-language models (VLMs) is driven by large-scale and
diverse multimodal datasets. However, progress toward generalist biomedical
VLMs is limited by the lack of annotated, publicly accessible datasets across
biology and medicine. Existing efforts are restricted to narrow domains,
missing the full diversity of biomedical knowledge encoded in scientific
literature. To address this gap, we introduce BIOMEDICA, a scalable,
open-source framework to extract, annotate, and serialize the entirety of the
PubMed Central Open Access subset into an easy-to-use, publicly accessible
dataset. Our framework produces a comprehensive archive with over 24 million
unique image-text pairs from over 6 million articles. Metadata and
expert-guided annotations are also provided. We demonstrate the utility and
accessibility of our resource by releasing BMCA-CLIP, a suite of CLIP-style
models continuously pre-trained on the BIOMEDICA dataset via streaming,
eliminating the need to download 27 TB of data locally. On average, our models
achieve state-of-the-art performance across 40 tasks - spanning pathology,
radiology, ophthalmology, dermatology, surgery, molecular biology,
parasitology, and cell biology - excelling in zero-shot classification with a
6.56% average improvement (as high as 29.8% and 17.5% in dermatology and
ophthalmology, respectively), and stronger image-text retrieval, all while
using 10x less compute. To foster reproducibility and collaboration, we release
our codebase and dataset for the broader research community.