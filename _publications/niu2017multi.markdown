---
layout: publication
title: Multi-modal Multi-scale Deep Learning For Large-scale Image Annotation
authors: Yulei Niu, Zhiwu Lu, Ji-rong Wen, Tao Xiang, Shih-fu Chang
conference: IEEE Transactions on Image Processing
year: 2018
bibkey: niu2017multi
citations: 85
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.01220'}]
tags: ["Datasets", "Scalability"]
short_authors: Niu et al.
---
Image annotation aims to annotate a given image with a variable number of
class labels corresponding to diverse visual concepts. In this paper, we
address two main issues in large-scale image annotation: 1) how to learn a rich
feature representation suitable for predicting a diverse set of visual concepts
ranging from object, scene to abstract concept; 2) how to annotate an image
with the optimal number of class labels. To address the first issue, we propose
a novel multi-scale deep model for extracting rich and discriminative features
capable of representing a wide range of visual concepts. Specifically, a novel
two-branch deep neural network architecture is proposed which comprises a very
deep main network branch and a companion feature fusion network branch designed
for fusing the multi-scale features computed from the main branch. The deep
model is also made multi-modal by taking noisy user-provided tags as model
input to complement the image input. For tackling the second issue, we
introduce a label quantity prediction auxiliary task to the main label
prediction task to explicitly estimate the optimal label number for a given
image. Extensive experiments are carried out on two large-scale image
annotation benchmark datasets and the results show that our method
significantly outperforms the state-of-the-art.