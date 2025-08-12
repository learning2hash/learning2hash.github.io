---
layout: publication
title: 'Product1m: Towards Weakly Supervised Instance-level Product Retrieval Via
  Cross-modal Pretraining'
authors: Xunlin Zhan, Yangxin Wu, Xiao Dong, Yunchao Wei, Minlong Lu, Yichi Zhang,
  Hang Xu, Xiaodan Liang
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: zhan2021product1m
citations: 39
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.14572'}]
tags: ["ICCV", "Supervised"]
short_authors: Zhan et al.
---
Nowadays, customer's demands for E-commerce are more diversified, which
introduces more complications to the product retrieval industry. Previous
methods are either subject to single-modal input or perform supervised
image-level product retrieval, thus fail to accommodate real-life scenarios
where enormous weakly annotated multi-modal data are present. In this paper, we
investigate a more realistic setting that aims to perform weakly-supervised
multi-modal instance-level product retrieval among fine-grained product
categories. To promote the study of this challenging task, we contribute
Product1M, one of the largest multi-modal cosmetic datasets for real-world
instance-level retrieval. Notably, Product1M contains over 1 million
image-caption pairs and consists of two sample types, i.e., single-product and
multi-product samples, which encompass a wide variety of cosmetics brands. In
addition to the great diversity, Product1M enjoys several appealing
characteristics including fine-grained categories, complex combinations, and
fuzzy correspondence that well mimic the real-world scenes. Moreover, we
propose a novel model named Cross-modal contrAstive Product Transformer for
instance-level prodUct REtrieval (CAPTURE), that excels in capturing the
potential synergy between multi-modal inputs via a hybrid-stream transformer in
a self-supervised manner.CAPTURE generates discriminative instance features via
masked multi-modal learning as well as cross-modal contrastive pretraining and
it outperforms several SOTA cross-modal baselines. Extensive ablation studies
well demonstrate the effectiveness and the generalization capacity of our
model. Dataset and codes are available at https:
//github.com/zhanxlin/Product1M.