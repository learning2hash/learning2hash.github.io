---
layout: publication
title: Building A Hebrew Semantic Role Labeling Lexical Resource From Parallel Movie
  Subtitles
authors: Ben Eyal, Michael Elhadad
conference: Proceedings of The 12th Language Resources and Evaluation Conference (2020)
  5936-5944
year: 2020
bibkey: eyal2020building
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.08206'}]
tags: ["Datasets", "LREC"]
short_authors: Ben Eyal, Michael Elhadad
---
We present a semantic role labeling resource for Hebrew built
semi-automatically through annotation projection from English. This corpus is
derived from the multilingual OpenSubtitles dataset and includes short informal
sentences, for which reliable linguistic annotations have been computed. We
provide a fully annotated version of the data including morphological analysis,
dependency syntax and semantic role labeling in both FrameNet and PropBank
styles. Sentences are aligned between English and Hebrew, both sides include
full annotations and the explicit mapping from the English arguments to the
Hebrew ones. We train a neural SRL model on this Hebrew resource exploiting the
pre-trained multilingual BERT transformer model, and provide the first
available baseline model for Hebrew SRL as a reference point. The code we
provide is generic and can be adapted to other languages to bootstrap SRL
resources.