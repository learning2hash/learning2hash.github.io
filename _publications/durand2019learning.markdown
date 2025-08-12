---
layout: publication
title: Learning A Deep Convnet For Multi-label Classification With Partial Labels
authors: Thibaut Durand, Nazanin Mehrasa, Greg Mori
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: durand2019learning
citations: 225
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.09720'}]
tags: ["CVPR"]
short_authors: Thibaut Durand, Nazanin Mehrasa, Greg Mori
---
Deep ConvNets have shown great performance for single-label image
classification (e.g. ImageNet), but it is necessary to move beyond the
single-label classification task because pictures of everyday life are
inherently multi-label. Multi-label classification is a more difficult task
than single-label classification because both the input images and output label
spaces are more complex. Furthermore, collecting clean multi-label annotations
is more difficult to scale-up than single-label annotations. To reduce the
annotation cost, we propose to train a model with partial labels i.e. only some
labels are known per image. We first empirically compare different labeling
strategies to show the potential for using partial labels on multi-label
datasets. Then to learn with partial labels, we introduce a new classification
loss that exploits the proportion of known labels per example. Our approach
allows the use of the same training settings as when learning with all the
annotations. We further explore several curriculum learning based strategies to
predict missing labels. Experiments are performed on three large-scale
multi-label datasets: MS COCO, NUS-WIDE and Open Images.