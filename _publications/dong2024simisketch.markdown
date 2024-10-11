---
layout: publication
title: Simisketch Efficiently Estimating Similarity Of Streaming Multisets
authors: Dong Fenghao, He Yang, Liang Yutong, Liu Zirui, Wu Yuhan, Chen Peiqing, Yang Tong
conference: "Arxiv"
year: 2024
bibkey: dong2024simisketch
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2405.19711"}
tags: ['ARXIV', 'Independent']
---
The challenge of estimating similarity between sets has been a significant concern in data science, finding diverse applications across various domains. However, previous approaches, such as MinHash, have predominantly centered around hashing techniques, which are well-suited for sets but less naturally adaptable to multisets, a common occurrence in scenarios like network streams and text data. Moreover, with the increasing prevalence of data arriving in streaming patterns, many existing methods struggle to handle cases where set items are presented in a continuous stream. Consequently, our focus in this paper is on the challenging scenario of multisets with item streams. To address this, we propose SimiSketch, a sketching algorithm designed to tackle this specific problem. The paper begins by presenting two simpler versions that employ intuitive sketches for similarity estimation. Subsequently, we formally introduce SimiSketch and leverage SALSA to enhance accuracy. To validate our algorithms, we conduct extensive testing on synthetic datasets, real-world network traffic, and text articles. Our experiment shows that compared with the state-of-the-art, SimiSketch can improve the accuracy by up to 42 times, and increase the throughput by up to 360 times. The complete source code is open-sourced and available on GitHub for reference.
