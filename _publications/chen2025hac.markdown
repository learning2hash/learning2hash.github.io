---
layout: publication
title: 'HAC++: Towards 100X Compression Of 3D Gaussian Splatting'
authors: Yihang Chen, Qianyi Wu, Weiyao Lin, Mehrtash Harandi, Jianfei Cai
conference: Arxiv
year: 2025
bibkey: chen2025hac
citations: 0
additional_links: [{name: Code, url: 'https://github.com/YihangChen-ee/HAC-plus'},
  {name: Paper, url: 'https://arxiv.org/abs/2501.12255'}]
tags: ["Quantization"]
short_authors: Chen et al.
---
3D Gaussian Splatting (3DGS) has emerged as a promising framework for novel
view synthesis, boasting rapid rendering speed with high fidelity. However, the
substantial Gaussians and their associated attributes necessitate effective
compression techniques. Nevertheless, the sparse and unorganized nature of the
point cloud of Gaussians (or anchors in our paper) presents challenges for
compression. To achieve a compact size, we propose HAC++, which leverages the
relationships between unorganized anchors and a structured hash grid, utilizing
their mutual information for context modeling. Additionally, HAC++ captures
intra-anchor contextual relationships to further enhance compression
performance. To facilitate entropy coding, we utilize Gaussian distributions to
precisely estimate the probability of each quantized attribute, where an
adaptive quantization module is proposed to enable high-precision quantization
of these attributes for improved fidelity restoration. Moreover, we incorporate
an adaptive masking strategy to eliminate invalid Gaussians and anchors.
Overall, HAC++ achieves a remarkable size reduction of over 100X compared to
vanilla 3DGS when averaged on all datasets, while simultaneously improving
fidelity. It also delivers more than 20X size reduction compared to
Scaffold-GS. Our code is available at
https://github.com/YihangChen-ee/HAC-plus.