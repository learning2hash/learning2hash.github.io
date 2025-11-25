---
layout: publication
title: Advancing Natural-language Based Audio Retrieval With Passt And Large Audio-caption
  Data Sets
authors: Paul Primus, Khaled Koutini, Gerhard Widmer
conference: Arxiv
year: 2023
bibkey: primus2023advancing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.04258'}]
tags: ["Audio Retrieval", "Evaluation", "Multimodal Retrieval"]
short_authors: Paul Primus, Khaled Koutini, Gerhard Widmer
---
This work presents a text-to-audio-retrieval system based on pre-trained text
and spectrogram transformers. Our method projects recordings and textual
descriptions into a shared audio-caption space in which related examples from
different modalities are close. Through a systematic analysis, we examine how
each component of the system influences retrieval performance. As a result, we
identify two key components that play a crucial role in driving performance:
the self-attention-based audio encoder for audio embedding and the utilization
of additional human-generated and synthetic data sets during pre-training. We
further experimented with augmenting ClothoV2 captions with available keywords
to increase their variety; however, this only led to marginal improvements. Our
system ranked first in the 2023's DCASE Challenge, and it outperforms the
current state of the art on the ClothoV2 benchmark by 5.6 pp. mAP@10.