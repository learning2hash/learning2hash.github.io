---
layout: publication
title: 'Multidimensional Byte Pair Encoding: Shortened Sequences For Improved Visual
  Data Generation'
authors: Tim Elsner, Paula Usinger, Julius Nehring-Wirxel, Gregor Kobsik, Victor Czech,
  Yanjiang He, Isaak Lim, Leif Kobbelt
conference: Arxiv
year: 2024
bibkey: elsner2024multidimensional
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.10281'}]
tags: []
short_authors: Elsner et al.
---
In language processing, transformers benefit greatly from text being
condensed. This is achieved through a larger vocabulary that captures word
fragments instead of plain characters. This is often done with Byte Pair
Encoding. In the context of images, tokenisation of visual data is usually
limited to regular grids obtained from quantisation methods, without global
content awareness. Our work improves tokenisation of visual data by bringing
Byte Pair Encoding from 1D to multiple dimensions, as a complementary add-on to
existing compression. We achieve this through counting constellations of token
pairs and replacing the most frequent token pair with a newly introduced token.
The multidimensionality only increases the computation time by a factor of 2
for images, making it applicable even to large datasets like ImageNet within
minutes on consumer hardware. This is a lossless preprocessing step. Our
evaluation shows improved training and inference performance of transformers on
visual data achieved by compressing frequent constellations of tokens: The
resulting sequences are shorter, with more uniformly distributed information
content, e.g. condensing empty regions in an image into single tokens. As our
experiments show, these condensed sequences are easier to process. We
additionally introduce a strategy to amplify this compression further by
clustering the vocabulary.