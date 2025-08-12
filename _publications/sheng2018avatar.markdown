---
layout: publication
title: 'Avatar-net: Multi-scale Zero-shot Style Transfer By Feature Decoration'
authors: Lu Sheng, Ziyi Lin, Jing Shao, Xiaogang Wang
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: sheng2018avatar
citations: 279
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.03857'}]
tags: ["CVPR"]
short_authors: Sheng et al.
---
Zero-shot artistic style transfer is an important image synthesis problem
aiming at transferring arbitrary style into content images. However, the
trade-off between the generalization and efficiency in existing methods impedes
a high quality zero-shot style transfer in real-time. In this paper, we resolve
this dilemma and propose an efficient yet effective Avatar-Net that enables
visually plausible multi-scale transfer for arbitrary style. The key ingredient
of our method is a style decorator that makes up the content features by
semantically aligned style features from an arbitrary style image, which does
not only holistically match their feature distributions but also preserve
detailed style patterns in the decorated features. By embedding this module
into an image reconstruction network that fuses multi-scale style abstractions,
the Avatar-Net renders multi-scale stylization for any style image in one
feed-forward pass. We demonstrate the state-of-the-art effectiveness and
efficiency of the proposed method in generating high-quality stylized images,
with a series of applications include multiple style integration, video
stylization and etc.