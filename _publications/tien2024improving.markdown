---
layout: publication
title: Improving Vietnamese Legal Document Retrieval Using Synthetic Data
authors: Son Pham Tien, Hieu Nguyen Doan, An Nguyen Dai, Sang Dinh Viet
conference: Arxiv
year: 2024
bibkey: tien2024improving
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.00657'}]
tags: ["Datasets", "Distance Metric Learning", "Text Retrieval"]
short_authors: Tien et al.
---
In the field of legal information retrieval, effective embedding-based models
are essential for accurate question-answering systems. However, the scarcity of
large annotated datasets poses a significant challenge, particularly for
Vietnamese legal texts. To address this issue, we propose a novel approach that
leverages large language models to generate high-quality, diverse synthetic
queries for Vietnamese legal passages. This synthetic data is then used to
pre-train retrieval models, specifically bi-encoder and ColBERT, which are
further fine-tuned using contrastive loss with mined hard negatives. Our
experiments demonstrate that these enhancements lead to strong improvement in
retrieval accuracy, validating the effectiveness of synthetic data and
pre-training techniques in overcoming the limitations posed by the lack of
large labeled datasets in the Vietnamese legal domain.