---
layout: publication
title: Contrastive Audio-language Learning For Music
authors: "Ilaria Manco, Emmanouil Benetos, Elio Quinton, Gy\xF6rgy Fazekas"
conference: Arxiv
year: 2022
bibkey: manco2022contrastive
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.12208'}]
tags: ["Few Shot & Zero Shot", "Multimodal Retrieval", "Text Retrieval"]
short_authors: Manco et al.
---
As one of the most intuitive interfaces known to humans, natural language has
the potential to mediate many tasks that involve human-computer interaction,
especially in application-focused fields like Music Information Retrieval. In
this work, we explore cross-modal learning in an attempt to bridge audio and
language in the music domain. To this end, we propose MusCALL, a framework for
Music Contrastive Audio-Language Learning. Our approach consists of a
dual-encoder architecture that learns the alignment between pairs of music
audio and descriptive sentences, producing multimodal embeddings that can be
used for text-to-audio and audio-to-text retrieval out-of-the-box. Thanks to
this property, MusCALL can be transferred to virtually any task that can be
cast as text-based retrieval. Our experiments show that our method performs
significantly better than the baselines at retrieving audio that matches a
textual description and, conversely, text that matches an audio query. We also
demonstrate that the multimodal alignment capability of our model can be
successfully extended to the zero-shot transfer scenario for genre
classification and auto-tagging on two public datasets.