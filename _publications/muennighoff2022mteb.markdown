---
layout: publication
title: 'MTEB: Massive Text Embedding Benchmark'
authors: "Niklas Muennighoff, Nouamane Tazi, Lo\xEFc Magne, Nils Reimers"
conference: Proceedings of the 17th Conference of the European Chapter of the Association
  for Computational Linguistics
year: 2023
bibkey: muennighoff2022mteb
citations: 189
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2210.07316'}]
tags: ["Datasets", "Evaluation"]
short_authors: Muennighoff et al.
---
Text embeddings are commonly evaluated on a small set of datasets from a
single task not covering their possible applications to other tasks. It is
unclear whether state-of-the-art embeddings on semantic textual similarity
(STS) can be equally well applied to other tasks like clustering or reranking.
This makes progress in the field difficult to track, as various models are
constantly being proposed without proper evaluation. To solve this problem, we
introduce the Massive Text Embedding Benchmark (MTEB). MTEB spans 8 embedding
tasks covering a total of 58 datasets and 112 languages. Through the
benchmarking of 33 models on MTEB, we establish the most comprehensive
benchmark of text embeddings to date. We find that no particular text embedding
method dominates across all tasks. This suggests that the field has yet to
converge on a universal text embedding method and scale it up sufficiently to
provide state-of-the-art results on all embedding tasks. MTEB comes with
open-source code and a public leaderboard at
https://github.com/embeddings-benchmark/mteb.