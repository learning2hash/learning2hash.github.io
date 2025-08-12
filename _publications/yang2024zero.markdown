---
layout: publication
title: Zero-shot Sketch-based Remote Sensing Image Retrieval Based On Multi-level
  And Attention-guided Tokenization
authors: Bo Yang, Chen Wang, Xiaoshuang Ma, Beiping Song, Zhuang Liu, Fangde Sun
conference: Remote Sensing
year: 2024
bibkey: yang2024zero
citations: 2
additional_links: [{name: Code, url: 'https://github.com/Snowstormfly/Cross-modal-retrieval-MLAGT'},
  {name: Paper, url: 'https://arxiv.org/abs/2402.02141'}]
tags: ["Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Yang et al.
---
Effectively and efficiently retrieving images from remote sensing databases
is a critical challenge in the realm of remote sensing big data. Utilizing
hand-drawn sketches as retrieval inputs offers intuitive and user-friendly
advantages, yet the potential of multi-level feature integration from sketches
remains underexplored, leading to suboptimal retrieval performance. To address
this gap, our study introduces a novel zero-shot, sketch-based retrieval method
for remote sensing images, leveraging multi-level feature extraction,
self-attention-guided tokenization and filtering, and cross-modality attention
update. This approach employs only vision information and does not require
semantic knowledge concerning the sketch and image. It starts by employing
multi-level self-attention guided feature extraction to tokenize the query
sketches, as well as self-attention feature extraction to tokenize the
candidate images. It then employs cross-attention mechanisms to establish token
correspondence between these two modalities, facilitating the computation of
sketch-to-image similarity. Our method significantly outperforms existing
sketch-based remote sensing image retrieval techniques, as evidenced by tests
on multiple datasets. Notably, it also exhibits robust zero-shot learning
capabilities and strong generalizability in handling unseen categories and
novel remote sensing data. The method's scalability can be further enhanced by
the pre-calculation of retrieval tokens for all candidate images in a database.
This research underscores the significant potential of multi-level,
attention-guided tokenization in cross-modal remote sensing image retrieval.
For broader accessibility and research facilitation, we have made the code and
dataset used in this study publicly available online. Code and dataset are
available at https://github.com/Snowstormfly/Cross-modal-retrieval-MLAGT.