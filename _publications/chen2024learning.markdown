---
layout: publication
title: Learning High-quality And General-purpose Phrase Representations
authors: "Lihu Chen, Ga\xEBl Varoquaux, Fabian M. Suchanek"
conference: Arxiv
year: 2024
bibkey: chen2024learning
citations: 0
additional_links: [{name: Code, url: 'https://huggingface.co/Lihuchen/pearl_small;'},
  {name: Code, url: 'https://huggingface.co/Lihuchen/pearl_base;'}, {name: Code, url: 'https://github.com/tigerchen52/PEARL'},
  {name: Paper, url: 'https://arxiv.org/abs/2401.10407'}]
tags: ["Self-Supervised"]
short_authors: "Lihu Chen, Ga\xEBl Varoquaux, Fabian M. Suchanek"
---
Phrase representations play an important role in data science and natural
language processing, benefiting various tasks like Entity Alignment, Record
Linkage, Fuzzy Joins, and Paraphrase Classification. The current
state-of-the-art method involves fine-tuning pre-trained language models for
phrasal embeddings using contrastive learning. However, we have identified
areas for improvement. First, these pre-trained models tend to be unnecessarily
complex and require to be pre-trained on a corpus with context sentences.
Second, leveraging the phrase type and morphology gives phrase representations
that are both more precise and more flexible. We propose an improved framework
to learn phrase representations in a context-free fashion. The framework
employs phrase type classification as an auxiliary task and incorporates
character-level information more effectively into the phrase representation.
Furthermore, we design three granularities of data augmentation to increase the
diversity of training samples. Our experiments across a wide range of tasks
show that our approach generates superior phrase embeddings compared to
previous methods while requiring a smaller model size. [PEARL-small]:
https://huggingface.co/Lihuchen/pearl_small; [PEARL-base]:
https://huggingface.co/Lihuchen/pearl_base; [Code and Dataset]:
https://github.com/tigerchen52/PEARL