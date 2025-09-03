---
layout: publication
title: 'SLAG: Scalable Language-augmented Gaussian Splatting'
authors: Laszlo Szilagyi, Francis Engelmann, Jeannette Bohg
conference: IEEE Robotics and Automation Letters
year: 2025
bibkey: szilagyi2025slag
citations: 0
additional_links: [{name: Other, url: 'https://slag-project'}, {name: Paper, url: 'https://arxiv.org/abs/2505.08124'}]
tags: ["Datasets", "Efficiency", "Scalability", "Tools & Libraries"]
short_authors: Laszlo Szilagyi, Francis Engelmann, Jeannette Bohg
---
Language-augmented scene representations hold great promise for large-scale robotics applications such as search-and-rescue, smart cities, and mining. Many of these scenarios are time-sensitive, requiring rapid scene encoding while also being data-intensive, necessitating scalable solutions. Deploying these representations on robots with limited computational resources further adds to the challenge. To address this, we introduce SLAG, a multi-GPU framework for language-augmented Gaussian splatting that enhances the speed and scalability of embedding large scenes. Our method integrates 2D visual-language model features into 3D scenes using SAM and CLIP. Unlike prior approaches, SLAG eliminates the need for a loss function to compute per-Gaussian language embeddings. Instead, it derives embeddings from 3D Gaussian scene parameters via a normalized weighted average, enabling highly parallelized scene encoding. Additionally, we introduce a vector database for efficient embedding storage and retrieval. Our experiments show that SLAG achieves an 18 times speedup in embedding computation on a 16-GPU setup compared to OpenGaussian, while preserving embedding quality on the ScanNet and LERF datasets. For more details, visit our project website: https://slag-project.github.io/.