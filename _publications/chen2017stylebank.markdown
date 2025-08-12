---
layout: publication
title: 'Stylebank: An Explicit Representation For Neural Image Style Transfer'
authors: Dongdong Chen, Lu Yuan, Jing Liao, Nenghai Yu, Gang Hua
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: chen2017stylebank
citations: 464
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.09210'}]
tags: ["CVPR"]
short_authors: Chen et al.
---
We propose StyleBank, which is composed of multiple convolution filter banks
and each filter bank explicitly represents one style, for neural image style
transfer. To transfer an image to a specific style, the corresponding filter
bank is operated on top of the intermediate feature embedding produced by a
single auto-encoder. The StyleBank and the auto-encoder are jointly learnt,
where the learning is conducted in such a way that the auto-encoder does not
encode any style information thanks to the flexibility introduced by the
explicit filter bank representation. It also enables us to conduct incremental
learning to add a new image style by learning a new filter bank while holding
the auto-encoder fixed. The explicit style representation along with the
flexible network design enables us to fuse styles at not only the image level,
but also the region level. Our method is the first style transfer network that
links back to traditional texton mapping methods, and hence provides new
understanding on neural style transfer. Our method is easy to train, runs in
real-time, and produces results that qualitatively better or at least
comparable to existing methods.