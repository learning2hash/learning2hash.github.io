---
layout: publication
title: Aggregation Schemes For Single-vector WSI Representation Learning In Digital
  Pathology
authors: Sobhan Hemati, Ghazal Alabtah, Saghir Alfasly, H. R. Tizhoosh
conference: Arxiv
year: 2025
bibkey: hemati2025aggregation
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.17822'}]
tags: [Evaluation]
short_authors: Hemati et al.
---
A crucial step to efficiently integrate Whole Slide Images (WSIs) in computational pathology is assigning a single high-quality feature vector, i.e., one embedding, to each WSI. With the existence of many pre-trained deep neural networks and the emergence of foundation models, extracting embeddings for sub-images (i.e., tiles or patches) is straightforward. However, for WSIs, given their high resolution and gigapixel nature, inputting them into existing GPUs as a single image is not feasible. As a result, WSIs are usually split into many patches. Feeding each patch to a pre-trained model, each WSI can then be represented by a set of patches, hence, a set of embeddings. Hence, in such a setup, WSI representation learning reduces to set representation learning where for each WSI we have access to a set of patch embeddings. To obtain a single embedding from a set of patch embeddings for each WSI, multiple set-based learning schemes have been proposed in the literature. In this paper, we evaluate the WSI search performance of multiple recently developed aggregation techniques (mainly set representation learning techniques) including simple average or max pooling operations, Deep Sets, Memory networks, Focal attention, Gaussian Mixture Model (GMM) Fisher Vector, and deep sparse and binary Fisher Vector on four different primary sites including bladder, breast, kidney, and Colon from TCGA. Further, we benchmark the search performance of these methods against the median of minimum distances of patch embeddings, a non-aggregating approach used for WSI retrieval.