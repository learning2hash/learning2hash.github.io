---
layout: publication
title: 'LSNIF: Locally-subdivided Neural Intersection Function'
authors: Shin Fujieda, Chih-Chen Kao, Takahiro Harada
conference: Proceedings of the ACM on Computer Graphics and Interactive Techniques
year: 2025
bibkey: fujieda2025lsnif
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.21627'}]
tags: []
short_authors: Shin Fujieda, Chih-Chen Kao, Takahiro Harada
---
Neural representations have shown the potential to accelerate ray casting in
a conventional ray-tracing-based rendering pipeline. We introduce a novel
approach called Locally-Subdivided Neural Intersection Function (LSNIF) that
replaces bottom-level BVHs used as traditional geometric representations with a
neural network. Our method introduces a sparse hash grid encoding scheme
incorporating geometry voxelization, a scene-agnostic training data collection,
and a tailored loss function. It enables the network to output not only
visibility but also hit-point information and material indices. LSNIF can be
trained offline for a single object, allowing us to use LSNIF as a replacement
for its corresponding BVH. With these designs, the network can handle hit-point
queries from any arbitrary viewpoint, supporting all types of rays in the
rendering pipeline. We demonstrate that LSNIF can render a variety of scenes,
including real-world scenes designed for other path tracers, while achieving a
memory footprint reduction of up to 106.2x compared to a compressed BVH.