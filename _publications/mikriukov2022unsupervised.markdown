---
layout: publication
title: Unsupervised Contrastive Hashing for Cross-Modal Retrieval in Remote Sensing
authors: Mikriukov Georgii, Ravanbakhsh Mahdyar, Demir Begüm
conference: "Arxiv"
year: 2022
bibkey: mikriukov2022unsupervised
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2204.08707"}
tags: ['ARXIV', 'Cross Modal', 'Image Retrieval', 'Supervised', 'Unsupervised']
---
The development of cross-modal retrieval systems that can search and retrieve semantically relevant data across different modalities based on a query in any modality has attracted great attention in remote sensing (RS). In this paper, we focus our attention on cross-modal text-image retrieval, where queries from one modality (e.g., text) can be matched to archive entries from another (e.g., image). Most of the existing cross-modal text-image retrieval systems in RS require a high number of labeled training samples and also do not allow fast and memory-efficient retrieval. These issues limit the applicability of the existing cross-modal retrieval systems for large-scale applications in RS. To address this problem, in this paper we introduce a novel unsupervised cross-modal contrastive hashing (DUCH) method for text-image retrieval in RS. To this end, the proposed DUCH is made up of two main modules 1) feature extraction module, which extracts deep representations of two modalities; 2) hashing module that learns to generate cross-modal binary hash codes from the extracted representations. We introduce a novel multi-objective loss function including i) contrastive objectives that enable similarity preservation in intra- and inter-modal similarities; ii) an adversarial objective that is enforced across two modalities for cross-modal representation consistency; and iii) binarization objectives for generating hash codes. Experimental results show that the proposed DUCH outperforms state-of-the-art methods. Our code is publicly available at https//git.tu-berlin.de/rsim/duch.
