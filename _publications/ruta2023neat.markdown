---
layout: publication
title: 'Neat: Neural Artistic Tracing For Beautiful Style Transfer'
authors: Dan Ruta, Andrew Gilbert, John Collomosse, Eli Shechtman, Nicholas Kolkin
conference: Arxiv
year: 2023
bibkey: ruta2023neat
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.05139'}]
tags: []
short_authors: Ruta et al.
---
Style transfer is the task of reproducing the semantic contents of a source
image in the artistic style of a second target image. In this paper, we present
NeAT, a new state-of-the art feed-forward style transfer method. We
re-formulate feed-forward style transfer as image editing, rather than image
generation, resulting in a model which improves over the state-of-the-art in
both preserving the source content and matching the target style. An important
component of our model's success is identifying and fixing "style halos", a
commonly occurring artefact across many style transfer techniques. In addition
to training and testing on standard datasets, we introduce the BBST-4M dataset,
a new, large scale, high resolution dataset of 4M images. As a component of
curating this data, we present a novel model able to classify if an image is
stylistic. We use BBST-4M to improve and measure the generalization of NeAT
across a huge variety of styles. Not only does NeAT offer state-of-the-art
quality and generalization, it is designed and trained for fast inference at
high resolution.