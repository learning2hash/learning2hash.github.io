---
layout: publication
title: A Generative Approach To Titling And Clustering Wikipedia Sections
authors: Anjalie Field, Sascha Rothe, Simon Baumgartner, Cong Yu, Abe Ittycheriah
conference: Proceedings of the Fourth Workshop on Neural Generation and Translation
year: 2020
bibkey: field2020generative
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.11216'}]
tags: ["Evaluation"]
short_authors: Field et al.
---
We evaluate the performance of transformer encoders with various decoders for
information organization through a new task: generation of section headings for
Wikipedia articles. Our analysis shows that decoders containing attention
mechanisms over the encoder output achieve high-scoring results by generating
extractive text. In contrast, a decoder without attention better facilitates
semantic encoding and can be used to generate section embeddings. We
additionally introduce a new loss function, which further encourages the
decoder to generate high-quality embeddings.