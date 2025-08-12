---
layout: publication
title: Online Invariance Selection For Local Feature Descriptors
authors: "R\xE9mi Pautrat, Viktor Larsson, Martin R. Oswald, Marc Pollefeys"
conference: Lecture Notes in Computer Science
year: 2020
bibkey: pautrat2020online
citations: 71
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.08988'}]
tags: []
short_authors: Pautrat et al.
---
To be invariant, or not to be invariant: that is the question formulated in
this work about local descriptors. A limitation of current feature descriptors
is the trade-off between generalization and discriminative power: more
invariance means less informative descriptors. We propose to overcome this
limitation with a disentanglement of invariance in local descriptors and with
an online selection of the most appropriate invariance given the context. Our
framework consists in a joint learning of multiple local descriptors with
different levels of invariance and of meta descriptors encoding the regional
variations of an image. The similarity of these meta descriptors across images
is used to select the right invariance when matching the local descriptors. Our
approach, named Local Invariance Selection at Runtime for Descriptors (LISRD),
enables descriptors to adapt to adverse changes in images, while remaining
discriminative when invariance is not required. We demonstrate that our method
can boost the performance of current descriptors and outperforms
state-of-the-art descriptors in several matching tasks, when evaluated on
challenging datasets with day-night illumination as well as viewpoint changes.