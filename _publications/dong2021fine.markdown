---
layout: publication
title: Fine-grained Fashion Similarity Prediction By Attribute-specific Embedding
  Learning
authors: Jianfeng Dong, Zhe Ma, Xiaofeng Mao, Xun Yang, Yuan He, Richang Hong, Shouling
  Ji
conference: IEEE Transactions on Image Processing
year: 2021
bibkey: dong2021fine
citations: 33
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2104.02429'}]
tags: ["Datasets"]
short_authors: Dong et al.
---
This paper strives to predict fine-grained fashion similarity. In this
similarity paradigm, one should pay more attention to the similarity in terms
of a specific design/attribute between fashion items. For example, whether the
collar designs of the two clothes are similar. It has potential value in many
fashion related applications, such as fashion copyright protection. To this
end, we propose an Attribute-Specific Embedding Network (ASEN) to jointly learn
multiple attribute-specific embeddings, thus measure the fine-grained
similarity in the corresponding space. The proposed ASEN is comprised of a
global branch and a local branch. The global branch takes the whole image as
input to extract features from a global perspective, while the local branch
takes as input the zoomed-in region-of-interest (RoI) w.r.t. the specified
attribute thus able to extract more fine-grained features. As the global branch
and the local branch extract the features from different perspectives, they are
complementary to each other. Additionally, in each branch, two attention
modules, i.e., Attribute-aware Spatial Attention and Attribute-aware Channel
Attention, are integrated to make ASEN be able to locate the related regions
and capture the essential patterns under the guidance of the specified
attribute, thus make the learned attribute-specific embeddings better reflect
the fine-grained similarity. Extensive experiments on three fashion-related
datasets, i.e., FashionAI, DARN, and DeepFashion, show the effectiveness of
ASEN for fine-grained fashion similarity prediction and its potential for
fashion reranking. Code and data are available at
https://github.com/maryeon/asenpp .