---
layout: publication
title: 'JESTR: Joint Embedding Space Technique For Ranking Candidate Molecules For
  The Annotation Of Untargeted Metabolomics Data'
authors: Apurva Kalia, Yan Zhou Chen, Dilip Krishnan, Soha Hassoun
conference: Arxiv
year: 2024
bibkey: kalia2024jestr
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.14464'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation"]
short_authors: Kalia et al.
---
Motivation: A major challenge in metabolomics is annotation: assigning molecular structures to mass spectral fragmentation patterns. Despite recent advances in molecule-to-spectra and in spectra-to-molecular fingerprint prediction (FP), annotation rates remain low. Results: We introduce in this paper a novel paradigm (JESTR) for annotation. Unlike prior approaches that explicitly construct molecular fingerprints or spectra, JESTR leverages the insight that molecules and their corresponding spectra are views of the same data and effectively embeds their representations in a joint space. Candidate structures are ranked based on cosine similarity between the embeddings of query spectrum and each candidate. We evaluate JESTR against mol-to-spec and spec-to-FP annotation tools on three datasets. On average, for rank@[1-5], JESTR outperforms other tools by 23.6%-71.6%. We further demonstrate the strong value of regularization with candidate molecules during training, boosting rank@1 performance by 11.4% and enhancing the model's ability to discern between target and candidate molecules. When comparing JESTR's performance against that of publicly available pretrained models of SIRIUS and CFM-ID on appropriate subsets of MassSpecGym benchmark dataset, JESTR outperforms these tools by 31% and 238%, respectively. Through JESTR, we offer a novel promising avenue towards accurate annotation, therefore unlocking valuable insights into the metabolome.