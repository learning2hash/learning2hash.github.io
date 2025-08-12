---
layout: publication
title: 'Ibrnet: Learning Multi-view Image-based Rendering'
authors: Qianqian Wang, Zhicheng Wang, Kyle Genova, Pratul Srinivasan, Howard Zhou,
  Jonathan T. Barron, Ricardo Martin-Brualla, Noah Snavely, Thomas Funkhouser
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: wang2021ibrnet
citations: 526
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.13090'}]
tags: ["CVPR"]
short_authors: Wang et al.
---
We present a method that synthesizes novel views of complex scenes by
interpolating a sparse set of nearby views. The core of our method is a network
architecture that includes a multilayer perceptron and a ray transformer that
estimates radiance and volume density at continuous 5D locations (3D spatial
locations and 2D viewing directions), drawing appearance information on the fly
from multiple source views. By drawing on source views at render time, our
method hearkens back to classic work on image-based rendering (IBR), and allows
us to render high-resolution imagery. Unlike neural scene representation work
that optimizes per-scene functions for rendering, we learn a generic view
interpolation function that generalizes to novel scenes. We render images using
classic volume rendering, which is fully differentiable and allows us to train
using only multi-view posed images as supervision. Experiments show that our
method outperforms recent novel view synthesis methods that also seek to
generalize to novel scenes. Further, if fine-tuned on each scene, our method is
competitive with state-of-the-art single-scene neural rendering methods.
Project page: https://ibrnet.github.io/