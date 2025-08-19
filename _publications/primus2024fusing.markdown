---
layout: publication
title: Fusing Audio And Metadata Embeddings Improves Language-based Audio Retrieval
authors: Paul Primus, Gerhard Widmer
conference: Arxiv
year: 2024
bibkey: primus2024fusing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.15897'}]
tags: [Evaluation]
short_authors: Paul Primus, Gerhard Widmer
---
Matching raw audio signals with textual descriptions requires understanding
the audio's content and the description's semantics and then drawing
connections between the two modalities. This paper investigates a hybrid
retrieval system that utilizes audio metadata as an additional clue to
understand the content of audio signals before matching them with textual
queries. We experimented with metadata often attached to audio recordings, such
as keywords and natural-language descriptions, and we investigated late and
mid-level fusion strategies to merge audio and metadata. Our hybrid approach
with keyword metadata and late fusion improved the retrieval performance over a
content-based baseline by 2.36 and 3.69 pp. mAP@10 on the ClothoV2 and
AudioCaps benchmarks, respectively.