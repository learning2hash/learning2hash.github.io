---
layout: publication
title: 'Descriptellation: Deep Learned Constellation Descriptors'
authors: Chunwei Xing, Xinyu Sun, Andrei Cramariuc, Samuel Gull, Jen Jen Chung, Cesar
  Cadena, Roland Siegwart, Florian Tschopp
conference: Arxiv
year: 2022
bibkey: xing2022descriptellation
citations: 0
additional_links: [{name: Code, url: 'https://github.com/ethz-asl/Descriptellation'},
  {name: Paper, url: 'https://arxiv.org/abs/2203.00567'}]
tags: []
short_authors: Xing et al.
---
Current descriptors for global localization often struggle under vast
viewpoint or appearance changes. One possible improvement is the addition of
topological information on semantic objects. However, handcrafted topological
descriptors are hard to tune and not robust to environmental noise, drastic
perspective changes, object occlusion or misdetections. To solve this problem,
we formulate a learning-based approach by modelling semantically meaningful
object constellations as graphs and using Deep Graph Convolution Networks to
map a constellation to a descriptor. We demonstrate the effectiveness of our
Deep Learned Constellation Descriptor (Descriptellation) on two real-world
datasets. Although Descriptellation is trained on randomly generated simulation
datasets, it shows good generalization abilities on real-world datasets.
Descriptellation also outperforms state-of-the-art and handcrafted
constellation descriptors for global localization, and is robust to different
types of noise. The code is publicly available at
https://github.com/ethz-asl/Descriptellation.