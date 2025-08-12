---
layout: publication
title: 'Learning To Focus: Cascaded Feature Matching Network For Few-shot Image Recognition'
authors: Mengting Chen, Xinggang Wang, Heng Luo, Yifeng Geng, Wenyu Liu
conference: Science China Information Sciences
year: 2021
bibkey: chen2021learning
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.05018'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Chen et al.
---
Deep networks can learn to accurately recognize objects of a category by
training on a large number of annotated images. However, a meta-learning
challenge known as a low-shot image recognition task comes when only a few
images with annotations are available for learning a recognition model for one
category. The objects in testing/query and training/support images are likely
to be different in size, location, style, and so on. Our method, called
Cascaded Feature Matching Network (CFMN), is proposed to solve this problem. We
train the meta-learner to learn a more fine-grained and adaptive deep distance
metric by focusing more on the features that have high correlations between
compared images by the feature matching block which can align associated
features together and naturally ignore those non-discriminative features. By
applying the proposed feature matching block in different layers of the
few-shot recognition network, multi-scale information among the compared images
can be incorporated into the final cascaded matching feature, which boosts the
recognition performance further and generalizes better by learning on
relationships. The experiments for few-shot learning on two standard datasets,
*mini*ImageNet and Omniglot, have confirmed the effectiveness of our
method. Besides, the multi-label few-shot task is first studied on a new data
split of COCO which further shows the superiority of the proposed feature
matching network when performing few-shot learning in complex images. The code
will be made publicly available.