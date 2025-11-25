---
layout: publication
title: Embedding And Enriching Explicit Semantics For Visible-infrared Person Re-identification
authors: Neng Dong, Shuanglin Yan, Liyan Zhang, Jinhui Tang
conference: Arxiv
year: 2024
bibkey: dong2024embedding
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.08406'}]
tags: ["Image Retrieval", "Multimodal Retrieval"]
short_authors: Dong et al.
---
Visible-infrared person re-identification (VIReID) retrieves pedestrian
images with the same identity across different modalities. Existing methods
learn visual content solely from images, lacking the capability to sense
high-level semantics. In this paper, we propose an Embedding and Enriching
Explicit Semantics (EEES) framework to learn semantically rich cross-modality
pedestrian representations. Our method offers several contributions. First,
with the collaboration of multiple large language-vision models, we develop
Explicit Semantics Embedding (ESE), which automatically supplements language
descriptions for pedestrians and aligns image-text pairs into a common space,
thereby learning visual content associated with explicit semantics. Second,
recognizing the complementarity of multi-view information, we present
Cross-View Semantics Compensation (CVSC), which constructs multi-view
image-text pair representations, establishes their many-to-many matching, and
propagates knowledge to single-view representations, thus compensating visual
content with its missing cross-view semantics. Third, to eliminate noisy
semantics such as conflicting color attributes in different modalities, we
design Cross-Modality Semantics Purification (CMSP), which constrains the
distance between inter-modality image-text pair representations to be close to
that between intra-modality image-text pair representations, further enhancing
the modality-invariance of visual content. Finally, experimental results
demonstrate the effectiveness and superiority of the proposed EEES.