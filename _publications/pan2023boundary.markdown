---
layout: publication
title: Boundary-aware Backward-compatible Representation Via Adversarial Learning
  In Image Retrieval
authors: Tan Pan, Furong Xu, Xudong Yang, Sifeng He, Chen Jiang, Qingpei Guo, Feng
  Qian Xiaobo Zhang, Yuan Cheng, Lei Yang, Wei Chu
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: pan2023boundary
citations: 7
additional_links: [{name: Code, url: 'https://github.com/Ashespt/AdvBCT'}, {name: Paper,
    url: 'https://arxiv.org/abs/2305.02610'}]
tags: ["CVPR", "Evaluation", "Image Retrieval", "Robustness", "Scalability"]
short_authors: Pan et al.
---
Image retrieval plays an important role in the Internet world. Usually, the
core parts of mainstream visual retrieval systems include an online service of
the embedding model and a large-scale vector database. For traditional model
upgrades, the old model will not be replaced by the new one until the
embeddings of all the images in the database are re-computed by the new model,
which takes days or weeks for a large amount of data. Recently,
backward-compatible training (BCT) enables the new model to be immediately
deployed online by making the new embeddings directly comparable to the old
ones. For BCT, improving the compatibility of two models with less negative
impact on retrieval performance is the key challenge. In this paper, we
introduce AdvBCT, an Adversarial Backward-Compatible Training method with an
elastic boundary constraint that takes both compatibility and discrimination
into consideration. We first employ adversarial learning to minimize the
distribution disparity between embeddings of the new model and the old model.
Meanwhile, we add an elastic boundary constraint during training to improve
compatibility and discrimination efficiently. Extensive experiments on GLDv2,
Revisited Oxford (ROxford), and Revisited Paris (RParis) demonstrate that our
method outperforms other BCT methods on both compatibility and discrimination.
The implementation of AdvBCT will be publicly available at
https://github.com/Ashespt/AdvBCT.