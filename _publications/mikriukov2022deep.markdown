---
layout: publication
title: Deep Unsupervised Contrastive Hashing For Large45;scale Cross45;modal Text45;image Retrieval In Remote Sensing
authors: Mikriukov Georgii, Ravanbakhsh Mahdyar, Demir Begüm
conference: "Arxiv"
year: 2022
bibkey: mikriukov2022deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2201.08125"}
  - {name: "Code", url: "https://git.tu&#45;berlin.de/rsim/duch"}
tags: ['ARXIV', 'Has Code', 'Image Retrieval', 'Unsupervised']
---
Due to the availability of large45;scale multi45;modal data (e.g. satellite images acquired by different sensors text sentences etc) archives the development of cross45;modal retrieval systems that can search and retrieve semantically relevant data across different modalities based on a query in any modality has attracted great attention in RS. In this paper we focus our attention on cross45;modal text45;image retrieval where queries from one modality (e.g. text) can be matched to archive entries from another (e.g. image). Most of the existing cross45;modal text45;image retrieval systems require a high number of labeled training samples and also do not allow fast and memory45;efficient retrieval due to their intrinsic characteristics. These issues limit the applicability of the existing cross45;modal retrieval systems for large45;scale applications in RS. To address this problem in this paper we introduce a novel deep unsupervised cross45;modal contrastive hashing (DUCH) method for RS text45;image retrieval. The proposed DUCH is made up of two main modules 1) feature extraction module (which extracts deep representations of the text45;image modalities); and 2) hashing module (which learns to generate cross45;modal binary hash codes from the extracted representations). Within the hashing module we introduce a novel multi45;objective loss function including i) contrastive objectives that enable similarity preservation in both intra45; and inter45;modal similarities; ii) an adversarial objective that is enforced across two modalities for cross45;modal representation consistency; iii) binarization objectives for generating representative hash codes. Experimental results show that the proposed DUCH outperforms state45;of45;the45;art unsupervised cross45;modal hashing methods on two multi45;modal (image and text) benchmark archives in RS. Our code is publicly available at https://git.tu&#45;berlin.de/rsim/duch.
