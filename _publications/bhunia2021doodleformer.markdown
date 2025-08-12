---
layout: publication
title: 'Doodleformer: Creative Sketch Drawing With Transformers'
authors: Ankan Kumar Bhunia, Salman Khan, Hisham Cholakkal, Rao Muhammad Anwer, Fahad
  Shahbaz Khan, Jorma Laaksonen, Michael Felsberg
conference: Lecture Notes in Computer Science
year: 2022
bibkey: bhunia2021doodleformer
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.03258'}]
tags: []
short_authors: Bhunia et al.
---
Creative sketching or doodling is an expressive activity, where imaginative
and previously unseen depictions of everyday visual objects are drawn. Creative
sketch image generation is a challenging vision problem, where the task is to
generate diverse, yet realistic creative sketches possessing the unseen
composition of the visual-world objects. Here, we propose a novel
coarse-to-fine two-stage framework, DoodleFormer, that decomposes the creative
sketch generation problem into the creation of coarse sketch composition
followed by the incorporation of fine-details in the sketch. We introduce
graph-aware transformer encoders that effectively capture global dynamic as
well as local static structural relations among different body parts. To ensure
diversity of the generated creative sketches, we introduce a probabilistic
coarse sketch decoder that explicitly models the variations of each sketch body
part to be drawn. Experiments are performed on two creative sketch datasets:
Creative Birds and Creative Creatures. Our qualitative, quantitative and
human-based evaluations show that DoodleFormer outperforms the state-of-the-art
on both datasets, yielding realistic and diverse creative sketches. On Creative
Creatures, DoodleFormer achieves an absolute gain of 25 in terms of Fr`echet
inception distance (FID) over the state-of-the-art. We also demonstrate the
effectiveness of DoodleFormer for related applications of text to creative
sketch generation and sketch completion.