---
layout: publication
title: Bridging Synthetic And Real Worlds For Pre-training Scene Text Detectors
authors: Tongkun Guan, Wei Shen, Xue Yang, Xuehui Wang, Xiaokang Yang
conference: Lecture Notes in Computer Science
year: 2024
bibkey: guan2023bridging
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.05286'}]
tags: ["Datasets", "Evaluation"]
short_authors: Guan et al.
---
Existing scene text detection methods typically rely on extensive real data
for training. Due to the lack of annotated real images, recent works have
attempted to exploit large-scale labeled synthetic data (LSD) for pre-training
text detectors. However, a synth-to-real domain gap emerges, further limiting
the performance of text detectors. Differently, in this work, we propose
FreeReal, a real-domain-aligned pre-training paradigm that enables the
complementary strengths of both LSD and unlabeled real data (URD).
Specifically, to bridge real and synthetic worlds for pre-training, a
glyph-based mixing mechanism (GlyphMix) is tailored for text images.GlyphMix
delineates the character structures of synthetic images and embeds them as
graffiti-like units onto real images. Without introducing real domain drift,
GlyphMix freely yields real-world images with annotations derived from
synthetic labels. Furthermore, when given free fine-grained synthetic labels,
GlyphMix can effectively bridge the linguistic domain gap stemming from
English-dominated LSD to URD in various languages. Without bells and whistles,
FreeReal achieves average gains of 1.97%, 3.90%, 3.85%, and 4.56% in improving
the performance of FCENet, PSENet, PANet, and DBNet methods, respectively,
consistently outperforming previous pre-training methods by a substantial
margin across four public datasets. Code is available at
https://github.com/SJTU-DeepVisionLab/FreeReal.