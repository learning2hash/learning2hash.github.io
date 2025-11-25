---
layout: publication
title: 'Mask2cad: 3D Shape Prediction By Learning To Segment And Retrieve'
authors: Weicheng Kuo, Anelia Angelova, Tsung-Yi Lin, Angela Dai
conference: Lecture Notes in Computer Science
year: 2020
bibkey: kuo2020mask2cad
citations: 57
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.13034'}]
tags: ["Datasets"]
short_authors: Kuo et al.
---
Object recognition has seen significant progress in the image domain, with
focus primarily on 2D perception. We propose to leverage existing large-scale
datasets of 3D models to understand the underlying 3D structure of objects seen
in an image by constructing a CAD-based representation of the objects and their
poses. We present Mask2CAD, which jointly detects objects in real-world images
and for each detected object, optimizes for the most similar CAD model and its
pose. We construct a joint embedding space between the detected regions of an
image corresponding to an object and 3D CAD models, enabling retrieval of CAD
models for an input RGB image. This produces a clean, lightweight
representation of the objects in an image; this CAD-based representation
ensures a valid, efficient shape representation for applications such as
content creation or interactive scenarios, and makes a step towards
understanding the transformation of real-world imagery to a synthetic domain.
Experiments on real-world images from Pix3D demonstrate the advantage of our
approach in comparison to state of the art. To facilitate future research, we
additionally propose a new image-to-3D baseline on ScanNet which features
larger shape diversity, real-world occlusions, and challenging image views.