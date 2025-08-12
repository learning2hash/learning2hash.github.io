---
layout: publication
title: 'Deep Manifold Traversal: Changing Labels With Convolutional Features'
authors: Jacob R. Gardner, Paul Upchurch, Matt J. Kusner, Yixuan Li, Kilian Q. Weinberger,
  Kavita Bala, John E. Hopcroft
conference: Arxiv
year: 2015
bibkey: gardner2015deep
citations: 48
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.06421'}]
tags: []
short_authors: Gardner et al.
---
Many tasks in computer vision can be cast as a "label changing" problem,
where the goal is to make a semantic change to the appearance of an image or
some subject in an image in order to alter the class membership. Although
successful task-specific methods have been developed for some label changing
applications, to date no general purpose method exists. Motivated by this we
propose deep manifold traversal, a method that addresses the problem in its
most general form: it first approximates the manifold of natural images then
morphs a test image along a traversal path away from a source class and towards
a target class while staying near the manifold throughout. The resulting
algorithm is surprisingly effective and versatile. It is completely data
driven, requiring only an example set of images from the desired source and
target domains. We demonstrate deep manifold traversal on highly diverse label
changing tasks: changing an individual's appearance (age and hair color),
changing the season of an outdoor image, and transforming a city skyline
towards nighttime.