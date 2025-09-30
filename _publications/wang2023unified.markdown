---
layout: publication
title: Unified Coarse-to-fine Alignment For Video-text Retrieval
authors: Ziyang Wang, Yi-Lin Sung, Feng Cheng, Gedas Bertasius, Mohit Bansal
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: wang2023unified
citations: 24
additional_links: [{name: Code, url: 'https://github.com/Ziyang412/UCoFiA'}, {name: Paper,
    url: 'https://arxiv.org/abs/2309.10091'}]
tags: ["ICCV", "Text Retrieval", "Video Retrieval"]
short_authors: Wang et al.
---
The canonical approach to video-text retrieval leverages a coarse-grained or
fine-grained alignment between visual and textual information. However,
retrieving the correct video according to the text query is often challenging
as it requires the ability to reason about both high-level (scene) and
low-level (object) visual clues and how they relate to the text query. To this
end, we propose a Unified Coarse-to-fine Alignment model, dubbed UCoFiA.
Specifically, our model captures the cross-modal similarity information at
different granularity levels. To alleviate the effect of irrelevant visual
clues, we also apply an Interactive Similarity Aggregation module (ISA) to
consider the importance of different visual features while aggregating the
cross-modal similarity to obtain a similarity score for each granularity.
Finally, we apply the Sinkhorn-Knopp algorithm to normalize the similarities of
each level before summing them, alleviating over- and under-representation
issues at different levels. By jointly considering the crossmodal similarity of
different granularity, UCoFiA allows the effective unification of multi-grained
alignments. Empirically, UCoFiA outperforms previous state-of-the-art
CLIP-based methods on multiple video-text retrieval benchmarks, achieving 2.4%,
1.4% and 1.3% improvements in text-to-video retrieval R@1 on MSR-VTT,
Activity-Net, and DiDeMo, respectively. Our code is publicly available at
https://github.com/Ziyang412/UCoFiA.