---
layout: publication
title: 'Scene Graph Based Image Retrieval -- A Case Study On The CLEVR Dataset'
authors: Sahana Ramnath, Amrita Saha, Soumen Chakrabarti, Mitesh M. Khapra
conference: "Arxiv"
year: 2019
citations: 9
bibkey: ramnath2019scene
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1911.00850'}
tags: ['Cross-Modal', 'Retrieval Models', 'Shallow', 'Supervised', 'Applications']
---
With the prolification of multimodal interaction in various domains, recently
there has been much interest in text based image retrieval in the computer
vision community. However most of the state of the art techniques model this
problem in a purely neural way, which makes it difficult to incorporate
pragmatic strategies in searching a large scale catalog especially when the
search requirements are insufficient and the model needs to resort to an
interactive retrieval process through multiple iterations of
question-answering. Motivated by this, we propose a neural-symbolic approach
for a one-shot retrieval of images from a large scale catalog, given the
caption description. To facilitate this, we represent the catalog and caption
as scene-graphs and model the retrieval task as a learnable graph matching
problem, trained end-to-end with a REINFORCE algorithm. Further, we briefly
describe an extension of this pipeline to an iterative retrieval framework,
based on interactive questioning and answering.
