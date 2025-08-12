---
layout: publication
title: Conceptual Compression Via Deep Structure And Texture Synthesis
authors: Jianhui Chang, Zhenghui Zhao, Chuanmin Jia, Shiqi Wang, Lingbo Yang, Qi Mao,
  Jian Zhang, Siwei Ma
conference: IEEE Transactions on Image Processing
year: 2022
bibkey: chang2020conceptual
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.04976'}]
tags: []
short_authors: Chang et al.
---
Existing compression methods typically focus on the removal of signal-level
redundancies, while the potential and versatility of decomposing visual data
into compact conceptual components still lack further study. To this end, we
propose a novel conceptual compression framework that encodes visual data into
compact structure and texture representations, then decodes in a deep synthesis
fashion, aiming to achieve better visual reconstruction quality, flexible
content manipulation, and potential support for various vision tasks. In
particular, we propose to compress images by a dual-layered model consisting of
two complementary visual features: 1) structure layer represented by structural
maps and 2) texture layer characterized by low-dimensional deep
representations. At the encoder side, the structural maps and texture
representations are individually extracted and compressed, generating the
compact, interpretable, inter-operable bitstreams. During the decoding stage, a
hierarchical fusion GAN (HF-GAN) is proposed to learn the synthesis paradigm
where the textures are rendered into the decoded structural maps, leading to
high-quality reconstruction with remarkable visual realism. Extensive
experiments on diverse images have demonstrated the superiority of our
framework with lower bitrates, higher reconstruction quality, and increased
versatility towards visual analysis and content manipulation tasks.