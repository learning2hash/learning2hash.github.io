---
layout: publication
title: Multiregion Bilinear Convolutional Neural Networks For Person Re-identification
authors: Evgeniya Ustinova, Yaroslav Ganin, Victor Lempitsky
conference: Arxiv
year: 2015
bibkey: ustinova2015multiregion
citations: 36
additional_links: [{name: Code, url: 'https://github.com/madkn/MultiregionBilinearCNN-ReId'},
  {name: Paper, url: 'https://arxiv.org/abs/1512.05300'}]
tags: ["Datasets", "Evaluation"]
short_authors: Evgeniya Ustinova, Yaroslav Ganin, Victor Lempitsky
---
In this work we propose a new architecture for person re-identification. As
the task of re-identification is inherently associated with embedding learning
and non-rigid appearance description, our architecture is based on the deep
bilinear convolutional network (Bilinear-CNN) that has been proposed recently
for fine-grained classification of highly non-rigid objects. While the last
stages of the original Bilinear-CNN architecture completely removes the
geometric information from consideration by performing orderless pooling, we
observe that a better embedding can be learned by performing bilinear pooling
in a more local way, where each pooling is confined to a predefined region. Our
architecture thus represents a compromise between traditional convolutional
networks and bilinear CNNs and strikes a balance between rigid matching and
completely ignoring spatial information.
  We perform the experimental validation of the new architecture on the three
popular benchmark datasets (Market-1501, CUHK01, CUHK03), comparing it to
baselines that include Bilinear-CNN as well as prior art. The new architecture
outperforms the baseline on all three datasets, while performing better than
state-of-the-art on two out of three. The code and the pretrained models of the
approach can be found at https://github.com/madkn/MultiregionBilinearCNN-ReId.