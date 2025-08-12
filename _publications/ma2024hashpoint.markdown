---
layout: publication
title: 'Hashpoint: Accelerated Point Searching And Sampling For Neural Rendering'
authors: Jiahao Ma, Miaomiao Liu, David Ahmedt-Aristizaba, Chuong Nguyen
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: ma2024hashpoint
citations: 1
additional_links: [{name: Code, url: 'https://jiahao-ma.github.io/hashpoint/'}, {
    name: Paper, url: 'https://arxiv.org/abs/2404.14044'}]
tags: ["CVPR", "Efficiency"]
short_authors: Ma et al.
---
In this paper, we address the problem of efficient point searching and
sampling for volume neural rendering. Within this realm, two typical approaches
are employed: rasterization and ray tracing. The rasterization-based methods
enable real-time rendering at the cost of increased memory and lower fidelity.
In contrast, the ray-tracing-based methods yield superior quality but demand
longer rendering time. We solve this problem by our HashPoint method combining
these two strategies, leveraging rasterization for efficient point searching
and sampling, and ray marching for rendering. Our method optimizes point
searching by rasterizing points within the camera's view, organizing them in a
hash table, and facilitating rapid searches. Notably, we accelerate the
rendering process by adaptive sampling on the primary surface encountered by
the ray. Our approach yields substantial speed-up for a range of
state-of-the-art ray-tracing-based methods, maintaining equivalent or superior
accuracy across synthetic and real test datasets. The code will be available at
https://jiahao-ma.github.io/hashpoint/.