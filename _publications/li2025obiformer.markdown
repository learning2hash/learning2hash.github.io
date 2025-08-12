---
layout: publication
title: 'Obiformer: A Fast Attentive Denoising Framework For Oracle Bone Inscriptions'
authors: Jinhao Li, Zijian Chen, Tingzhu Chen, Zhiji Liu, Changbo Wang
conference: Displays
year: 2025
bibkey: li2025obiformer
citations: 0
additional_links: [{name: Code, url: 'https://github.com/LJHolyGround/OBIFormer'},
  {name: Paper, url: 'https://arxiv.org/abs/2504.13524'}]
tags: ["Tools & Libraries"]
short_authors: Li et al.
---
Oracle bone inscriptions (OBIs) are the earliest known form of Chinese
characters and serve as a valuable resource for research in anthropology and
archaeology. However, most excavated fragments are severely degraded due to
thousands of years of natural weathering, corrosion, and man-made destruction,
making automatic OBI recognition extremely challenging. Previous methods either
focus on pixel-level information or utilize vanilla transformers for
glyph-based OBI denoising, which leads to tremendous computational overhead.
Therefore, this paper proposes a fast attentive denoising framework for oracle
bone inscriptions, i.e., OBIFormer. It leverages channel-wise self-attention,
glyph extraction, and selective kernel feature fusion to reconstruct denoised
images precisely while being computationally efficient. Our OBIFormer achieves
state-of-the-art denoising performance for PSNR and SSIM metrics on synthetic
and original OBI datasets. Furthermore, comprehensive experiments on a real
oracle dataset demonstrate the great potential of our OBIFormer in assisting
automatic OBI recognition. The code will be made available at
https://github.com/LJHolyGround/OBIFormer.