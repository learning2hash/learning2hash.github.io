---
layout: publication
title: 'Luojiahog: A Hierarchy Oriented Geo-aware Image Caption Dataset For Remote
  Sensing Image-text Retrival'
authors: Yuanxin Zhao, Mi Zhang, Bingnan Yang, Zhan Zhang, Jiaju Kang, Jianya Gong
conference: Arxiv
year: 2024
bibkey: zhao2024luojiahog
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.10887'}]
tags: ["Datasets", "Evaluation", "Image Retrieval"]
short_authors: Zhao et al.
---
Image-text retrieval (ITR) plays a significant role in making informed
decisions for various remote sensing (RS) applications. Nonetheless, creating
ITR datasets containing vision and language modalities not only requires
significant geo-spatial sampling area but also varing categories and detailed
descriptions. To this end, we introduce an image caption dataset LuojiaHOG,
which is geospatial-aware, label-extension-friendly and
comprehensive-captioned. LuojiaHOG involves the hierarchical spatial sampling,
extensible classification system to Open Geospatial Consortium (OGC) standards,
and detailed caption generation. In addition, we propose a CLIP-based Image
Semantic Enhancement Network (CISEN) to promote sophisticated ITR. CISEN
consists of two components, namely dual-path knowledge transfer and progressive
cross-modal feature fusion. Comprehensive statistics on LuojiaHOG reveal the
richness in sampling diversity, labels quantity and descriptions granularity.
The evaluation on LuojiaHOG is conducted across various state-of-the-art ITR
models, including ALBEF, ALIGN, CLIP, FILIP, Wukong, GeoRSCLIP and CISEN. We
use second- and third-level labels to evaluate these vision-language models
through adapter-tuning and CISEN demonstrates superior performance. For
instance, it achieves the highest scores with WMAP@5 of 88.47% and 87.28% on
third-level ITR tasks, respectively. In particular, CISEN exhibits an
improvement of approximately 1.3% and 0.9% in terms of WMAP@5 compared to its
baseline. These findings highlight CISEN advancements accurately retrieving
pertinent information across image and text. LuojiaHOG and CISEN can serve as a
foundational resource for future RS image-text alignment research, facilitating
a wide range of vision-language applications.