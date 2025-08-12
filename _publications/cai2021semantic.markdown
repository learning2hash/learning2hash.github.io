---
layout: publication
title: Semantic Scene Completion Via Integrating Instances And Scene In-the-loop
authors: Yingjie Cai, Xuesong Chen, Chao Zhang, Kwan-Yee Lin, Xiaogang Wang, Hongsheng
  Li
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: cai2021semantic
citations: 49
additional_links: [{name: Code, url: 'https://github.com/yjcaimeow/SISNet'}, {name: Paper,
    url: 'https://arxiv.org/abs/2104.03640'}]
tags: ["CVPR"]
short_authors: Cai et al.
---
Semantic Scene Completion aims at reconstructing a complete 3D scene with
precise voxel-wise semantics from a single-view depth or RGBD image. It is a
crucial but challenging problem for indoor scene understanding. In this work,
we present a novel framework named Scene-Instance-Scene Network
(\textit\{SISNet\}), which takes advantages of both instance and scene level
semantic information. Our method is capable of inferring fine-grained shape
details as well as nearby objects whose semantic categories are easily
mixed-up. The key insight is that we decouple the instances from a coarsely
completed semantic scene instead of a raw input image to guide the
reconstruction of instances and the overall scene. SISNet conducts iterative
scene-to-instance (SI) and instance-to-scene (IS) semantic completion.
Specifically, the SI is able to encode objects' surrounding context for
effectively decoupling instances from the scene and each instance could be
voxelized into higher resolution to capture finer details. With IS,
fine-grained instance information can be integrated back into the 3D scene and
thus leads to more accurate semantic scene completion. Utilizing such an
iterative mechanism, the scene and instance completion benefits each other to
achieve higher completion accuracy. Extensively experiments show that our
proposed method consistently outperforms state-of-the-art methods on both real
NYU, NYUCAD and synthetic SUNCG-RGBD datasets. The code and the supplementary
material will be available at https://github.com/yjcaimeow/SISNet.