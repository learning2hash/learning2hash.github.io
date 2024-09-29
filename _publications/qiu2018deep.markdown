---
layout: publication
title: Deep Semantic Hashing With Generative Adversarial Networks
authors: Qiu Zhaofan, Pan Yingwei, Yao Ting, Mei Tao
conference: "Arxiv"
year: 2018
bibkey: qiu2018deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1804.08275"}
tags: ['ARXIV', 'CNN', 'Image Retrieval', 'Supervised']
---
Hashing has been a widely45;adopted technique for nearest neighbor search in large45;scale image retrieval tasks. Recent research has shown that leveraging supervised information can lead to high quality hashing. However the cost of annotating data is often an obstacle when applying supervised hashing to a new domain. Moreover the results can suffer from the robustness problem as the data at training and test stage could come from similar but different distributions. This paper studies the exploration of generating synthetic data through semi45;supervised generative adversarial networks (GANs) which leverages largely unlabeled and limited labeled training data to produce highly compelling data with intrinsic invariance and global coherence for better understanding statistical structures of natural data. We demonstrate that the above two limitations can be well mitigated by applying the synthetic data for hashing. Specifically a novel deep semantic hashing with GANs (DSH45;GANs) is presented which mainly consists of four components a deep convolution neural networks (CNN) for learning image representations an adversary stream to distinguish synthetic images from real ones a hash stream for encoding image representations to hash codes and a classification stream. The whole architecture is trained end45;to45;end by jointly optimizing three losses i.e. adversarial loss to correct label of synthetic or real for each sample triplet ranking loss to preserve the relative similarity ordering in the input real45;synthetic triplets and classification loss to classify each sample accurately. Extensive experiments conducted on both CIFAR45;10 and NUS45;WIDE image benchmarks validate the capability of exploiting synthetic images for hashing. Our framework also achieves superior results when compared to state45;of45;the45;art deep hash models.
