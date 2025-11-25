---
layout: publication
title: 'Revisiting CLIP: Efficient Alignment Of 3D MRI And Tabular Data Using Domain-specific
  Foundation Models'
authors: "Jakob Krogh Petersen, Valdemar Licht, Mads Nielsen, Asbj\xF8rn Munk"
conference: 2025 IEEE 22nd International Symposium on Biomedical Imaging (ISBI)
year: 2025
bibkey: petersen2025revisiting
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.14051'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Petersen et al.
---
Multi-modal models require aligned, shared embedding spaces. However, common
CLIP-based approaches need large amounts of samples and do not natively support
3D or tabular data, both of which are crucial in the medical domain. To address
these issues, we revisit CLIP-style alignment by training a domain-specific 3D
foundation model as an image encoder and demonstrate that modality alignment is
feasible with only 62 MRI scans. Our approach is enabled by a simple embedding
accumulation strategy required for training in 3D, which scales the amount of
negative pairs across batches in order to stabilize training. We perform a
thorough evaluation of various design choices, including the choice of backbone
and loss functions, and evaluate the proposed methodology on zero-shot
classification and image-retrieval tasks. While zero-shot image-retrieval
remains challenging, zero-shot classification results demonstrate that the
proposed approach can meaningfully align the representations of 3D MRI with
tabular data.