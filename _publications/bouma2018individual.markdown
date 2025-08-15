---
layout: publication
title: Individual Common Dolphin Identification Via Metric Embedding Learning
authors: Soren Bouma, Matthew D. M. Pawley, Krista Hupman, Andrew Gilman
conference: 2018 International Conference on Image and Vision Computing New Zealand
  (IVCNZ)
year: 2018
bibkey: bouma2018individual
citations: 36
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.03662'}]
tags: ["Distance Metric Learning"]
short_authors: Bouma et al.
---
Photo-identification (photo-id) of dolphin individuals is a commonly used
technique in ecological sciences to monitor state and health of individuals, as
well as to study the social structure and distribution of a population.
Traditional photo-id involves a laborious manual process of matching each
dolphin fin photograph captured in the field to a catalogue of known
individuals.
  We examine this problem in the context of open-set recognition and utilise a
triplet loss function to learn a compact representation of fin images in a
Euclidean embedding, where the Euclidean distance metric represents fin
similarity. We show that this compact representation can be successfully learnt
from a fairly small (in deep learning context) training set and still
generalise well to out-of-sample identities (completely new dolphin
individuals), with top-1 and top-5 test set (37 individuals) accuracy of
\(90.5\pm2\) and \(93.6\pm1\) percent. In the presence of 1200 distractors, top-1
accuracy dropped by \(12%\); however, top-5 accuracy saw only a \(2.8%\) drop