---
layout: publication
title: 'Geodabs: Trajectory Indexing Meets Fingerprinting At Scale'
authors: Bertil Chapuis, Benoit Garbinato
conference: 2018 IEEE 38th International Conference on Distributed Computing Systems
  (ICDCS)
year: 2018
bibkey: chapuis2018geodabs
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.04292'}]
tags: []
short_authors: Bertil Chapuis, Benoit Garbinato
---
Finding trajectories and discovering motifs that are similar in large
datasets is a central problem for a wide range of applications. Solutions
addressing this problem usually rely on spatial indexing and on the computation
of a similarity measure in polynomial time. Although effective in the context
of sparse trajectory datasets, this approach is too expensive in the context of
dense datasets, where many trajectories potentially match with a given query.
In this paper, we apply fingerprinting, a copy-detection mechanism used in the
context of textual data, to trajectories. To this end, we fingerprint
trajectories with geodabs, a construction based on geohash aimed at trajectory
fingerprinting. We demonstrate that by relying on the properties of a space
filling curve geodabs can be used to build sharded inverted indexes. We show
how normalization affects precision and recall, two key measures in information
retrieval. We then demonstrate that the probabilistic nature of fingerprinting
has a marginal effect on the quality of the results. Finally, we evaluate our
method in terms of performances and show that, in contrast with existing
methods, it is not affected by the density of the trajectory dataset and that
it can be efficiently distributed.