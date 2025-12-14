---
layout: publication
title: 'Fashionsearchnet-v2: Learning Attribute Representations With Localization
  For Image Retrieval With Attribute Manipulation'
authors: Kenan E. Ak, Joo Hwee Lim, Ying Sun, Jo Yew Tham, Ashraf A. Kassim
conference: Arxiv
year: 2021
bibkey: ak2021fashionsearchnet
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.14145'}]
tags: [Distance Metric Learning, Supervised, Image Retrieval, Datasets]
short_authors: Ak et al.
---
The focus of this paper is on the problem of image retrieval with attribute
manipulation. Our proposed work is able to manipulate the desired attributes of
the query image while maintaining its other attributes. For example, the collar
attribute of the query image can be changed from round to v-neck to retrieve
similar images from a large dataset. A key challenge in e-commerce is that
images have multiple attributes where users would like to manipulate and it is
important to estimate discriminative feature representations for each of these
attributes. The proposed FashionSearchNet-v2 architecture is able to learn
attribute specific representations by leveraging on its weakly-supervised
localization module, which ignores the unrelated features of attributes in the
feature space, thus improving the similarity learning. The network is jointly
trained with the combination of attribute classification and triplet ranking
loss to estimate local representations. These local representations are then
merged into a single global representation based on the instructed attribute
manipulation where desired images can be retrieved with a distance metric. The
proposed method also provides explainability for its retrieval process to help
provide additional information on the attention of the network. Experiments
performed on several datasets that are rich in terms of the number of
attributes show that FashionSearchNet-v2 outperforms the other state-of-the-art
attribute manipulation techniques. Different than our earlier work
(FashionSearchNet), we propose several improvements in the learning procedure
and show that the proposed FashionSearchNet-v2 can be generalized to different
domains other than fashion.