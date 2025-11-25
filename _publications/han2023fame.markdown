---
layout: publication
title: 'Fame-vil: Multi-tasking Vision-language Model For Heterogeneous Fashion Tasks'
authors: Xiao Han, Xiatian Zhu, Licheng Yu, Li Zhang, Yi-Zhe Song, Tao Xiang
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: han2023fame
citations: 35
additional_links: [{name: Code, url: 'https://github.com/BrandonHanx/FAME-ViL'}, {
    name: Paper, url: 'https://arxiv.org/abs/2303.02483'}]
tags: ["CVPR", "Efficiency", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Han et al.
---
In the fashion domain, there exists a variety of vision-and-language (V+L)
tasks, including cross-modal retrieval, text-guided image retrieval,
multi-modal classification, and image captioning. They differ drastically in
each individual input/output format and dataset size. It has been common to
design a task-specific model and fine-tune it independently from a pre-trained
V+L model (e.g., CLIP). This results in parameter inefficiency and inability to
exploit inter-task relatedness. To address such issues, we propose a novel
FAshion-focused Multi-task Efficient learning method for Vision-and-Language
tasks (FAME-ViL) in this work. Compared with existing approaches, FAME-ViL
applies a single model for multiple heterogeneous fashion tasks, therefore
being much more parameter-efficient. It is enabled by two novel components: (1)
a task-versatile architecture with cross-attention adapters and task-specific
adapters integrated into a unified V+L model, and (2) a stable and effective
multi-task training strategy that supports learning from heterogeneous data and
prevents negative transfer. Extensive experiments on four fashion tasks show
that our FAME-ViL can save 61.5% of parameters over alternatives, while
significantly outperforming the conventional independently trained single-task
models. Code is available at https://github.com/BrandonHanx/FAME-ViL.