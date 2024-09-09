---
layout: publication
title: "Learning Global and Local Consistent Representations for Unsupervised Image Retrieval via Deep Graph Diffusion Networks"
authors: Dou Zhiyong, Cui Haotian, Zhang Lin, Wang Bo
conference: Arxiv
year: 2020
bibkey: dou2020learning
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2001.01284"}
tags: ['ARXIV', 'Deep Learning', 'Graph', 'Image Retrieval', 'Supervised', 'Unsupervised']
---
Diffusion has shown great success in improving accuracy of unsupervised image retrieval systems by utilizing high-order structures of image manifold. However, existing diffusion methods suffer from three major limitations: 1) they usually rely on local structures without considering global manifold information; 2) they focus on improving pair-wise similarities within existing images input output transductively while lacking flexibility to learn representations for novel unseen instances inductively; 3) they fail to scale to large datasets due to prohibitive memory consumption and computational burden due to intrinsic high-order operations on the whole graph. In this paper, to address these limitations, we propose a novel method, Graph Diffusion Networks (GRAD-Net), that adopts graph neural networks (GNNs), a novel variant of deep learning algorithms on irregular graphs. GRAD-Net learns semantic representations by exploiting both local and global structures of image manifold in an unsupervised fashion. By utilizing sparse coding techniques, GRAD-Net not only preserves global information on the image manifold, but also enables scalable training and efficient querying. Experiments on several large benchmark datasets demonstrate effectiveness of our method over state-of-the-art diffusion algorithms for unsupervised image retrieval.