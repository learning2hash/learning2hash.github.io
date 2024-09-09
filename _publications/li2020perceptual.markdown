---
layout: publication
title: "Perceptual Robust Hashing for Color Images with Canonical Correlation Analysis"
authors: Li Xinran, Qin Chuan, Qian Zhenxing, Yao Heng, Zhang Xinpeng
conference: Arxiv
year: 2020
bibkey: li2020perceptual
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2012.04312"}
tags: ['ARXIV']
---
In this paper, a novel perceptual image hashing scheme for color images is proposed based on ring-ribbon quadtree and color vector angle. First, original image is subjected to normalization and Gaussian low-pass filtering to produce a secondary image, which is divided into a series of ring-ribbons with different radii and the same number of pixels. Then, both textural and color features are extracted locally and globally. Quadtree decomposition (QD) is applied on luminance values of the ring-ribbons to extract local textural features, and the gray level co-occurrence matrix (GLCM) is used to extract global textural features. Local color features of significant corner points on outer boundaries of ring-ribbons are extracted through color vector angles (CVA), and color low-order moments (CLMs) is utilized to extract global color features. Finally, two types of feature vectors are fused via canonical correlation analysis (CCA) to prodcue the final hash after scrambling. Compared with direct concatenation, the CCA feature fusion method improves classification performance, which better reflects overall correlation between two sets of feature vectors. Receiver operating characteristic (ROC) curve shows that our scheme has satisfactory performances with respect to robustness, discrimination and security, which can be effectively used in copy detection and content authentication.