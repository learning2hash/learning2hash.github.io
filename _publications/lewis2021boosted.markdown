---
layout: publication
title: Boosted Dense Retriever
authors: "Patrick Lewis, Barlas O\u011Fuz, Wenhan Xiong, Fabio Petroni, Wen-Tau Yih,\
  \ Sebastian Riedel"
conference: Arxiv
year: 2021
bibkey: lewis2021boosted
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.07771'}]
tags: ["Efficiency", "Large Scale Search", "Memory Efficiency", "Quantization"]
short_authors: Lewis et al.
---
We propose DrBoost, a dense retrieval ensemble inspired by boosting. DrBoost
is trained in stages: each component model is learned sequentially and
specialized by focusing only on retrieval mistakes made by the current
ensemble. The final representation is the concatenation of the output vectors
of all the component models, making it a drop-in replacement for standard dense
retrievers at test time. DrBoost enjoys several advantages compared to standard
dense retrieval models. It produces representations which are 4x more compact,
while delivering comparable retrieval results. It also performs surprisingly
well under approximate search with coarse quantization, reducing latency and
bandwidth needs by another 4x. In practice, this can make the difference
between serving indices from disk versus from memory, paving the way for much
cheaper deployments.