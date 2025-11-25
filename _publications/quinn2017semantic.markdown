---
layout: publication
title: Semantic Image Retrieval Via Active Grounding Of Visual Situations
authors: Max H. Quinn, Erik Conser, Jordan M. Witte, Melanie Mitchell
conference: 2018 IEEE 12th International Conference on Semantic Computing (ICSC)
year: 2017
bibkey: quinn2017semantic
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.00088'}]
tags: ["Evaluation", "Image Retrieval"]
short_authors: Quinn et al.
---
We describe a novel architecture for semantic image retrieval---in
particular, retrieval of instances of visual situations. Visual situations are
concepts such as "a boxing match," "walking the dog," "a crowd waiting for a
bus," or "a game of ping-pong," whose instantiations in images are linked more
by their common spatial and semantic structure than by low-level visual
similarity. Given a query situation description, our architecture---called
Situate---learns models capturing the visual features of expected objects as
well the expected spatial configuration of relationships among objects. Given a
new image, Situate uses these models in an attempt to ground (i.e., to create a
bounding box locating) each expected component of the situation in the image
via an active search procedure. Situate uses the resulting grounding to compute
a score indicating the degree to which the new image is judged to contain an
instance of the situation. Such scores can be used to rank images in a
collection as part of a retrieval system. In the preliminary study described
here, we demonstrate the promise of this system by comparing Situate's
performance with that of two baseline methods, as well as with a related
semantic image-retrieval system based on "scene graphs."