---
layout: publication
title: 'More Photos Are All You Need: Semi-supervised Learning For Fine-grained Sketch
  Based Image Retrieval'
authors: Ayan Kumar Bhunia, Pinaki Nath Chowdhury, Aneeshan Sain, Yongxin Yang, Tao
  Xiang, Yi-Zhe Song
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: bhunia2021more
citations: 64
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.13990'}]
tags: [Evaluation, Supervised, Image Retrieval, Multimodal Retrieval, Scalability,
  CVPR, Tools & Libraries]
short_authors: Bhunia et al.
---
A fundamental challenge faced by existing Fine-Grained Sketch-Based Image
Retrieval (FG-SBIR) models is the data scarcity -- model performances are
largely bottlenecked by the lack of sketch-photo pairs. Whilst the number of
photos can be easily scaled, each corresponding sketch still needs to be
individually produced. In this paper, we aim to mitigate such an upper-bound on
sketch data, and study whether unlabelled photos alone (of which they are many)
can be cultivated for performances gain. In particular, we introduce a novel
semi-supervised framework for cross-modal retrieval that can additionally
leverage large-scale unlabelled photos to account for data scarcity. At the
centre of our semi-supervision design is a sequential photo-to-sketch
generation model that aims to generate paired sketches for unlabelled photos.
Importantly, we further introduce a discriminator guided mechanism to guide
against unfaithful generation, together with a distillation loss based
regularizer to provide tolerance against noisy training samples. Last but not
least, we treat generation and retrieval as two conjugate problems, where a
joint learning procedure is devised for each module to mutually benefit from
each other. Extensive experiments show that our semi-supervised model yields
significant performance boost over the state-of-the-art supervised
alternatives, as well as existing methods that can exploit unlabelled photos
for FG-SBIR.