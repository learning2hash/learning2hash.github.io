---
layout: publication
title: Image Embedding Sampling Method For Diverse Captioning
authors: Sania Waheed, Na Min An
conference: Arxiv
year: 2025
bibkey: waheed2025image
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.10118'}]
tags: []
short_authors: Sania Waheed, Na Min An
---
Image Captioning for state-of-the-art VLMs has significantly improved over
time; however, this comes at the cost of increased computational complexity,
making them less accessible for resource-constrained applications such as
mobile devices and assistive technologies. Alternatively, smaller VLMs
prioritize high-level scene descriptions, overlooking finer details that
contribute to a richer understanding of an image. In this paper, we introduce a
training-free framework that enhances caption diversity and informativeness by
explicitly attending to distinct image regions using a comparably small VLM,
BLIP, as the backbone. Our approach leverages structured segmentation to
produce hierarchical representations that capture both global and localized
semantics. Without requiring additional model training, we demonstrate that our
method allows smaller VLMs to achieve performance comparable to larger models
in terms of image-caption alignment, semantic integrity, and diversity. We
evaluate our framework on MSCOCO, Flickr30k, and Nocaps test datasets,
achieving a Div-2 score of 0.735, 0.750, and 0.748 for each dataset
respectively, while maintaining strong image-caption relevancy and semantic
integrity with the human-annotated captions.