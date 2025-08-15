---
layout: publication
title: 'VISAGE: Video Instance Segmentation With Appearance-guided Enhancement'
authors: Hanjung Kim, Jaehyun Kang, Miran Heo, Sukjun Hwang, Seoung Wug Oh, Seon Joo
  Kim
conference: Lecture Notes in Computer Science
year: 2024
bibkey: kim2024visage
citations: 0
additional_links: [{name: Code, url: 'https://github.com/KimHanjung/VISAGE.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2312.04885'}]
tags: ["Datasets"]
short_authors: Kim et al.
---
In recent years, online Video Instance Segmentation (VIS) methods have shown
remarkable advancement with their powerful query-based detectors. Utilizing the
output queries of the detector at the frame-level, these methods achieve high
accuracy on challenging benchmarks. However, our observations demonstrate that
these methods heavily rely on location information, which often causes
incorrect associations between objects. This paper presents that a key axis of
object matching in trackers is appearance information, which becomes greatly
instructive under conditions where positional cues are insufficient for
distinguishing their identities. Therefore, we suggest a simple yet powerful
extension to object decoders that explicitly extract embeddings from backbone
features and drive queries to capture the appearances of objects, which greatly
enhances instance association accuracy. Furthermore, recognizing the
limitations of existing benchmarks in fully evaluating appearance awareness, we
have constructed a synthetic dataset to rigorously validate our method. By
effectively resolving the over-reliance on location information, we achieve
state-of-the-art results on YouTube-VIS 2019/2021 and Occluded VIS (OVIS). Code
is available at https://github.com/KimHanjung/VISAGE.