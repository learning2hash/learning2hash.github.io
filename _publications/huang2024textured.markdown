---
layout: publication
title: 'Textured-gs: Gaussian Splatting With Spatially Defined Color And Opacity'
authors: Zhentao Huang, Minglun Gong
conference: Arxiv
year: 2024
bibkey: huang2024textured
citations: 1
additional_links: [{name: Code, url: 'https://github.com/ZhentaoHuang/Textured-GS'},
  {name: Paper, url: 'https://arxiv.org/abs/2407.09733'}]
tags: []
short_authors: Zhentao Huang, Minglun Gong
---
In this paper, we introduce Textured-GS, an innovative method for rendering
Gaussian splatting that incorporates spatially defined color and opacity
variations using Spherical Harmonics (SH). This approach enables each Gaussian
to exhibit a richer representation by accommodating varying colors and
opacities across its surface, significantly enhancing rendering quality
compared to traditional methods. To demonstrate the merits of our approach, we
have adapted the Mini-Splatting architecture to integrate textured Gaussians
without increasing the number of Gaussians. Our experiments across multiple
real-world datasets show that Textured-GS consistently outperforms both the
baseline Mini-Splatting and standard 3DGS in terms of visual fidelity. The
results highlight the potential of Textured-GS to advance Gaussian-based
rendering technologies, promising more efficient and high-quality scene
reconstructions. Our implementation is available at
https://github.com/ZhentaoHuang/Textured-GS.