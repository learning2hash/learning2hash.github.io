---
layout: publication
title: 'Movies2scenes: Using Movie Metadata To Learn Scene Representation'
authors: Shixing Chen, Chun-hao Liu, Xiang Hao, Xiaohan Nie, Maxim Arap, Raffay Hamid
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: chen2022movies2scenes
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.10650'}]
tags: ["CVPR"]
short_authors: Chen et al.
---
Understanding scenes in movies is crucial for a variety of applications such
as video moderation, search, and recommendation. However, labeling individual
scenes is a time-consuming process. In contrast, movie level metadata (e.g.,
genre, synopsis, etc.) regularly gets produced as part of the film production
process, and is therefore significantly more commonly available. In this work,
we propose a novel contrastive learning approach that uses movie metadata to
learn a general-purpose scene representation. Specifically, we use movie
metadata to define a measure of movie similarity, and use it during contrastive
learning to limit our search for positive scene-pairs to only the movies that
are considered similar to each other. Our learned scene representation
consistently outperforms existing state-of-the-art methods on a diverse set of
tasks evaluated using multiple benchmark datasets. Notably, our learned
representation offers an average improvement of 7.9% on the seven
classification tasks and 9.7% improvement on the two regression tasks in LVU
dataset. Furthermore, using a newly collected movie dataset, we present
comparative results of our scene representation on a set of video moderation
tasks to demonstrate its generalizability on previously less explored tasks.