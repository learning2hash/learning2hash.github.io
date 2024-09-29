---
layout: publication
title: Tiny Descriptors For Image Retrieval With Unsupervised Triplet Hashing
authors: Lin Jie, Morère Olivier, Petta Julie, Chandrasekhar Vijay, Veillard Antoine
conference: "Arxiv"
year: 2015
bibkey: lin2015tiny
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1511.03055"}
tags: ['ARXIV', 'Deep Learning', 'Image Retrieval', 'Unsupervised']
---
A typical image retrieval pipeline starts with the comparison of global descriptors from a large database to find a short list of candidate matches. A good image descriptor is key to the retrieval pipeline and should reconcile two contradictory requirements providing recall rates as high as possible and being as compact as possible for fast matching. Following the recent successes of Deep Convolutional Neural Networks (DCNN) for large scale image classification descriptors extracted from DCNNs are increasingly used in place of the traditional hand crafted descriptors such as Fisher Vectors (FV) with better retrieval performances. Nevertheless the dimensionality of a typical DCNN descriptor 45;45;extracted either from the visual feature pyramid or the fully45;connected layers45;45; remains quite high at several thousands of scalar values. In this paper we propose Unsupervised Triplet Hashing (UTH) a fully unsupervised method to compute extremely compact binary hashes 45;45;in the 3245;256 bits range45;45; from high45;dimensional global descriptors. UTH consists of two successive deep learning steps. First Stacked Restricted Boltzmann Machines (SRBM) a type of unsupervised deep neural nets are used to learn binary embedding functions able to bring the descriptor size down to the desired bitrate. SRBMs are typically able to ensure a very high compression rate at the expense of loosing some desirable metric properties of the original DCNN descriptor space. Then triplet networks a rank learning scheme based on weight sharing nets is used to fine45;tune the binary embedding functions to retain as much as possible of the useful metric properties of the original space. A thorough empirical evaluation conducted on multiple publicly available dataset using DCNN descriptors shows that our method is able to significantly outperform state45;of45;the45;art unsupervised schemes in the target bit range.
