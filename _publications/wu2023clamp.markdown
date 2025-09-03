---
layout: publication
title: 'Clamp: Contrastive Language-music Pre-training For Cross-modal Symbolic Music
  Information Retrieval'
authors: Shangda Wu, Dingyao Yu, Xu Tan, Maosong Sun
conference: Arxiv
year: 2023
bibkey: wu2023clamp
citations: 1
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2304.11029'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Few Shot & Zero Shot"]
short_authors: Wu et al.
---
We introduce CLaMP: Contrastive Language-Music Pre-training, which learns
cross-modal representations between natural language and symbolic music using a
music encoder and a text encoder trained jointly with a contrastive loss. To
pre-train CLaMP, we collected a large dataset of 1.4 million music-text pairs.
It employed text dropout as a data augmentation technique and bar patching to
efficiently represent music data which reduces sequence length to less than
10%. In addition, we developed a masked music model pre-training objective to
enhance the music encoder's comprehension of musical context and structure.
CLaMP integrates textual information to enable semantic search and zero-shot
classification for symbolic music, surpassing the capabilities of previous
models. To support the evaluation of semantic search and music classification,
we publicly release WikiMusicText (WikiMT), a dataset of 1010 lead sheets in
ABC notation, each accompanied by a title, artist, genre, and description. In
comparison to state-of-the-art models that require fine-tuning, zero-shot CLaMP
demonstrated comparable or superior performance on score-oriented datasets. Our
models and code are available at
https://github.com/microsoft/muzic/tree/main/clamp.