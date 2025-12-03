---
layout: publication
title: 'Globetrotter: Connecting Languages By Connecting Images'
authors: "D\xEDdac Sur\xEDs, Dave Epstein, Carl Vondrick"
conference: Arxiv
year: 2020
bibkey: "sur\xEDs2020globetrotter"
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.04631'}]
tags: ["Datasets", "Supervised", "Unsupervised"]
short_authors: "D\xEDdac Sur\xEDs, Dave Epstein, Carl Vondrick"
---
Machine translation between many languages at once is highly challenging,
since training with ground truth requires supervision between all language
pairs, which is difficult to obtain. Our key insight is that, while languages
may vary drastically, the underlying visual appearance of the world remains
consistent. We introduce a method that uses visual observations to bridge the
gap between languages, rather than relying on parallel corpora or topological
properties of the representations. We train a model that aligns segments of
text from different languages if and only if the images associated with them
are similar and each image in turn is well-aligned with its textual
description. We train our model from scratch on a new dataset of text in over
fifty languages with accompanying images. Experiments show that our method
outperforms previous work on unsupervised word and sentence translation using
retrieval. Code, models and data are available on globetrotter.cs.columbia.edu.