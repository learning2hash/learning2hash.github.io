---
layout: publication
title: Audio-visual Embedding For Cross-modal Musicvideo Retrieval Through Supervised
  Deep CCA
authors: Donghuo Zeng, Yi Yu, Keizo Oyama
conference: Arxiv
year: 2019
bibkey: zeng2019audio
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.03744'}]
tags: [Neural Hashing, Video Retrieval, Datasets, Supervised, Evaluation]
short_authors: Donghuo Zeng, Yi Yu, Keizo Oyama
---
Deep learning has successfully shown excellent performance in learning joint
representations between different data modalities. Unfortunately, little
research focuses on cross-modal correlation learning where temporal structures
of different data modalities, such as audio and video, should be taken into
account. Music video retrieval by given musical audio is a natural way to
search and interact with music contents. In this work, we study cross-modal
music video retrieval in terms of emotion similarity. Particularly, audio of an
arbitrary length is used to retrieve a longer or full-length music video. To
this end, we propose a novel audio-visual embedding algorithm by Supervised
Deep CanonicalCorrelation Analysis (S-DCCA) that projects audio and video into
a shared space to bridge the semantic gap between audio and video. This also
preserves the similarity between audio and visual contents from different
videos with the same class label and the temporal structure. The contribution
of our approach is mainly manifested in the two aspects: i) We propose to
select top k audio chunks by attention-based Long Short-Term Memory
(LSTM)model, which can represent good audio summarization with local
properties. ii) We propose an end-to-end deep model for cross-modal
audio-visual learning where S-DCCA is trained to learn the semantic correlation
between audio and visual modalities. Due to the lack of music video dataset, we
construct 10K music video dataset from YouTube 8M dataset. Some promising
results such as MAP and precision-recall show that our proposed model can be
applied to music video retrieval.