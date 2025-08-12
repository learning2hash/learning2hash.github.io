---
layout: publication
title: Sample-efficient Learning Of Novel Visual Concepts
authors: Sarthak Bhagat, Simon Stepputtis, Joseph Campbell, Katia Sycara
conference: Arxiv
year: 2023
bibkey: bhagat2023sample
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.09482'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Bhagat et al.
---
Despite the advances made in visual object recognition, state-of-the-art deep
learning models struggle to effectively recognize novel objects in a few-shot
setting where only a limited number of examples are provided. Unlike humans who
excel at such tasks, these models often fail to leverage known relationships
between entities in order to draw conclusions about such objects. In this work,
we show that incorporating a symbolic knowledge graph into a state-of-the-art
recognition model enables a new approach for effective few-shot classification.
In our proposed neuro-symbolic architecture and training methodology, the
knowledge graph is augmented with additional relationships extracted from a
small set of examples, improving its ability to recognize novel objects by
considering the presence of interconnected entities. Unlike existing few-shot
classifiers, we show that this enables our model to incorporate not only
objects but also abstract concepts and affordances. The existence of the
knowledge graph also makes this approach amenable to interpretability through
analysis of the relationships contained within it. We empirically show that our
approach outperforms current state-of-the-art few-shot multi-label
classification methods on the COCO dataset and evaluate the addition of
abstract concepts and affordances on the Visual Genome dataset.