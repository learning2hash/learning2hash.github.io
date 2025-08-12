---
layout: publication
title: 'XGAN: Unsupervised Image-to-image Translation For Many-to-many Mappings'
authors: "Am\xE9lie Royer, Konstantinos Bousmalis, Stephan Gouws, Fred Bertsch, Inbar\
  \ Mosseri, Forrester Cole, Kevin Murphy"
conference: Arxiv
year: 2017
bibkey: royer2017xgan
citations: 74
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.05139'}]
tags: ["Unsupervised"]
short_authors: Royer et al.
---
Style transfer usually refers to the task of applying color and texture
information from a specific style image to a given content image while
preserving the structure of the latter. Here we tackle the more generic problem
of semantic style transfer: given two unpaired collections of images, we aim to
learn a mapping between the corpus-level style of each collection, while
preserving semantic content shared across the two domains. We introduce XGAN
("Cross-GAN"), a dual adversarial autoencoder, which captures a shared
representation of the common domain semantic content in an unsupervised way,
while jointly learning the domain-to-domain image translations in both
directions. We exploit ideas from the domain adaptation literature and define a
semantic consistency loss which encourages the model to preserve semantics in
the learned embedding space. We report promising qualitative results for the
task of face-to-cartoon translation. The cartoon dataset, CartoonSet, we
collected for this purpose is publicly available at
google.github.io/cartoonset/ as a new benchmark for semantic style transfer.