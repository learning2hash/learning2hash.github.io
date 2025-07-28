---
layout: publication
title: 'WAD-CMSN: Wasserstein Distance Based Cross-modal Semantic Network For Zero-shot
  Sketch-based Image Retrieval'
authors: Guanglong Xu, Zhensheng Hu, Jia Cai
conference: International Journal of Wavelets, Multiresolution and Information Processing
year: 2022
bibkey: xu2022wad
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.05465'}]
tags: []
short_authors: Guanglong Xu, Zhensheng Hu, Jia Cai
---
Zero-shot sketch-based image retrieval (ZSSBIR), as a popular studied branch
of computer vision, attracts wide attention recently. Unlike sketch-based image
retrieval (SBIR), the main aim of ZSSBIR is to retrieve natural images given
free hand-drawn sketches that may not appear during training. Previous
approaches used semantic aligned sketch-image pairs or utilized memory
expensive fusion layer for projecting the visual information to a low
dimensional subspace, which ignores the significant heterogeneous cross-domain
discrepancy between highly abstract sketch and relevant image. This may yield
poor performance in the training phase. To tackle this issue and overcome this
drawback, we propose a Wasserstein distance based cross-modal semantic network
(WAD-CMSN) for ZSSBIR. Specifically, it first projects the visual information
of each branch (sketch, image) to a common low dimensional semantic subspace
via Wasserstein distance in an adversarial training manner. Furthermore,
identity matching loss is employed to select useful features, which can not
only capture complete semantic knowledge, but also alleviate the over-fitting
phenomenon caused by the WAD-CMSN model. Experimental results on the
challenging Sketchy (Extended) and TU-Berlin (Extended) datasets indicate the
effectiveness of the proposed WAD-CMSN model over several competitors.