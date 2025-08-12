---
layout: publication
title: 'Momentsnerf: Leveraging Orthogonal Moments For Few-shot Neural Rendering'
authors: Ahmad Almughrabi, Ricardo Marques, Petia Radeva
conference: Arxiv
year: 2024
bibkey: almughrabi2024momentsnerf
citations: 0
additional_links: [{name: Code, url: 'https://amughrabi.github.io/momentsnerf/'},
  {name: Paper, url: 'https://arxiv.org/abs/2407.02668'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Ahmad Almughrabi, Ricardo Marques, Petia Radeva
---
We propose MomentsNeRF, a novel framework for one- and few-shot neural
rendering that predicts a neural representation of a 3D scene using Orthogonal
Moments. Our architecture offers a new transfer learning method to train on
multi-scenes and incorporate a per-scene optimization using one or a few images
at test time. Our approach is the first to successfully harness features
extracted from Gabor and Zernike moments, seamlessly integrating them into the
NeRF architecture. We show that MomentsNeRF performs better in synthesizing
images with complex textures and shapes, achieving a significant noise
reduction, artifact elimination, and completing the missing parts compared to
the recent one- and few-shot neural rendering frameworks. Extensive experiments
on the DTU and Shapenet datasets show that MomentsNeRF improves the
state-of-the-art by \{3.39\;dB\;PSNR\}, 11.1% SSIM, 17.9% LPIPS, and 8.3% DISTS
metrics. Moreover, it outperforms state-of-the-art performance for both novel
view synthesis and single-image 3D view reconstruction. The source code is
accessible at: https://amughrabi.github.io/momentsnerf/.