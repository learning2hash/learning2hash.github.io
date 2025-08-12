---
layout: publication
title: 'Dadagp: A Dataset Of Tokenized Guitarpro Songs For Sequence Models'
authors: Pedro Sarmento, Adarsh Kumar, Cj Carr, Zack Zukowski, Mathieu Barthet, Yi-Hsuan
  Yang
conference: Arxiv
year: 2021
bibkey: sarmento2021dadagp
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.14653'}]
tags: ["Datasets"]
short_authors: Sarmento et al.
---
Originating in the Renaissance and burgeoning in the digital era, tablatures
are a commonly used music notation system which provides explicit
representations of instrument fingerings rather than pitches. GuitarPro has
established itself as a widely used tablature format and software enabling
musicians to edit and share songs for musical practice, learning, and
composition. In this work, we present DadaGP, a new symbolic music dataset
comprising 26,181 song scores in the GuitarPro format covering 739 musical
genres, along with an accompanying tokenized format well-suited for generative
sequence models such as the Transformer. The tokenized format is inspired by
event-based MIDI encodings, often used in symbolic music generation models. The
dataset is released with an encoder/decoder which converts GuitarPro files to
tokens and back. We present results of a use case in which DadaGP is used to
train a Transformer-based model to generate new songs in GuitarPro format. We
discuss other relevant use cases for the dataset (guitar-bass transcription,
music style transfer and artist/genre classification) as well as ethical
implications. DadaGP opens up the possibility to train GuitarPro score
generators, fine-tune models on custom data, create new styles of music,
AI-powered songwriting apps, and human-AI improvisation.