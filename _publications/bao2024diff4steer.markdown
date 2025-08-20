---
layout: publication
title: 'Diff4steer: Steerable Diffusion Prior For Generative Music Retrieval With
  Semantic Guidance'
authors: Xuchan Bao, Judith Yue Li, Zhong Yi Wan, Kun Su, Timo Denk, Joonseok Lee,
  Dima Kuzmin, Fei Sha
conference: ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2025
bibkey: bao2024diff4steer
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.04746'}]
tags: [Tools & Libraries, ICASSP, Evaluation]
short_authors: Bao et al.
---
Modern music retrieval systems often rely on fixed representations of user
preferences, limiting their ability to capture users' diverse and uncertain
retrieval needs. To address this limitation, we introduce Diff4Steer, a novel
generative retrieval framework that employs lightweight diffusion models to
synthesize diverse seed embeddings from user queries that represent potential
directions for music exploration. Unlike deterministic methods that map user
query to a single point in embedding space, Diff4Steer provides a statistical
prior on the target modality (audio) for retrieval, effectively capturing the
uncertainty and multi-faceted nature of user preferences. Furthermore,
Diff4Steer can be steered by image or text inputs, enabling more flexible and
controllable music discovery combined with nearest neighbor search. Our
framework outperforms deterministic regression methods and LLM-based generative
retrieval baseline in terms of retrieval and ranking metrics, demonstrating its
effectiveness in capturing user preferences, leading to more diverse and
relevant recommendations. Listening examples are available at
tinyurl.com/diff4steer.