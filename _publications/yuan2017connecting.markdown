---
layout: publication
title: 'Connecting Look And Feel: Associating The Visual And Tactile Properties Of
  Physical Materials'
authors: Wenzhen Yuan, Shaoxiong Wang, Siyuan Dong, Edward Adelson
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: yuan2017connecting
citations: 104
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.03822'}]
tags: ["CVPR"]
short_authors: Yuan et al.
---
For machines to interact with the physical world, they must understand the
physical properties of objects and materials they encounter. We use fabrics as
an example of a deformable material with a rich set of mechanical properties. A
thin flexible fabric, when draped, tends to look different from a heavy stiff
fabric. It also feels different when touched. Using a collection of 118 fabric
sample, we captured color and depth images of draped fabrics along with tactile
data from a high resolution touch sensor. We then sought to associate the
information from vision and touch by jointly training CNNs across the three
modalities. Through the CNN, each input, regardless of the modality, generates
an embedding vector that records the fabric's physical property. By comparing
the embeddings, our system is able to look at a fabric image and predict how it
will feel, and vice versa. We also show that a system jointly trained on vision
and touch data can outperform a similar system trained only on visual data when
tested purely with visual inputs.