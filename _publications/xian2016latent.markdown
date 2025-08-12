---
layout: publication
title: Latent Embeddings For Zero-shot Classification
authors: Yongqin Xian, Zeynep Akata, Gaurav Sharma, Quynh Nguyen, Matthias Hein, Bernt
  Schiele
conference: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2016
bibkey: xian2016latent
citations: 673
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.08895'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Xian et al.
---
We present a novel latent embedding model for learning a compatibility
function between image and class embeddings, in the context of zero-shot
classification. The proposed method augments the state-of-the-art bilinear
compatibility model by incorporating latent variables. Instead of learning a
single bilinear map, it learns a collection of maps with the selection, of
which map to use, being a latent variable for the current image-class pair. We
train the model with a ranking based objective function which penalizes
incorrect rankings of the true class for a given image. We empirically
demonstrate that our model improves the state-of-the-art for various class
embeddings consistently on three challenging publicly available datasets for
the zero-shot setting. Moreover, our method leads to visually highly
interpretable results with clear clusters of different fine-grained object
properties that correspond to different latent variable maps.