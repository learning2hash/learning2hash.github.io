---
layout: publication
title: 'ELFIS: Expert Learning For Fine-grained Image Recognition Using Subsets'
authors: "Pablo Villacorta, Jes\xFAs M. Rodr\xEDguez-de-Vera, Marc Bola\xF1os, Ignacio\
  \ Saras\xFAa, Bhalaji Nagarajan, Petia Radeva"
conference: Arxiv
year: 2023
bibkey: villacorta2023elfis
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.09269'}]
tags: []
short_authors: Villacorta et al.
---
Fine-Grained Visual Recognition (FGVR) tackles the problem of distinguishing
highly similar categories. One of the main approaches to FGVR, namely subset
learning, tries to leverage information from existing class taxonomies to
improve the performance of deep neural networks. However, these methods rely on
the existence of handcrafted hierarchies that are not necessarily optimal for
the models. In this paper, we propose ELFIS, an expert learning framework for
FGVR that clusters categories of the dataset into meta-categories using both
dataset-inherent lexical and model-specific information. A set of neural
networks-based experts are trained focusing on the meta-categories and are
integrated into a multi-task framework. Extensive experimentation shows
improvements in the SoTA FGVR benchmarks of up to +1.3% of accuracy using both
CNNs and transformer-based networks. Overall, the obtained results evidence
that ELFIS can be applied on top of any classification model, enabling the
obtention of SoTA results. The source code will be made public soon.