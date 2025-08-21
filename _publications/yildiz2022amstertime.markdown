---
layout: publication
title: 'Amstertime: A Visual Place Recognition Benchmark Dataset For Severe Domain
  Shift'
authors: Burak Yildiz, Seyran Khademi, Ronald Maria Siebes, Jan van Gemert
conference: 2022 26th International Conference on Pattern Recognition (ICPR)
year: 2022
bibkey: yildiz2022amstertime
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.16291'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Self-Supervised", "Supervised"]
short_authors: Yildiz et al.
---
We introduce AmsterTime: a challenging dataset to benchmark visual place
recognition (VPR) in presence of a severe domain shift. AmsterTime offers a
collection of 2,500 well-curated images matching the same scene from a street
view matched to historical archival image data from Amsterdam city. The image
pairs capture the same place with different cameras, viewpoints, and
appearances. Unlike existing benchmark datasets, AmsterTime is directly
crowdsourced in a GIS navigation platform (Mapillary). We evaluate various
baselines, including non-learning, supervised and self-supervised methods,
pre-trained on different relevant datasets, for both verification and retrieval
tasks. Our result credits the best accuracy to the ResNet-101 model pre-trained
on the Landmarks dataset for both verification and retrieval tasks by 84% and
24%, respectively. Additionally, a subset of Amsterdam landmarks is collected
for feature evaluation in a classification task. Classification labels are
further used to extract the visual explanations using Grad-CAM for inspection
of the learned similar visuals in a deep metric learning models.