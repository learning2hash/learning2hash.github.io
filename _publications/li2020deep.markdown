---
layout: publication
title: Deep Unsupervised Image Hashing By Maximizing Bit Entropy
authors: Li Yunqiang, Van Gemert Jan
conference: "Arxiv"
year: 2020
bibkey: li2020deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2012.12334"}
tags: ['ARXIV', 'Unsupervised']
---
Unsupervised hashing is important for indexing huge image or video collections without having expensive annotations available. Hashing aims to learn short binary codes for compact storage and efficient semantic retrieval. We propose an unsupervised deep hashing layer called Bi45;half Net that maximizes entropy of the binary codes. Entropy is maximal when both possible values of the bit are uniformly (half45;half) distributed. To maximize bit entropy we do not add a term to the loss function as this is difficult to optimize and tune. Instead we design a new parameter45;free network layer to explicitly force continuous image features to approximate the optimal half45;half bit distribution. This layer is shown to minimize a penalized term of the Wasserstein distance between the learned continuous image features and the optimal half45;half bit distribution. Experimental results on the image datasets Flickr25k Nus45;wide Cifar45;10 Mscoco Mnist and the video datasets Ucf45;101 and Hmdb45;51 show that our approach leads to compact codes and compares favorably to the current state45;of45;the45;art.
