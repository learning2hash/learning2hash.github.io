---
layout: publication
title: Dominating Set Database Selection For Visual Place Recognition
authors: Anastasiia Kornilova, Ivan Moskalenko, Timofei Pushkin, Fakhriddin Tojiboev,
  Rahim Tariverdizadeh, Gonzalo Ferrer
conference: 2023 21st International Conference on Advanced Robotics (ICAR) Abu Dhabi
  United Arab Emirates 2023 pp. 473-479
year: 2023
bibkey: kornilova2023dominating
citations: 0
additional_links: [{name: Code, url: 'https://prime-slam.github.io/place-recognition-db/'},
  {name: Paper, url: 'https://arxiv.org/abs/2303.05123'}]
tags: []
short_authors: Kornilova et al.
---
This paper presents an approach for creating a visual place recognition (VPR)
database for localization in indoor environments from RGBD scanning sequences.
The proposed approach is formulated as a minimization problem in terms of
dominating set algorithm for graph, constructed from spatial information, and
referred as DominatingSet. Our algorithm shows better scene coverage in
comparison to other methodologies that are used for database creation. Also, we
demonstrate that using DominatingSet, a database size could be up to 250-1400
times smaller than the original scanning sequence while maintaining a recall
rate of more than 80% on testing sequences. We evaluated our algorithm on
7-scenes and BundleFusion datasets and an additionally recorded sequence in a
highly repetitive office setting. In addition, the database selection can
produce weakly-supervised labels for fine-tuning neural place recognition
algorithms to particular settings, improving even more their accuracy. The
paper also presents a fully automated pipeline for VPR database creation from
RGBD scanning sequences, as well as a set of metrics for VPR database
evaluation. The code and released data are available on our web-page~ --
https://prime-slam.github.io/place-recognition-db/