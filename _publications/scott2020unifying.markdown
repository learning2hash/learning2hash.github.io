---
layout: publication
title: Unifying Few- And Zero-shot Egocentric Action Recognition
authors: Tyler R. Scott, Michael Shvartsman, Karl Ridgeway
conference: Arxiv
year: 2020
bibkey: scott2020unifying
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.11393'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Tyler R. Scott, Michael Shvartsman, Karl Ridgeway
---
Although there has been significant research in egocentric action
recognition, most methods and tasks, including EPIC-KITCHENS, suppose a fixed
set of action classes. Fixed-set classification is useful for benchmarking
methods, but is often unrealistic in practical settings due to the
compositionality of actions, resulting in a functionally infinite-cardinality
label set. In this work, we explore generalization with an open set of classes
by unifying two popular approaches: few- and zero-shot generalization (the
latter which we reframe as cross-modal few-shot generalization). We propose a
new set of splits derived from the EPIC-KITCHENS dataset that allow evaluation
of open-set classification, and use these splits to show that adding a
metric-learning loss to the conventional direct-alignment baseline can improve
zero-shot classification by as much as 10%, while not sacrificing few-shot
performance.