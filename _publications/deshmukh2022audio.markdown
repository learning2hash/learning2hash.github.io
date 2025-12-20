---
layout: publication
title: Audio Retrieval With Wavtext5k And CLAP Training
authors: Soham Deshmukh, Benjamin Elizalde, Huaming Wang
conference: Arxiv
year: 2022
bibkey: deshmukh2022audio
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.14275'}]
tags: ["Audio Retrieval", "Datasets", "Evaluation", "Text Retrieval", "Tools & Libraries"]
short_authors: Soham Deshmukh, Benjamin Elizalde, Huaming Wang
---
Audio-Text retrieval takes a natural language query to retrieve relevant
audio files in a database. Conversely, Text-Audio retrieval takes an audio file
as a query to retrieve relevant natural language descriptions. Most of the
literature train retrieval systems with one audio captioning dataset, but
evaluating the benefit of training with multiple datasets is underexplored.
Moreover, retrieval systems have to learn the alignment between elaborated
sentences describing audio content of variable length ranging from a few
seconds to several minutes. In this work, we propose a new collection of web
audio-text pairs and a new framework for retrieval. First, we provide a new
collection of about five thousand web audio-text pairs that we refer to as
WavText5K. When used to train our retrieval system, WavText5K improved
performance more than other audio captioning datasets. Second, our framework
learns to connect language and audio content by using a text encoder, two audio
encoders, and a contrastive learning objective. Combining both audio encoders
helps to process variable length audio. The two contributions beat state of the
art performance for AudioCaps and Clotho on Text-Audio retrieval by a relative
2% and 16%, and Audio-Text retrieval by 6% and 23%.