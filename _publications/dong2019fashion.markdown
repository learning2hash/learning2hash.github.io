---
layout: publication
title: Fashion Editing With Adversarial Parsing Learning
authors: Haoye Dong, Xiaodan Liang, Yixuan Zhang, Xujie Zhang, Zhenyu Xie, Bowen Wu,
  Ziqi Zhang, Xiaohui Shen, Jian Yin
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: dong2019fashion
citations: 73
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.00884'}]
tags: ["CVPR"]
short_authors: Dong et al.
---
Interactive fashion image manipulation, which enables users to edit images
with sketches and color strokes, is an interesting research problem with great
application value. Existing works often treat it as a general inpainting task
and do not fully leverage the semantic structural information in fashion
images. Moreover, they directly utilize conventional convolution and
normalization layers to restore the incomplete image, which tends to wash away
the sketch and color information. In this paper, we propose a novel Fashion
Editing Generative Adversarial Network (FE-GAN), which is capable of
manipulating fashion images by free-form sketches and sparse color strokes.
FE-GAN consists of two modules: 1) a free-form parsing network that learns to
control the human parsing generation by manipulating sketch and color; 2) a
parsing-aware inpainting network that renders detailed textures with semantic
guidance from the human parsing map. A new attention normalization layer is
further applied at multiple scales in the decoder of the inpainting network to
enhance the quality of the synthesized image. Extensive experiments on
high-resolution fashion image datasets demonstrate that the proposed method
significantly outperforms the state-of-the-art methods on image manipulation.