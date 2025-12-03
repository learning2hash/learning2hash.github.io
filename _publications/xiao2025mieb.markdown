---
layout: publication
title: 'MIEB: Massive Image Embedding Benchmark'
authors: "Chenghao Xiao, Isaac Chung, Imene Kerboua, Jamie Stirling, Xin Zhang, M\xE1\
  rton Kardos, Roman Solomatin, Noura Al Moubayed, Kenneth Enevoldsen, Niklas Muennighoff"
conference: Arxiv
year: 2025
bibkey: xiao2025mieb
citations: 0
additional_links: [{name: Code, url: 'https://github.com/embeddings-benchmark/mteb'},
  {name: Paper, url: 'https://arxiv.org/abs/2504.10471'}]
tags: ["Datasets", "Evaluation"]
short_authors: Xiao et al.
---
Image representations are often evaluated through disjointed, task-specific
protocols, leading to a fragmented understanding of model capabilities. For
instance, it is unclear whether an image embedding model adept at clustering
images is equally good at retrieving relevant images given a piece of text. We
introduce the Massive Image Embedding Benchmark (MIEB) to evaluate the
performance of image and image-text embedding models across the broadest
spectrum to date. MIEB spans 38 languages across 130 individual tasks, which we
group into 8 high-level categories. We benchmark 50 models across our
benchmark, finding that no single method dominates across all task categories.
We reveal hidden capabilities in advanced vision models such as their accurate
visual representation of texts, and their yet limited capabilities in
interleaved encodings and matching images and texts in the presence of
confounders. We also show that the performance of vision encoders on MIEB
correlates highly with their performance when used in multimodal large language
models. Our code, dataset, and leaderboard are publicly available at
https://github.com/embeddings-benchmark/mteb.