---
layout: publication
title: Rendering Point Clouds With Compute Shaders
authors: "Markus Sch\xFCtz, Michael Wimmer"
conference: SIGGRAPH Asia 2019 Posters
year: 2019
bibkey: "sch\xFCtz2019rendering"
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.02681'}]
tags: []
short_authors: "Markus Sch\xFCtz, Michael Wimmer"
---
We propose a compute shader based point cloud rasterizer with up to 10 times
higher performance than classic point-based rendering with the GL_POINT
primitive. In addition to that, our rasterizer offers 5 byte depth-buffer
precision with uniform or customizable distribution, and we show that it is
possible to implement a high-quality splatting method that blends together
overlapping fragments while still maintaining higher frame-rates than the
traditional approach.