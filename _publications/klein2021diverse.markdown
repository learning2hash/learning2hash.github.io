---
layout: publication
title: Diverse Image Captioning With Grounded Style
authors: Franz Klein, Shweta Mahajan, Stefan Roth
conference: Lecture Notes in Computer Science
year: 2021
bibkey: klein2021diverse
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.01813'}]
tags: ["Datasets"]
short_authors: Franz Klein, Shweta Mahajan, Stefan Roth
---
Stylized image captioning as presented in prior work aims to generate
captions that reflect characteristics beyond a factual description of the scene
composition, such as sentiments. Such prior work relies on given sentiment
identifiers, which are used to express a certain global style in the caption,
e.g. positive or negative, however without taking into account the stylistic
content of the visual scene. To address this shortcoming, we first analyze the
limitations of current stylized captioning datasets and propose COCO
attribute-based augmentations to obtain varied stylized captions from COCO
annotations. Furthermore, we encode the stylized information in the latent
space of a Variational Autoencoder; specifically, we leverage extracted image
attributes to explicitly structure its sequential latent space according to
different localized style characteristics. Our experiments on the Senticap and
COCO datasets show the ability of our approach to generate accurate captions
with diversity in styles that are grounded in the image.