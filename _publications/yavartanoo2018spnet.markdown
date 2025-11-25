---
layout: publication
title: 'Spnet: Deep 3D Object Classification And Retrieval Using Stereographic Projection'
authors: Mohsen Yavartanoo, Eu Young Kim, Kyoung Mu Lee
conference: Lecture Notes in Computer Science
year: 2018
bibkey: yavartanoo2018spnet
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.01571'}]
tags: ["Evaluation", "Image Retrieval", "Memory Efficiency"]
short_authors: Mohsen Yavartanoo, Eu Young Kim, Kyoung Mu Lee
---
We propose an efficient Stereographic Projection Neural Network (SPNet) for
learning representations of 3D objects. We first transform a 3D input volume
into a 2D planar image using stereographic projection. We then present a
shallow 2D convolutional neural network (CNN) to estimate the object category
followed by view ensemble, which combines the responses from multiple views of
the object to further enhance the predictions. Specifically, the proposed
approach consists of four stages: (1) Stereographic projection of a 3D object,
(2) view-specific feature learning, (3) view selection and (4) view ensemble.
The proposed approach performs comparably to the state-of-the-art methods while
having substantially lower GPU memory as well as network parameters. Despite
its lightness, the experiments on 3D object classification and shape retrievals
demonstrate the high performance of the proposed method.