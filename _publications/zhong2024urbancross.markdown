---
layout: publication
title: 'Urbancross: Enhancing Satellite Image-text Retrieval With Cross-domain Adaptation'
authors: Siru Zhong, Xixuan Hao, Yibo Yan, Ying Zhang, Yangqiu Song, Yuxuan Liang
conference: Proceedings of the 32nd ACM International Conference on Multimedia
year: 2024
bibkey: zhong2024urbancross
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.14241'}]
tags: ["Text Retrieval"]
short_authors: Zhong et al.
---
Urbanization challenges underscore the necessity for effective satellite
image-text retrieval methods to swiftly access specific information enriched
with geographic semantics for urban applications. However, existing methods
often overlook significant domain gaps across diverse urban landscapes,
primarily focusing on enhancing retrieval performance within single domains. To
tackle this issue, we present UrbanCross, a new framework for cross-domain
satellite image-text retrieval. UrbanCross leverages a high-quality,
cross-domain dataset enriched with extensive geo-tags from three countries to
highlight domain diversity. It employs the Large Multimodal Model (LMM) for
textual refinement and the Segment Anything Model (SAM) for visual
augmentation, achieving a fine-grained alignment of images, segments and texts,
yielding a 10% improvement in retrieval performance. Additionally, UrbanCross
incorporates an adaptive curriculum-based source sampler and a weighted
adversarial cross-domain fine-tuning module, progressively enhancing
adaptability across various domains. Extensive experiments confirm UrbanCross's
superior efficiency in retrieval and adaptation to new urban environments,
demonstrating an average performance increase of 15% over its version without
domain adaptation mechanisms, effectively bridging the domain gap.