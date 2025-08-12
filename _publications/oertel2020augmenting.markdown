---
layout: publication
title: Augmenting Visual Place Recognition With Structural Cues
authors: Amadeus Oertel, Titus Cieslewski, Davide Scaramuzza
conference: IEEE Robotics and Automation Letters
year: 2020
bibkey: oertel2020augmenting
citations: 35
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.00278'}]
tags: []
short_authors: Amadeus Oertel, Titus Cieslewski, Davide Scaramuzza
---
In this paper, we propose to augment image-based place recognition with
structural cues. Specifically, these structural cues are obtained using
structure-from-motion, such that no additional sensors are needed for place
recognition. This is achieved by augmenting the 2D convolutional neural network
(CNN) typically used for image-based place recognition with a 3D CNN that takes
as input a voxel grid derived from the structure-from-motion point cloud. We
evaluate different methods for fusing the 2D and 3D features and obtain best
performance with global average pooling and simple concatenation. On the Oxford
RobotCar dataset, the resulting descriptor exhibits superior recognition
performance compared to descriptors extracted from only one of the input
modalities, including state-of-the-art image-based descriptors. Especially at
low descriptor dimensionalities, we outperform state-of-the-art descriptors by
up to 90%.