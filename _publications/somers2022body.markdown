---
layout: publication
title: Body Part-based Representation Learning For Occluded Person Re-identification
authors: Vladimir Somers, Christophe de Vleeschouwer, Alexandre Alahi
conference: Proceedings of the 2023 IEEE/CVF Winter Conference on Applications of
  Computer Vision (WACV23)
year: 2022
bibkey: somers2022body
citations: 13
additional_links: [{name: Code, url: 'https://github.com/VlSomers/bpbreid'}, {name: Paper,
    url: 'https://arxiv.org/abs/2211.03679'}]
tags: [Evaluation, Datasets]
short_authors: Vladimir Somers, Christophe de Vleeschouwer, Alexandre Alahi
---
Occluded person re-identification (ReID) is a person retrieval task which
aims at matching occluded person images with holistic ones. For addressing
occluded ReID, part-based methods have been shown beneficial as they offer
fine-grained information and are well suited to represent partially visible
human bodies. However, training a part-based model is a challenging task for
two reasons. Firstly, individual body part appearance is not as discriminative
as global appearance (two distinct IDs might have the same local appearance),
this means standard ReID training objectives using identity labels are not
adapted to local feature learning. Secondly, ReID datasets are not provided
with human topographical annotations. In this work, we propose BPBreID, a body
part-based ReID model for solving the above issues. We first design two modules
for predicting body part attention maps and producing body part-based features
of the ReID target. We then propose GiLt, a novel training scheme for learning
part-based representations that is robust to occlusions and non-discriminative
local appearance. Extensive experiments on popular holistic and occluded
datasets show the effectiveness of our proposed method, which outperforms
state-of-the-art methods by 0.7% mAP and 5.6% rank-1 accuracy on the
challenging Occluded-Duke dataset. Our code is available at
https://github.com/VlSomers/bpbreid.