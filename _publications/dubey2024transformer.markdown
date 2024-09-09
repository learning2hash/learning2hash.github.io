---
layout: publication
title: Transformer-based Clipped Contrastive Quantization Learning for Unsupervised Image Retrieval
authors: Dubey Ayush, Dubey Shiv Ram, Singh Satish Kumar, Chu Wei-Ta
conference: "Arxiv"
year: 2024
bibkey: dubey2024transformer
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2401.15362"}
tags: ['ARXIV', 'CNN', 'Image Retrieval', 'Quantisation', 'Self Supervised', 'Supervised', 'Unsupervised']
---
Unsupervised image retrieval aims to learn the important visual characteristics without any given level to retrieve the similar images for a given query image. The Convolutional Neural Network (CNN)-based approaches have been extensively exploited with self-supervised contrastive learning for image hashing. However, the existing approaches suffer due to lack of effective utilization of global features by CNNs and biased-ness created by false negative pairs in the contrastive learning. In this paper, we propose a TransClippedCLR model by encoding the global context of an image using Transformer having local context through patch based processing, by generating the hash codes through product quantization and by avoiding the potential false negative pairs through clipped contrastive learning. The proposed model is tested with superior performance for unsupervised image retrieval on benchmark datasets, including CIFAR10, NUS-Wide and Flickr25K, as compared to the recent state-of-the-art deep models. The results using the proposed clipped contrastive learning are greatly improved on all datasets as compared to same backbone network with vanilla contrastive learning.
