---
layout: publication
title: "Deep Unsupervised Image Hashing by Maximizing Bit Entropy"
authors: Yunqiang Li, Jan van Gemert
conference: AAAI
year: 2021
bibkey: andoni2006near
additional_links:
   - {name: "PDF", url: "https://arxiv.org/abs/2012.12334"}
   - {name: "Code", url: "https://github.com/liyunqianggyn/Deep-Unsupervised-Image-Hashing"}
tags: ['AAAI', 'Has Code', 'Image Retrieval', 'Supervised']
---
Unsupervised hashing is important for indexing huge image or video collections without having expensive annotations available. Hashing aims to learn short binary codes for compact storage and efficient semantic retrieval. We propose an unsupervised deep hashing layer called Bi-half Net that maximizes entropy of the binary codes. Entropy is maximal when both possible values of the bit are uniformly (half-half) distributed. To maximize bit entropy, we do not add a term to the loss function as this is difficult to optimize and tune. Instead, we design a new parameter-free network layer to explicitly force continuous image features to approximate the optimal half-half bit distribution. This layer is shown to minimize a penalized term of the Wasserstein distance between the learned continuous image features and the optimal half-half bit distribution. Experimental results on the image datasets Flickr25k, Nus-wide, Cifar-10, Mscoco, Mnist and the video datasets Ucf-101 and Hmdb-51 show that our approach leads to compact codes and compares favorably to the current state-of-the-art.
