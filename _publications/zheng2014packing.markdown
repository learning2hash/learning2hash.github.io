---
layout: publication
title: 'Packing And Padding: Coupled Multi-index For Accurate Image Retrieval'
authors: Liang Zheng, Shengjin Wang, Ziqiong Liu, Qi Tian
conference: "Arxiv"
year: 2014
citations: 140
bibkey: zheng2014packing
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1402.2681'}
tags: ['Cross-Modal', 'Deep', 'Quantisation', 'Retrieval Models', 'Datasets', 'Quantization', 'Applications']
---
In Bag-of-Words (BoW) based image retrieval, the SIFT visual word has a low
discriminative power, so false positive matches occur prevalently. Apart from
the information loss during quantization, another cause is that the SIFT
feature only describes the local gradient distribution. To address this
problem, this paper proposes a coupled Multi-Index (c-MI) framework to perform
feature fusion at indexing level. Basically, complementary features are coupled
into a multi-dimensional inverted index. Each dimension of c-MI corresponds to
one kind of feature, and the retrieval process votes for images similar in both
SIFT and other feature spaces. Specifically, we exploit the fusion of local
color feature into c-MI. While the precision of visual match is greatly
enhanced, we adopt Multiple Assignment to improve recall. The joint cooperation
of SIFT and color features significantly reduces the impact of false positive
matches.
  Extensive experiments on several benchmark datasets demonstrate that c-MI
improves the retrieval accuracy significantly, while consuming only half of the
query time compared to the baseline. Importantly, we show that c-MI is well
complementary to many prior techniques. Assembling these methods, we have
obtained an mAP of 85.8% and N-S score of 3.85 on Holidays and Ukbench
datasets, respectively, which compare favorably with the state-of-the-arts.
