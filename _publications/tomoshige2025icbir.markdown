---
layout: publication
title: 'Icbir-sli: Interpretable Content-based Image Retrieval With 2D Slice Embeddings'
authors: Shuhei Tomoshige, Hayato Muraki, Kenichi Oishi, Hitoshi Iyatomi
conference: 'Medical Imaging 2025: Image Processing'
year: 2025
bibkey: tomoshige2025icbir
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.01642'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Robustness"]
short_authors: Tomoshige et al.
---
Current methods for searching brain MR images rely on text-based approaches,
highlighting a significant need for content-based image retrieval (CBIR)
systems. Directly applying 3D brain MR images to machine learning models offers
the benefit of effectively learning the brain's structure; however, building
the generalized model necessitates a large amount of training data. While
models that consider depth direction and utilize continuous 2D slices have
demonstrated success in segmentation and classification tasks involving 3D
data, concerns remain. Specifically, using general 2D slices may lead to the
oversight of pathological features and discontinuities in depth direction
information. Furthermore, to the best of the authors' knowledge, there have
been no attempts to develop a practical CBIR system that preserves the entire
brain's structural information. In this study, we propose an interpretable CBIR
method for brain MR images, named iCBIR-Sli (Interpretable CBIR with 2D Slice
Embedding), which, for the first time globally, utilizes a series of 2D slices.
iCBIR-Sli addresses the challenges associated with using 2D slices by
effectively aggregating slice information, thereby achieving low-dimensional
representations with high completeness, usability, robustness, and
interoperability, which are qualities essential for effective CBIR. In
retrieval evaluation experiments utilizing five publicly available brain MR
datasets (ADNI2/3, OASIS3/4, AIBL) for Alzheimer's disease and cognitively
normal, iCBIR-Sli demonstrated top-1 retrieval performance (macro F1 = 0.859),
comparable to existing deep learning models explicitly designed for
classification, without the need for an external classifier. Additionally, the
method provided high interpretability by clearly identifying the brain regions
indicative of the searched-for disease.