---
layout: publication
title: 'Stylegaussian: Instant 3D Style Transfer With Gaussian Splatting'
authors: Kunhao Liu, Fangneng Zhan, Muyu Xu, Christian Theobalt, Ling Shao, Shijian
  Lu
conference: SIGGRAPH Asia 2024 Technical Communications
year: 2024
bibkey: liu2024stylegaussian
citations: 6
additional_links: [{name: Code, url: 'https://kunhao-liu.github.io/StyleGaussian/'},
  {name: Paper, url: 'https://arxiv.org/abs/2403.07807'}]
tags: ["Efficiency"]
short_authors: Liu et al.
---
We introduce StyleGaussian, a novel 3D style transfer technique that allows
instant transfer of any image's style to a 3D scene at 10 frames per second
(fps). Leveraging 3D Gaussian Splatting (3DGS), StyleGaussian achieves style
transfer without compromising its real-time rendering ability and multi-view
consistency. It achieves instant style transfer with three steps: embedding,
transfer, and decoding. Initially, 2D VGG scene features are embedded into
reconstructed 3D Gaussians. Next, the embedded features are transformed
according to a reference style image. Finally, the transformed features are
decoded into the stylized RGB. StyleGaussian has two novel designs. The first
is an efficient feature rendering strategy that first renders low-dimensional
features and then maps them into high-dimensional features while embedding VGG
features. It cuts the memory consumption significantly and enables 3DGS to
render the high-dimensional memory-intensive features. The second is a
K-nearest-neighbor-based 3D CNN. Working as the decoder for the stylized
features, it eliminates the 2D CNN operations that compromise strict multi-view
consistency. Extensive experiments show that StyleGaussian achieves instant 3D
stylization with superior stylization quality while preserving real-time
rendering and strict multi-view consistency. Project page:
https://kunhao-liu.github.io/StyleGaussian/