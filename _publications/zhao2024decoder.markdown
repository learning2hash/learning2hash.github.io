---
layout: publication
title: Decoder Pre-training With Only Text For Scene Text Recognition
authors: Shuai Zhao, Yongkun Du, Zhineng Chen, Yu-Gang Jiang
conference: Arxiv
year: 2024
bibkey: zhao2024decoder
citations: 0
additional_links: [{name: Code, url: 'https://github.com/Topdu/OpenOCR'}, {name: Paper,
    url: 'https://arxiv.org/abs/2408.05706'}]
tags: []
short_authors: Zhao et al.
---
Scene text recognition (STR) pre-training methods have achieved remarkable
progress, primarily relying on synthetic datasets. However, the domain gap
between synthetic and real images poses a challenge in acquiring feature
representations that align well with images on real scenes, thereby limiting
the performance of these methods. We note that vision-language models like
CLIP, pre-trained on extensive real image-text pairs, effectively align images
and text in a unified embedding space, suggesting the potential to derive the
representations of real images from text alone. Building upon this premise, we
introduce a novel method named Decoder Pre-training with only text for STR
(DPTR). DPTR treats text embeddings produced by the CLIP text encoder as pseudo
visual embeddings and uses them to pre-train the decoder. An Offline Randomized
Perturbation (ORP) strategy is introduced. It enriches the diversity of text
embeddings by incorporating natural image embeddings extracted from the CLIP
image encoder, effectively directing the decoder to acquire the potential
representations of real images. In addition, we introduce a Feature Merge Unit
(FMU) that guides the extracted visual embeddings focusing on the character
foreground within the text image, thereby enabling the pre-trained decoder to
work more efficiently and accurately. Extensive experiments across various STR
decoders and language recognition tasks underscore the broad applicability and
remarkable performance of DPTR, providing a novel insight for STR pre-training.
Code is available at https://github.com/Topdu/OpenOCR