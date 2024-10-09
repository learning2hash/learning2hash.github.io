---
layout: publication
title: Randomized Positional Encodings Boost Length Generalization Of Transformers
authors: Anian Ruoss, Grégoire Delétang, Tim Genewein, Jordi Grau-moya, Róbert Csordás, Mehdi Bennani, Shane Legg, Joel Veness
conference: "Arxiv"
year: 2023
bibkey: ruoss2023randomized
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2305.16843v1"}
tags: ['ARXIV', 'Independent']
---
Transformers have impressive generalization capabilities on tasks with a fixed context length. However they fail to generalize to sequences of arbitrary length even for seemingly simple tasks such as duplicating a string. Moreover simply training on longer sequences is inefficient due to the quadratic computation complexity of the global attention mechanism. In this work we demonstrate that this failure mode is linked to positional encodings being out-of-distribution for longer sequences (even for relative encodings) and introduce a novel family of positional encodings that can overcome this problem. Concretely our randomized positional encoding scheme simulates the positions of longer sequences and randomly selects an ordered subset to fit the sequences length. Our large-scale empirical evaluation of 6000 models across 15 algorithmic reasoning tasks shows that our method allows Transformers to generalize to sequences of unseen length (increasing test accuracy by 12.037; on average).
