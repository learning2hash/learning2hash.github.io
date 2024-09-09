---
layout: publication
title: "Compositional Sketch Search"
authors: Black Alexander, Bui Tu, Mai Long, Jin Hailin, Collomosse John
conference: Arxiv
year: 2021
bibkey: black2021compositional
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2106.08009"}
tags: ['ARXIV', 'CNN', 'Image Retrieval', 'Quantisation', 'TIP']
---
We present an algorithm for searching image collections using free-hand sketches
that describe the appearance and relative positions of multiple objects. Sketch
based image retrieval (SBIR) methods predominantly match queries containing a
single, dominant object invariant to its position within an image. Our work
exploits drawings as a concise and intuitive representation for specifying
entire scene compositions. We train a convolutional neural network (CNN) to
encode masked visual features from sketched objects, pooling these into a
spatial descriptor encoding the spatial relationships and appearances of objects
in the composition. Training the CNN backbone as a Siamese network under triplet
loss yields a metric search embedding for measuring compositional similarity
which may be efficiently leveraged for visual search by applying product
quantization.
