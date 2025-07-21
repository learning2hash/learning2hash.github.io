---
layout: publication
title: Directional Statistics-based Deep Metric Learning for Image Classification
  and Retrieval
authors: Zhe Xuefei, Chen Shifeng, Yan Hong
conference: Pattern Recognition
year: 2019
bibkey: zhe2018directional
citations: 72
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.09662'}]
tags: ["CVPR", "Distance-Metric-Learning"]
---
Deep distance metric learning (DDML), which is proposed to learn image
similarity metrics in an end-to-end manner based on the convolution neural
network, has achieved encouraging results in many computer vision
tasks.\\(L2\\)-normalization in the embedding space has been used to improve the
performance of several DDML methods. However, the commonly used Euclidean
distance is no longer an accurate metric for \\(L2\\)-normalized embedding space,
i.e., a hyper-sphere. Another challenge of current DDML methods is that their
loss functions are usually based on rigid data formats, such as the triplet
tuple. Thus, an extra process is needed to prepare data in specific formats. In
addition, their losses are obtained from a limited number of samples, which
leads to a lack of the global view of the embedding space. In this paper, we
replace the Euclidean distance with the cosine similarity to better utilize the
\\(L2\\)-normalization, which is able to attenuate the curse of dimensionality.
More specifically, a novel loss function based on the von Mises-Fisher
distribution is proposed to learn a compact hyper-spherical embedding space.
Moreover, a new efficient learning algorithm is developed to better capture the
global structure of the embedding space. Experiments for both classification
and retrieval tasks on several standard datasets show that our method achieves
state-of-the-art performance with a simpler training procedure. Furthermore, we
demonstrate that, even with a small number of convolutional layers, our model
can still obtain significantly better classification performance than the
widely used softmax loss.