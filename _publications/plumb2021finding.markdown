---
layout: publication
title: Finding And Fixing Spurious Patterns With Explanations
authors: Gregory Plumb, Marco Tulio Ribeiro, Ameet Talwalkar
conference: Arxiv
year: 2021
bibkey: plumb2021finding
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.02112'}]
tags: []
short_authors: Gregory Plumb, Marco Tulio Ribeiro, Ameet Talwalkar
---
Image classifiers often use spurious patterns, such as "relying on the
presence of a person to detect a tennis racket, which do not generalize. In
this work, we present an end-to-end pipeline for identifying and mitigating
spurious patterns for such models, under the assumption that we have access to
pixel-wise object-annotations. We start by identifying patterns such as "the
model's prediction for tennis racket changes 63% of the time if we hide the
people." Then, if a pattern is spurious, we mitigate it via a novel form of
data augmentation. We demonstrate that our method identifies a diverse set of
spurious patterns and that it mitigates them by producing a model that is both
more accurate on a distribution where the spurious pattern is not helpful and
more robust to distribution shift.