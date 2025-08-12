---
layout: publication
title: Decoding The Underlying Meaning Of Multimodal Hateful Memes
authors: Ming Shan Hee, Wen-Haw Chong, Roy Ka-Wei Lee
conference: Proceedings of the Thirty-Second International Joint Conference on Artificial
  Intelligence
year: 2023
bibkey: hee2023decoding
citations: 17
additional_links: [{name: Code, url: 'https://github.com/Social-AI-Studio/HatRed'},
  {name: Paper, url: 'https://arxiv.org/abs/2305.17678'}]
tags: ["IJCAI"]
short_authors: Ming Shan Hee, Wen-Haw Chong, Roy Ka-Wei Lee
---
Recent studies have proposed models that yielded promising performance for
the hateful meme classification task. Nevertheless, these proposed models do
not generate interpretable explanations that uncover the underlying meaning and
support the classification output. A major reason for the lack of explainable
hateful meme methods is the absence of a hateful meme dataset that contains
ground truth explanations for benchmarking or training. Intuitively, having
such explanations can educate and assist content moderators in interpreting and
removing flagged hateful memes. This paper address this research gap by
introducing Hateful meme with Reasons Dataset (HatReD), which is a new
multimodal hateful meme dataset annotated with the underlying hateful
contextual reasons. We also define a new conditional generation task that aims
to automatically generate underlying reasons to explain hateful memes and
establish the baseline performance of state-of-the-art pre-trained language
models on this task. We further demonstrate the usefulness of HatReD by
analyzing the challenges of the new conditional generation task in explaining
memes in seen and unseen domains. The dataset and benchmark models are made
available here: https://github.com/Social-AI-Studio/HatRed