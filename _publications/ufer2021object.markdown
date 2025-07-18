---
layout: publication
title: Object Retrieval And Localization In Large Art Collections Using Deep Multi-style
  Feature Fusion And Iterative Voting
authors: "Ufer Nikolai, Lang Sabine, Ommer Bj\xF6rn"
conference: Lecture Notes in Computer Science
year: 2021
bibkey: ufer2021object
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.06935'}]
tags: [DATASETS]
---
The search for specific objects or motifs is essential to art history as both
assist in decoding the meaning of artworks. Digitization has produced large art
collections, but manual methods prove to be insufficient to analyze them. In
the following, we introduce an algorithm that allows users to search for image
regions containing specific motifs or objects and find similar regions in an
extensive dataset, helping art historians to analyze large digitized art
collections. Computer vision has presented efficient methods for visual
instance retrieval across photographs. However, applied to art collections,
they reveal severe deficiencies because of diverse motifs and massive domain
shifts induced by differences in techniques, materials, and styles. In this
paper, we present a multi-style feature fusion approach that successfully
reduces the domain gap and improves retrieval results without labelled data or
curated image collections. Our region-based voting with GPU-accelerated
approximate nearest-neighbour search allows us to find and localize even small
motifs within an extensive dataset in a few seconds. We obtain state-of-the-art
results on the Brueghel dataset and demonstrate its generalization to
inhomogeneous collections with a large number of distractors.