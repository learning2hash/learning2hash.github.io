---
layout: publication
title: 'Link And Code: Fast Indexing With Graphs And Compact Regression Codes'
authors: "Douze Matthijs, Sablayrolles Alexandre, J\xE9gou Herv\xE9"
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: douze2018link
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.09996'}]
tags: ["CVPR", "Compact Codes", "Efficiency", "Graph-based ANN", "Large-Scale Search", "Quantization", "Scalability", "Similarity Search"]
short_authors: "Douze Matthijs, Sablayrolles Alexandre, J\xE9gou Herv\xE9"
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