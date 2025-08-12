---
layout: publication
title: A Style-aware Discriminator For Controllable Image Translation
authors: Kunhee Kim, Sanghun Park, Eunyeong Jeon, Taehun Kim, Daijin Kim
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: kim2022style
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.15375'}]
tags: ["CVPR"]
short_authors: Kim et al.
---
Current image-to-image translations do not control the output domain beyond
the classes used during training, nor do they interpolate between different
domains well, leading to implausible results. This limitation largely arises
because labels do not consider the semantic distance. To mitigate such
problems, we propose a style-aware discriminator that acts as a critic as well
as a style encoder to provide conditions. The style-aware discriminator learns
a controllable style space using prototype-based self-supervised learning and
simultaneously guides the generator. Experiments on multiple datasets verify
that the proposed model outperforms current state-of-the-art image-to-image
translation methods. In contrast with current methods, the proposed approach
supports various applications, including style interpolation, content
transplantation, and local image translation.