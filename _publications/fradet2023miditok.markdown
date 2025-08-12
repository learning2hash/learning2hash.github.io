---
layout: publication
title: 'Miditok: A Python Package For MIDI File Tokenization'
authors: Nathan Fradet, Jean-Pierre Briot, Fabien Chhel, Amal El Fallah Seghrouchni,
  Nicolas Gutowski
conference: Arxiv
year: 2023
bibkey: fradet2023miditok
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.17202'}]
tags: ["Tools & Libraries"]
short_authors: Fradet et al.
---
Recent progress in natural language processing has been adapted to the
symbolic music modality. Language models, such as Transformers, have been used
with symbolic music for a variety of tasks among which music generation,
modeling or transcription, with state-of-the-art performances. These models are
beginning to be used in production products. To encode and decode music for the
backbone model, they need to rely on tokenizers, whose role is to serialize
music into sequences of distinct elements called tokens. MidiTok is an
open-source library allowing to tokenize symbolic music with great flexibility
and extended features. It features the most popular music tokenizations, under
a unified API. It is made to be easily used and extensible for everyone.