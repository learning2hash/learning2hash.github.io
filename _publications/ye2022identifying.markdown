---
layout: publication
title: Identifying Ambiguous Similarity Conditions Via Semantic Matching
authors: Han-jia Ye, Yi Shi, De-chuan Zhan
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: ye2022identifying
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.04053'}]
tags: ["CVPR"]
short_authors: Han-jia Ye, Yi Shi, De-chuan Zhan
---
Rich semantics inside an image result in its ambiguous relationship with
others, i.e., two images could be similar in one condition but dissimilar in
another. Given triplets like "aircraft" is similar to "bird" than "train",
Weakly Supervised Conditional Similarity Learning (WS-CSL) learns multiple
embeddings to match semantic conditions without explicit condition labels such
as "can fly". However, similarity relationships in a triplet are uncertain
except providing a condition. For example, the previous comparison becomes
invalid once the conditional label changes to "is vehicle". To this end, we
introduce a novel evaluation criterion by predicting the comparison's
correctness after assigning the learned embeddings to their optimal conditions,
which measures how much WS-CSL could cover latent semantics as the supervised
model. Furthermore, we propose the Distance Induced Semantic COndition
VERification Network (DiscoverNet), which characterizes the instance-instance
and triplets-condition relations in a "decompose-and-fuse" manner. To make the
learned embeddings cover all semantics, DiscoverNet utilizes a set module or an
additional regularizer over the correspondence between a triplet and a
condition. DiscoverNet achieves state-of-the-art performance on benchmarks like
UT-Zappos-50k and Celeb-A w.r.t. different criteria.