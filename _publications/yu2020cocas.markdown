---
layout: publication
title: 'COCAS: A Large-scale Clothes Changing Person Dataset For Re-identification'
authors: Shijie Yu, Shihua Li, Dapeng Chen, Rui Zhao, Junjie Yan, Yu Qiao
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: yu2020cocas
citations: 88
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.07862'}]
tags: ["CVPR", "Datasets"]
short_authors: Yu et al.
---
Recent years have witnessed great progress in person re-identification
(re-id). Several academic benchmarks such as Market1501, CUHK03 and DukeMTMC
play important roles to promote the re-id research. To our best knowledge, all
the existing benchmarks assume the same person will have the same clothes.
While in real-world scenarios, it is very often for a person to change clothes.
To address the clothes changing person re-id problem, we construct a novel
large-scale re-id benchmark named ClOthes ChAnging Person Set (COCAS), which
provides multiple images of the same identity with different clothes. COCAS
totally contains 62,382 body images from 5,266 persons. Based on COCAS, we
introduce a new person re-id setting for clothes changing problem, where the
query includes both a clothes template and a person image taking another
clothes. Moreover, we propose a two-branch network named Biometric-Clothes
Network (BC-Net) which can effectively integrate biometric and clothes feature
for re-id under our setting. Experiments show that it is feasible for clothes
changing re-id with clothes templates.