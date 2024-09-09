---
layout: publication
title: "An Unsupervised Cross-Modal Hashing Method Robust to Noisy Training Image-Text Correspondences in Remote Sensing"
authors: Mikriukov Georgii, Ravanbakhsh Mahdyar, Demir Begüm
conference: Arxiv
year: 2022
bibkey: mikriukov2022an
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2202.13117"}
  - {name: "Paper", url: "https://git.tu-berlin.de/rsim/chnr"}
tags: ['ARXIV', 'Cross Modal', 'Supervised', 'Text Retrieval', 'Unsupervised']
---
The development of accurate and scalable cross-modal image-text retrieval methods, where queries from one modality (e.g., text) can be matched to archive entries from another (e.g., remote sensing image) has attracted great attention in remote sensing (RS). Most of the existing methods assume that a reliable multi-modal training set with accurately matched text-image pairs is existing. However, this assumption may not always hold since the multi-modal training sets may include noisy pairs (i.e., textual descriptions/captions associated to training images can be noisy), distorting the learning process of the retrieval methods. To address this problem, we propose a novel unsupervised cross-modal hashing method robust to the noisy image-text correspondences (CHNR). CHNR consists of three modules: 1) feature extraction module, which extracts feature representations of image-text pairs; 2) noise detection module, which detects potential noisy correspondences; and 3) hashing module that generates cross-modal binary hash codes. The proposed CHNR includes two training phases: i) meta-learning phase that uses a small portion of clean (i.e., reliable) data to train the noise detection module in an adversarial fashion; and ii) the main training phase for which the trained noise detection module is used to identify noisy correspondences while the hashing module is trained on the noisy multi-modal training set. Experimental results show that the proposed CHNR outperforms state-of-the-art methods. Our code is publicly available at https://git.tu-berlin.de/rsim/chnr