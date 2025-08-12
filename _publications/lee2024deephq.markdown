---
layout: publication
title: 'Deephq: Learned Hierarchical Quantizer For Progressive Deep Image Coding'
authors: Jooyoung Lee, Se Yoon Jeong, Munchurl Kim
conference: Arxiv
year: 2024
bibkey: lee2024deephq
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.12150'}]
tags: ["Efficiency", "Quantization"]
short_authors: Jooyoung Lee, Se Yoon Jeong, Munchurl Kim
---
Unlike fixed- or variable-rate image coding, progressive image coding (PIC)
aims to compress various qualities of images into a single bitstream,
increasing the versatility of bitstream utilization and providing high
compression efficiency compared to simulcast compression. Research on neural
network (NN)-based PIC is in its early stages, mainly focusing on applying
varying quantization step sizes to the transformed latent representations in a
hierarchical manner. These approaches are designed to compress only the
progressively added information as the quality improves, considering that a
wider quantization interval for lower-quality compression includes multiple
narrower sub-intervals for higher-quality compression. However, the existing
methods are based on handcrafted quantization hierarchies, resulting in
sub-optimal compression efficiency. In this paper, we propose an NN-based
progressive coding method that firstly utilizes learned quantization step sizes
via learning for each quantization layer. We also incorporate selective
compression with which only the essential representation components are
compressed for each quantization layer. We demonstrate that our method achieves
significantly higher coding efficiency than the existing approaches with
decreased decoding time and reduced model size.