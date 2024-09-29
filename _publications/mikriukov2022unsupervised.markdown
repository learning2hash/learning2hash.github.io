---
layout: publication
title: Unsupervised Contrastive Hashing For Cross45;modal Retrieval In Remote Sensing
authors: Mikriukov Georgii, Ravanbakhsh Mahdyar, Demir Begüm
conference: "Arxiv"
year: 2022
bibkey: mikriukov2022unsupervised
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2204.08707"}
  - {name: "Code", url: "https://git.tu&#45;berlin.de/rsim/duch"}
tags: ['ARXIV', 'Has Code', 'Image Retrieval', 'Unsupervised']
---
The development of cross45;modal retrieval systems that can search and retrieve semantically relevant data across different modalities based on a query in any modality has attracted great attention in remote sensing (RS). In this paper we focus our attention on cross45;modal text45;image retrieval where queries from one modality (e.g. text) can be matched to archive entries from another (e.g. image). Most of the existing cross45;modal text45;image retrieval systems in RS require a high number of labeled training samples and also do not allow fast and memory45;efficient retrieval. These issues limit the applicability of the existing cross45;modal retrieval systems for large45;scale applications in RS. To address this problem in this paper we introduce a novel unsupervised cross45;modal contrastive hashing (DUCH) method for text45;image retrieval in RS. To this end the proposed DUCH is made up of two main modules 1) feature extraction module which extracts deep representations of two modalities; 2) hashing module that learns to generate cross45;modal binary hash codes from the extracted representations. We introduce a novel multi45;objective loss function including i) contrastive objectives that enable similarity preservation in intra45; and inter45;modal similarities; ii) an adversarial objective that is enforced across two modalities for cross45;modal representation consistency; and iii) binarization objectives for generating hash codes. Experimental results show that the proposed DUCH outperforms state45;of45;the45;art methods. Our code is publicly available at https://git.tu&#45;berlin.de/rsim/duch.
