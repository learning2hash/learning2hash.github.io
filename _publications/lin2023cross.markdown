---
layout: publication
title: Cross-modal Adaptive Dual Association For Text-to-image Person Retrieval
authors: Dixuan Lin, Yixing Peng, Jingke Meng, Wei-Shi Zheng
conference: Arxiv
year: 2023
bibkey: lin2023cross
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.01745'}]
tags: ["Image Retrieval", "Multimodal Retrieval"]
short_authors: Lin et al.
---
Text-to-image person re-identification (ReID) aims to retrieve images of a
person based on a given textual description. The key challenge is to learn the
relations between detailed information from visual and textual modalities.
Existing works focus on learning a latent space to narrow the modality gap and
further build local correspondences between two modalities. However, these
methods assume that image-to-text and text-to-image associations are
modality-agnostic, resulting in suboptimal associations. In this work, we show
the discrepancy between image-to-text association and text-to-image association
and propose CADA: Cross-Modal Adaptive Dual Association that finely builds
bidirectional image-text detailed associations. Our approach features a
decoder-based adaptive dual association module that enables full interaction
between visual and textual modalities, allowing for bidirectional and adaptive
cross-modal correspondence associations. Specifically, the paper proposes a
bidirectional association mechanism: Association of text Tokens to image
Patches (ATP) and Association of image Regions to text Attributes (ARA). We
adaptively model the ATP based on the fact that aggregating cross-modal
features based on mistaken associations will lead to feature distortion. For
modeling the ARA, since the attributes are typically the first distinguishing
cues of a person, we propose to explore the attribute-level association by
predicting the masked text phrase using the related image region. Finally, we
learn the dual associations between texts and images, and the experimental
results demonstrate the superiority of our dual formulation. Codes will be made
publicly available.