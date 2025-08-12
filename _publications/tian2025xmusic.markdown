---
layout: publication
title: 'Xmusic: Towards A Generalized And Controllable Symbolic Music Generation Framework'
authors: Sida Tian, Can Zhang, Wei Yuan, Wei Tan, Wenjie Zhu
conference: Arxiv
year: 2025
bibkey: tian2025xmusic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.08809'}]
tags: ["Tools & Libraries"]
short_authors: Tian et al.
---
In recent years, remarkable advancements in artificial intelligence-generated
content (AIGC) have been achieved in the fields of image synthesis and text
generation, generating content comparable to that produced by humans. However,
the quality of AI-generated music has not yet reached this standard, primarily
due to the challenge of effectively controlling musical emotions and ensuring
high-quality outputs. This paper presents a generalized symbolic music
generation framework, XMusic, which supports flexible prompts (i.e., images,
videos, texts, tags, and humming) to generate emotionally controllable and
high-quality symbolic music. XMusic consists of two core components, XProjector
and XComposer. XProjector parses the prompts of various modalities into
symbolic music elements (i.e., emotions, genres, rhythms and notes) within the
projection space to generate matching music. XComposer contains a Generator and
a Selector. The Generator generates emotionally controllable and melodious
music based on our innovative symbolic music representation, whereas the
Selector identifies high-quality symbolic music by constructing a multi-task
learning scheme involving quality assessment, emotion recognition, and genre
recognition tasks. In addition, we build XMIDI, a large-scale symbolic music
dataset that contains 108,023 MIDI files annotated with precise emotion and
genre labels. Objective and subjective evaluations show that XMusic
significantly outperforms the current state-of-the-art methods with impressive
music quality. Our XMusic has been awarded as one of the nine Highlights of
Collectibles at WAIC 2023. The project homepage of XMusic is
https://xmusic-project.github.io.