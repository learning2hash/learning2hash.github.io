---
layout: publication
title: Learning Semantics For Image Annotation
authors: Amara Tariq, Hassan Foroosh
conference: Arxiv
year: 2017
bibkey: tariq2017learning
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.05102'}]
tags: ["Image Retrieval"]
short_authors: Amara Tariq, Hassan Foroosh
---
Image search and retrieval engines rely heavily on textual annotation in
order to match word queries to a set of candidate images. A system that can
automatically annotate images with meaningful text can be highly beneficial for
such engines. Currently, the approaches to develop such systems try to
establish relationships between keywords and visual features of images. In this
paper, We make three main contributions to this area: (i) We transform this
problem from the low-level keyword space to the high-level semantics space that
we refer to as the "\{\em image theme\}", (ii) Instead of treating each possible
keyword independently, we use latent Dirichlet allocation to learn image themes
from the associated texts in a training phase. Images are then annotated with
image themes rather than keywords, using a modified continuous relevance model,
which takes into account the spatial coherence and the visual continuity among
images of common theme. (iii) To achieve more coherent annotations among images
of common theme, we have integrated ConceptNet in learning the semantics of
images, and hence augment image descriptions beyond annotations provided by
humans. Images are thus further annotated by a few most significant words of
the prominent image theme. Our extensive experiments show that a coherent
theme-based image annotation using high-level semantics results in improved
precision and recall as compared with equivalent classical keyword annotation
systems.