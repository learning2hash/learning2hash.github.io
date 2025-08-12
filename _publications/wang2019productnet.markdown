---
layout: publication
title: 'Productnet: A Collection Of High-quality Datasets For Product Representation
  Learning'
authors: Chu Wang, Lei Tang, Yang Lu, Shujun Bian, Hirohisa Fujita, da Zhang, Zuohua
  Zhang, Yongning Wu
conference: Companion Proceedings of The 2019 World Wide Web Conference
year: 2019
bibkey: wang2019productnet
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.09037'}]
tags: ["Datasets"]
short_authors: Wang et al.
---
ProductNet is a collection of high-quality product datasets for better
product understanding. Motivated by ImageNet, ProductNet aims at supporting
product representation learning by curating product datasets of high quality
with properly chosen taxonomy. In this paper, the two goals of building
high-quality product datasets and learning product representation support each
other in an iterative fashion: the product embedding is obtained via a
multi-modal deep neural network (master model) designed to leverage product
image and catalog information; and in return, the embedding is utilized via
active learning (local model) to vastly accelerate the annotation process. For
the labeled data, the proposed master model yields high categorization accuracy
(94.7% top-1 accuracy for 1240 classes), which can be used as search indices,
partition keys, and input features for machine learning models. The product
embedding, as well as the fined-tuned master model for a specific business
task, can also be used for various transfer learning tasks.