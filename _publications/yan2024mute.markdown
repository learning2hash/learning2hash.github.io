---
layout: publication
title: 'MUTE-SLAM: Real-time Neural SLAM With Multiple Tri-plane Hash Representations'
authors: Yifan Yan, Ruomin He, Zhenghua Liu
conference: 2024 8th Asian Conference on Artificial Intelligence Technology (ACAIT)
year: 2024
bibkey: yan2024mute
citations: 0
additional_links: [{name: Code, url: 'https://github.com/lumennYan/MUTE_SLAM'}, {
    name: Paper, url: 'https://arxiv.org/abs/2403.17765'}]
tags: ["AAAI", "Efficiency"]
short_authors: Yifan Yan, Ruomin He, Zhenghua Liu
---
We introduce MUTE-SLAM, a real-time neural RGB-D SLAM system employing
multiple tri-plane hash-encodings for efficient scene representation. MUTE-SLAM
effectively tracks camera positions and incrementally builds a scalable
multi-map representation for both small and large indoor environments. As
previous methods often require pre-defined scene boundaries, MUTE-SLAM
dynamically allocates sub-maps for newly observed local regions, enabling
constraint-free mapping without prior scene information. Unlike traditional
grid-based methods, we use three orthogonal axis-aligned planes for
hash-encoding scene properties, significantly reducing hash collisions and the
number of trainable parameters. This hybrid approach not only ensures real-time
performance but also enhances the fidelity of surface reconstruction.
Furthermore, our optimization strategy concurrently optimizes all sub-maps
intersecting with the current camera frustum, ensuring global consistency.
Extensive testing on both real-world and synthetic datasets has shown that
MUTE-SLAM delivers state-of-the-art surface reconstruction quality and
competitive tracking performance across diverse indoor settings. The code is
available at https://github.com/lumennYan/MUTE_SLAM.