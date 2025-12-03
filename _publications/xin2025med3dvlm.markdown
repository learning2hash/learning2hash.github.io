---
layout: publication
title: 'Med3dvlm: An Efficient Vision-language Model For 3D Medical Image Analysis'
authors: Yu Xin, Gorkem Can Ates, Kuang Gong, Wei Shao
conference: IEEE Journal of Biomedical and Health Informatics
year: 2025
bibkey: xin2025med3dvlm
citations: 2
additional_links: [{name: Code, url: 'https://github.com/mirthAI/Med3DVLM'}, {name: Paper,
    url: 'https://arxiv.org/abs/2503.20047'}]
tags: ["Datasets", "Evaluation", "Self-Supervised", "Text Retrieval"]
short_authors: Xin et al.
---
Vision-language models (VLMs) have shown promise in 2D medical image analysis, but extending them to 3D remains challenging due to the high computational demands of volumetric data and the difficulty of aligning 3D spatial features with clinical text. We present Med3DVLM, a 3D VLM designed to address these challenges through three key innovations: (1) DCFormer, an efficient encoder that uses decomposed 3D convolutions to capture fine-grained spatial features at scale; (2) SigLIP, a contrastive learning strategy with pairwise sigmoid loss that improves image-text alignment without relying on large negative batches; and (3) a dual-stream MLP-Mixer projector that fuses low- and high-level image features with text embeddings for richer multi-modal representations. We evaluate our model on the M3D dataset, which includes radiology reports and VQA data for 120,084 3D medical images. Results show that Med3DVLM achieves superior performance across multiple benchmarks. For image-text retrieval, it reaches 61.00% R@1 on 2,000 samples, significantly outperforming the current state-of-the-art M3D model (19.10%). For report generation, it achieves a METEOR score of 36.42% (vs. 14.38%). In open-ended visual question answering (VQA), it scores 36.76% METEOR (vs. 33.58%), and in closed-ended VQA, it achieves 79.95% accuracy (vs. 75.78%). These results highlight Med3DVLM's ability to bridge the gap between 3D imaging and language, enabling scalable, multi-task reasoning across clinical applications. Our code is publicly available at https://github.com/mirthAI/Med3DVLM.