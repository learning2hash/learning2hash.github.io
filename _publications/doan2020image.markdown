---
layout: publication
title: Image Hashing By Minimizing Discrete Component45;wise Wasserstein Distance
authors: Doan Khoa D., Manchanda Saurav, Badirli Sarkhan, Reddy Chandan K.
conference: "Arxiv"
year: 2020
bibkey: doan2020image
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2003.00134"}
  - {name: "Code", url: "https://github.com/khoadoan/adversarial&#45;hashing)"}
tags: ['ARXIV', 'Has Code', 'Image Retrieval', 'Unsupervised']
---
Image hashing is one of the fundamental problems that demand both efficient and effective solutions for various practical scenarios. Adversarial autoencoders are shown to be able to implicitly learn a robust locality45;preserving hash function that generates balanced and high45;quality hash codes. However the existing adversarial hashing methods are inefficient to be employed for large45;scale image retrieval applications. Specifically they require an exponential number of samples to be able to generate optimal hash codes and a significantly high computational cost to train. In this paper we show that the high sample45;complexity requirement often results in sub45;optimal retrieval performance of the adversarial hashing methods. To address this challenge we propose a new adversarial45;autoencoder hashing approach that has a much lower sample requirement and computational cost. Specifically by exploiting the desired properties of the hash function in the low45;dimensional discrete space our method efficiently estimates a better variant of Wasserstein distance by averaging a set of easy45;to45;compute one45;dimensional Wasserstein distances. The resulting hashing approach has an order45;of45;magnitude better sample complexity thus better generalization property compared to the other adversarial hashing methods. In addition the computational cost is significantly reduced using our approach. We conduct experiments on several real45;world datasets and show that the proposed method outperforms the competing hashing methods achieving up to 1037; improvement over the current state45;of45;the45;art image hashing methods. The code accompanying this paper is available on Github (https://github.com/khoadoan/adversarial&#45;hashing).
