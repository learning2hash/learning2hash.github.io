---
layout: publication
title: 'Link And Code: Fast Indexing With Graphs And Compact Regression Codes'
authors: "Matthijs Douze, Alexandre Sablayrolles, Herv\xE9 J\xE9gou"
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: douze2018link
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.09996'}]
tags: ["CVPR", "Evaluation", "Large Scale Search", "Quantization", "Similarity Search"]
short_authors: "Matthijs Douze, Alexandre Sablayrolles, Herv\xE9 J\xE9gou"
---
Similarity search approaches based on graph walks have recently attained
outstanding speed-accuracy trade-offs, taking aside the memory requirements. In
this paper, we revisit these approaches by considering, additionally, the
memory constraint required to index billions of images on a single server. This
leads us to propose a method based both on graph traversal and compact
representations. We encode the indexed vectors using quantization and exploit
the graph structure to refine the similarity estimation.
  In essence, our method takes the best of these two worlds: the search
strategy is based on nested graphs, thereby providing high precision with a
relatively small set of comparisons. At the same time it offers a significant
memory compression. As a result, our approach outperforms the state of the art
on operating points considering 64-128 bytes per vector, as demonstrated by our
results on two billion-scale public benchmarks.