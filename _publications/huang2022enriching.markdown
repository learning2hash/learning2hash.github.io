---
layout: publication
title: Enriching Unsupervised User Embedding Via Medical Concepts
authors: Xiaolei Huang, Franck Dernoncourt, Mark Dredze
conference: Arxiv
year: 2022
bibkey: huang2022enriching
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.10627'}]
tags: ["Unsupervised"]
short_authors: Xiaolei Huang, Franck Dernoncourt, Mark Dredze
---
Clinical notes in Electronic Health Records (EHR) present rich documented
information of patients to inference phenotype for disease diagnosis and study
patient characteristics for cohort selection. Unsupervised user embedding aims
to encode patients into fixed-length vectors without human supervisions.
Medical concepts extracted from the clinical notes contain rich connections
between patients and their clinical categories. However, existing unsupervised
approaches of user embeddings from clinical notes do not explicitly incorporate
medical concepts. In this study, we propose a concept-aware unsupervised user
embedding that jointly leverages text documents and medical concepts from two
clinical corpora, MIMIC-III and Diabetes. We evaluate user embeddings on both
extrinsic and intrinsic tasks, including phenotype classification, in-hospital
mortality prediction, patient retrieval, and patient relatedness. Experiments
on the two clinical corpora show our approach exceeds unsupervised baselines,
and incorporating medical concepts can significantly improve the baseline
performance.