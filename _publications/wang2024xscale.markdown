---
layout: publication
title: 'Xscale-nvs: Cross-scale Novel View Synthesis With Hash Featurized Manifold'
authors: Guangyu Wang, Jinzhi Zhang, Fan Wang, Ruqi Huang, Lu Fang
conference: Arxiv
year: 2024
bibkey: wang2024xscale
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.19517'}]
tags: []
short_authors: Wang et al.
---
We propose XScale-NVS for high-fidelity cross-scale novel view synthesis of
real-world large-scale scenes. Existing representations based on explicit
surface suffer from discretization resolution or UV distortion, while implicit
volumetric representations lack scalability for large scenes due to the
dispersed weight distribution and surface ambiguity. In light of the above
challenges, we introduce hash featurized manifold, a novel hash-based
featurization coupled with a deferred neural rendering framework. This approach
fully unlocks the expressivity of the representation by explicitly
concentrating the hash entries on the 2D manifold, thus effectively
representing highly detailed contents independent of the discretization
resolution. We also introduce a novel dataset, namely GigaNVS, to benchmark
cross-scale, high-resolution novel view synthesis of realworld large-scale
scenes. Our method significantly outperforms competing baselines on various
real-world scenes, yielding an average LPIPS that is 40% lower than prior
state-of-the-art on the challenging GigaNVS benchmark. Please see our project
page at: xscalenvs.github.io.