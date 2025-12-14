---
layout: publication
title: 'SAMURAI: Shape-aware Multimodal Retrieval For 3D Object Identification'
authors: Dinh-Khoi Vo, van-Loc Nguyen, Minh-Triet Tran, Trung-Nghia Le
conference: 2025 International Conference on Multimedia Analysis and Pattern Recognition
  (MAPR)
year: 2025
bibkey: vo2025samurai
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.21056'}]
tags: [Evaluation, Re-ranking, Multimodal Retrieval, Tools & Libraries, Hybrid ANN
    Methods]
short_authors: Vo et al.
---
Retrieving 3D objects in complex indoor environments using only a masked 2D image and a natural language description presents significant challenges. The ROOMELSA challenge limits access to full 3D scene context, complicating reasoning about object appearance, geometry, and semantics. These challenges are intensified by distorted viewpoints, textureless masked regions, ambiguous language prompts, and noisy segmentation masks. To address this, we propose SAMURAI: Shape-Aware Multimodal Retrieval for 3D Object Identification. SAMURAI integrates CLIP-based semantic matching with shape-guided re-ranking derived from binary silhouettes of masked regions, alongside a robust majority voting strategy. A dedicated preprocessing pipeline enhances mask quality by extracting the largest connected component and removing background noise. Our hybrid retrieval framework leverages both language and shape cues, achieving competitive performance on the ROOMELSA private test set. These results highlight the importance of combining shape priors with language understanding for robust open-world 3D object retrieval.