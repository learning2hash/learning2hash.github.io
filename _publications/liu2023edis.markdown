---
layout: publication
title: 'EDIS: Entity-driven Image Search Over Multimodal Web Content'
authors: Siqi Liu, Weixi Feng, Tsu-Jui Fu, Wenhu Chen, William Yang Wang
conference: Proceedings of the 2023 Conference on Empirical Methods in Natural Language
  Processing
year: 2023
bibkey: liu2023edis
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.13631'}]
tags: ["EMNLP", "Image Retrieval"]
short_authors: Liu et al.
---
Making image retrieval methods practical for real-world search applications
requires significant progress in dataset scales, entity comprehension, and
multimodal information fusion. In this work, we introduce
\textbf\{E\}ntity-\textbf\{D\}riven \textbf\{I\}mage \textbf\{S\}earch (EDIS), a
challenging dataset for cross-modal image search in the news domain. EDIS
consists of 1 million web images from actual search engine results and curated
datasets, with each image paired with a textual description. Unlike datasets
that assume a small set of single-modality candidates, EDIS reflects real-world
web image search scenarios by including a million multimodal image-text pairs
as candidates. EDIS encourages the development of retrieval models that
simultaneously address cross-modal information fusion and matching. To achieve
accurate ranking results, a model must: 1) understand named entities and events
from text queries, 2) ground entities onto images or text descriptions, and 3)
effectively fuse textual and visual representations. Our experimental results
show that EDIS challenges state-of-the-art methods with dense entities and a
large-scale candidate set. The ablation study also proves that fusing textual
features with visual features is critical in improving retrieval results.