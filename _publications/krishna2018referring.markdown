---
layout: publication
title: Referring Relationships
authors: Ranjay Krishna, Ines Chami, Michael Bernstein, Li Fei-Fei
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: krishna2018referring
citations: 93
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.10362'}]
tags: ["CVPR"]
short_authors: Krishna et al.
---
Images are not simply sets of objects: each image represents a web of
interconnected relationships. These relationships between entities carry
semantic meaning and help a viewer differentiate between instances of an
entity. For example, in an image of a soccer match, there may be multiple
persons present, but each participates in different relationships: one is
kicking the ball, and the other is guarding the goal. In this paper, we
formulate the task of utilizing these "referring relationships" to disambiguate
between entities of the same category. We introduce an iterative model that
localizes the two entities in the referring relationship, conditioned on one
another. We formulate the cyclic condition between the entities in a
relationship by modelling predicates that connect the entities as shifts in
attention from one entity to another. We demonstrate that our model can not
only outperform existing approaches on three datasets --- CLEVR, VRD and Visual
Genome --- but also that it produces visually meaningful predicate shifts, as
an instance of interpretable neural networks. Finally, we show that by
modelling predicates as attention shifts, we can even localize entities in the
absence of their category, allowing our model to find completely unseen
categories.