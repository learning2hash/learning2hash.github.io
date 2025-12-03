---
layout: publication
title: 'REJEPA: A Novel Joint-embedding Predictive Architecture For Efficient Remote
  Sensing Image Retrieval'
authors: Shabnam Choudhury, Yash Salunkhe, Sarthak Mehrotra, Biplab Banerjee
conference: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2025
bibkey: choudhury2025rejepa
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.03169'}]
tags: ["Efficiency", "Evaluation", "Image Retrieval", "Self-Supervised", "Supervised"]
short_authors: Choudhury et al.
---
The rapid expansion of remote sensing image archives demands the development of strong and efficient techniques for content-based image retrieval (RS-CBIR). This paper presents REJEPA (Retrieval with Joint-Embedding Predictive Architecture), an innovative self-supervised framework designed for unimodal RS-CBIR. REJEPA utilises spatially distributed context token encoding to forecast abstract representations of target tokens, effectively capturing high-level semantic features and eliminating unnecessary pixel-level details. In contrast to generative methods that focus on pixel reconstruction or contrastive techniques that depend on negative pairs, REJEPA functions within feature space, achieving a reduction in computational complexity of 40-60% when compared to pixel-reconstruction baselines like Masked Autoencoders (MAE). To guarantee strong and varied representations, REJEPA incorporates Variance-Invariance-Covariance Regularisation (VICReg), which prevents encoder collapse by promoting feature diversity and reducing redundancy. The method demonstrates an estimated enhancement in retrieval accuracy of 5.1% on BEN-14K (S1), 7.4% on BEN-14K (S2), 6.0% on FMoW-RGB, and 10.1% on FMoW-Sentinel compared to prominent SSL techniques, including CSMAE-SESD, Mask-VLM, SatMAE, ScaleMAE, and SatMAE++, on extensive RS benchmarks BEN-14K (multispectral and SAR data), FMoW-RGB and FMoW-Sentinel. Through effective generalisation across sensor modalities, REJEPA establishes itself as a sensor-agnostic benchmark for efficient, scalable, and precise RS-CBIR, addressing challenges like varying resolutions, high object density, and complex backgrounds with computational efficiency.