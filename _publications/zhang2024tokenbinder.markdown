---
layout: publication
title: 'Tokenbinder: Text-video Retrieval With One-to-many Alignment Paradigm'
authors: Bingqing Zhang, Zhuo Cao, Heming Du, Xin Yu, Xue Li, Jiajun Liu, Sen Wang
conference: Arxiv
year: 2024
bibkey: zhang2024tokenbinder
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.19865'}]
tags: ["Evaluation", "Robustness", "Video Retrieval"]
short_authors: Zhang et al.
---
Text-Video Retrieval (TVR) methods typically match query-candidate pairs by
aligning text and video features in coarse-grained, fine-grained, or combined
(coarse-to-fine) manners. However, these frameworks predominantly employ a
one(query)-to-one(candidate) alignment paradigm, which struggles to discern
nuanced differences among candidates, leading to frequent mismatches. Inspired
by Comparative Judgement in human cognitive science, where decisions are made
by directly comparing items rather than evaluating them independently, we
propose TokenBinder. This innovative two-stage TVR framework introduces a novel
one-to-many coarse-to-fine alignment paradigm, imitating the human cognitive
process of identifying specific items within a large collection. Our method
employs a Focused-view Fusion Network with a sophisticated cross-attention
mechanism, dynamically aligning and comparing features across multiple videos
to capture finer nuances and contextual variations. Extensive experiments on
six benchmark datasets confirm that TokenBinder substantially outperforms
existing state-of-the-art methods. These results demonstrate its robustness and
the effectiveness of its fine-grained alignment in bridging intra- and
inter-modality information gaps in TVR tasks.