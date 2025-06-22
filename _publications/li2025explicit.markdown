---
layout: publication
title: 'Finecir: Explicit Parsing Of Fine-grained Modification Semantics For Composed
  Image Retrieval'
authors: Zixu Li et al.
conference: Arxiv
year: 2025
citations: 0
bibkey: li2025explicit
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.21309'}, {name: Code,
    url: 'https://github.com/SDU-L/FineCIR.git'}]
tags: [Applications, ECIR, Tools and Libraries, ANN Search, Evaluation Metrics, Benchmarks
    and Datasets, Has Code]
---
Composed Image Retrieval (CIR) facilitates image retrieval through a
multimodal query consisting of a reference image and modification text. The
reference image defines the retrieval context, while the modification text
specifies desired alterations. However, existing CIR datasets predominantly
employ coarse-grained modification text (CoarseMT), which inadequately captures
fine-grained retrieval intents. This limitation introduces two key challenges:
(1) ignoring detailed differences leads to imprecise positive samples, and (2)
greater ambiguity arises when retrieving visually similar images. These issues
degrade retrieval accuracy, necessitating manual result filtering or repeated
queries. To address these limitations, we develop a robust fine-grained CIR
data annotation pipeline that minimizes imprecise positive samples and enhances
CIR systems' ability to discern modification intents accurately. Using this
pipeline, we refine the FashionIQ and CIRR datasets to create two fine-grained
CIR datasets: Fine-FashionIQ and Fine-CIRR. Furthermore, we introduce FineCIR,
the first CIR framework explicitly designed to parse the modification text.
FineCIR effectively captures fine-grained modification semantics and aligns
them with ambiguous visual entities, enhancing retrieval precision. Extensive
experiments demonstrate that FineCIR consistently outperforms state-of-the-art
CIR baselines on both fine-grained and traditional CIR benchmark datasets. Our
FineCIR code and fine-grained CIR datasets are available at
https://github.com/SDU-L/FineCIR.git.