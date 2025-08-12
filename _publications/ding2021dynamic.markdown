---
layout: publication
title: Dynamic Texture Recognition Using PDV Hashing And Dictionary Learning On Multi-scale
  Volume Local Binary Pattern
authors: Ruxin Ding, Jianfeng Ren, Heng Yu, Jiawei Li
conference: ICASSP 2022 - 2022 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2022
bibkey: ding2021dynamic
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.12315'}]
tags: ["Hashing Methods", "ICASSP"]
short_authors: Ding et al.
---
Spatial-temporal local binary pattern (STLBP) has been widely used in dynamic
texture recognition. STLBP often encounters the high-dimension problem as its
dimension increases exponentially, so that STLBP could only utilize a small
neighborhood. To tackle this problem, we propose a method for dynamic texture
recognition using PDV hashing and dictionary learning on multi-scale volume
local binary pattern (PHD-MVLBP). Instead of forming very high-dimensional LBP
histogram features, it first uses hash functions to map the pixel difference
vectors (PDVs) to binary vectors, then forms a dictionary using the derived
binary vector, and encodes them using the derived dictionary. In such a way,
the PDVs are mapped to feature vectors of the size of dictionary, instead of
LBP histograms of very high dimension. Such an encoding scheme could extract
the discriminant information from videos in a much larger neighborhood
effectively. The experimental results on two widely-used dynamic textures
datasets, DynTex++ and UCLA, show the superiority performance of the proposed
approach over the state-of-the-art methods.