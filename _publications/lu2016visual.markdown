---
layout: publication
title: Visual Relationship Detection With Language Priors
authors: Cewu Lu, Ranjay Krishna, Michael Bernstein, Li Fei-fei
conference: Lecture Notes in Computer Science
year: 2016
bibkey: lu2016visual
citations: 994
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1608.00187'}]
tags: ["Image Retrieval"]
short_authors: Lu et al.
---
Visual relationships capture a wide variety of interactions between pairs of
objects in images (e.g. "man riding bicycle" and "man pushing bicycle").
Consequently, the set of possible relationships is extremely large and it is
difficult to obtain sufficient training examples for all possible
relationships. Because of this limitation, previous work on visual relationship
detection has concentrated on predicting only a handful of relationships.
Though most relationships are infrequent, their objects (e.g. "man" and
"bicycle") and predicates (e.g. "riding" and "pushing") independently occur
more frequently. We propose a model that uses this insight to train visual
models for objects and predicates individually and later combines them together
to predict multiple relationships per image. We improve on prior work by
leveraging language priors from semantic word embeddings to finetune the
likelihood of a predicted relationship. Our model can scale to predict
thousands of types of relationships from a few examples. Additionally, we
localize the objects in the predicted relationships as bounding boxes in the
image. We further demonstrate that understanding relationships can improve
content based image retrieval.