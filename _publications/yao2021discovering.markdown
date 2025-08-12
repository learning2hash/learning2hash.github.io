---
layout: publication
title: Discovering 3D Parts From Image Collections
authors: Chun-Han Yao, Wei-Chih Hung, Varun Jampani, Ming-Hsuan Yang
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: yao2021discovering
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.13629'}]
tags: ["ICCV"]
short_authors: Yao et al.
---
Reasoning 3D shapes from 2D images is an essential yet challenging task,
especially when only single-view images are at our disposal. While an object
can have a complicated shape, individual parts are usually close to geometric
primitives and thus are easier to model. Furthermore, parts provide a mid-level
representation that is robust to appearance variations across objects in a
particular category. In this work, we tackle the problem of 3D part discovery
from only 2D image collections. Instead of relying on manually annotated parts
for supervision, we propose a self-supervised approach, latent part discovery
(LPD). Our key insight is to learn a novel part shape prior that allows each
part to fit an object shape faithfully while constrained to have simple
geometry. Extensive experiments on the synthetic ShapeNet, PartNet, and
real-world Pascal 3D+ datasets show that our method discovers consistent object
parts and achieves favorable reconstruction accuracy compared to the existing
methods with the same level of supervision.