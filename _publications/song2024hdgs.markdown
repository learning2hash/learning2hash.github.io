---
layout: publication
title: 'HDGS: Textured 2D Gaussian Splatting For Enhanced Scene Rendering'
authors: Yunzhou Song, Heguang Lin, Jiahui Lei, Lingjie Liu, Kostas Daniilidis
conference: Arxiv
year: 2024
bibkey: song2024hdgs
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.01823'}]
tags: ["Efficiency"]
short_authors: Song et al.
---
Recent advancements in neural rendering, particularly 2D Gaussian Splatting
(2DGS), have shown promising results for jointly reconstructing fine appearance
and geometry by leveraging 2D Gaussian surfels. However, current methods face
significant challenges when rendering at arbitrary viewpoints, such as
anti-aliasing for down-sampled rendering, and texture detail preservation for
high-resolution rendering. We proposed a novel method to align the 2D surfels
with texture maps and augment it with per-ray depth sorting and fisher-based
pruning for rendering consistency and efficiency. With correct order,
per-surfel texture maps significantly improve the capabilities to capture fine
details. Additionally, to render high-fidelity details in varying viewpoints,
we designed a frustum-based sampling method to mitigate the aliasing artifacts.
Experimental results on benchmarks and our custom texture-rich dataset
demonstrate that our method surpasses existing techniques, particularly in
detail preservation and anti-aliasing.