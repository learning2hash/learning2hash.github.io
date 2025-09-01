---
layout: publication
title: 'Gsv-cities: Toward Appropriate Supervised Visual Place Recognition'
authors: "Amar Ali-Bey, Brahim Chaib-Draa, Philippe Gigu\xE8re"
conference: Neurocomputing
year: 2022
bibkey: alibey2022gsv
citations: 59
additional_links: [{name: Code, url: 'https://github.com/amaralibey/gsv-cities.'},
  {name: Paper, url: 'https://arxiv.org/abs/2210.10239'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Scalability", "Supervised"]
short_authors: "Amar Ali-Bey, Brahim Chaib-Draa, Philippe Gigu\xE8re"
---
This paper aims to investigate representation learning for large scale visual
place recognition, which consists of determining the location depicted in a
query image by referring to a database of reference images. This is a
challenging task due to the large-scale environmental changes that can occur
over time (i.e., weather, illumination, season, traffic, occlusion). Progress
is currently challenged by the lack of large databases with accurate ground
truth. To address this challenge, we introduce GSV-Cities, a new image dataset
providing the widest geographic coverage to date with highly accurate ground
truth, covering more than 40 cities across all continents over a 14-year
period. We subsequently explore the full potential of recent advances in deep
metric learning to train networks specifically for place recognition, and
evaluate how different loss functions influence performance. In addition, we
show that performance of existing methods substantially improves when trained
on GSV-Cities. Finally, we introduce a new fully convolutional aggregation
layer that outperforms existing techniques, including GeM, NetVLAD and
CosPlace, and establish a new state-of-the-art on large-scale benchmarks, such
as Pittsburgh, Mapillary-SLS, SPED and Nordland. The dataset and code are
available for research purposes at https://github.com/amaralibey/gsv-cities.