---
layout: publication
title: 'Impression-clip: Contrastive Shape-impression Embedding For Fonts'
authors: Yugo Kubota, Daichi Haraguchi, Seiichi Uchida
conference: Arxiv
year: 2024
bibkey: kubota2024impression
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.16350'}]
tags: ["Multimodal Retrieval"]
short_authors: Yugo Kubota, Daichi Haraguchi, Seiichi Uchida
---
Fonts convey different impressions to readers. These impressions often come
from the font shapes. However, the correlation between fonts and their
impression is weak and unstable because impressions are subjective. To capture
such weak and unstable cross-modal correlation between font shapes and their
impressions, we propose Impression-CLIP, which is a novel machine-learning
model based on CLIP (Contrastive Language-Image Pre-training). By using the
CLIP-based model, font image features and their impression features are pulled
closer, and font image features and unrelated impression features are pushed
apart. This procedure realizes co-embedding between font image and their
impressions. In our experiment, we perform cross-modal retrieval between fonts
and impressions through co-embedding. The results indicate that Impression-CLIP
achieves better retrieval accuracy than the state-of-the-art method.
Additionally, our model shows the robustness to noise and missing tags.