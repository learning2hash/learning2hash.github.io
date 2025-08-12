---
layout: publication
title: 'Musicscore: A Dataset For Music Score Modeling And Generation'
authors: Yuheng Lin, Zheqi Dai, Qiuqiang Kong
conference: Arxiv
year: 2024
bibkey: lin2024musicscore
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.11462'}]
tags: ["Datasets"]
short_authors: Yuheng Lin, Zheqi Dai, Qiuqiang Kong
---
Music scores are written representations of music and contain rich
information about musical components. The visual information on music scores
includes notes, rests, staff lines, clefs, dynamics, and articulations. This
visual information in music scores contains more semantic information than
audio and symbolic representations of music. Previous music score datasets have
limited sizes and are mainly designed for optical music recognition (OMR).
There is a lack of research on creating a large-scale benchmark dataset for
music modeling and generation. In this work, we propose MusicScore, a
large-scale music score dataset collected and processed from the International
Music Score Library Project (IMSLP). MusicScore consists of image-text pairs,
where the image is a page of a music score and the text is the metadata of the
music. The metadata of MusicScore is extracted from the general information
section of the IMSLP pages. The metadata includes rich information about the
composer, instrument, piece style, and genre of the music pieces. MusicScore is
curated into small, medium, and large scales of 400, 14k, and 200k image-text
pairs with varying diversity, respectively. We build a score generation system
based on a UNet diffusion model to generate visually readable music scores
conditioned on text descriptions to benchmark the MusicScore dataset for music
score generation. MusicScore is released to the public at
https://huggingface.co/datasets/ZheqiDAI/MusicScore.