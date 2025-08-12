---
layout: publication
title: Dataset Enhancement With Instance-level Augmentations
authors: Orest Kupyn, Christian Rupprecht
conference: Lecture Notes in Computer Science
year: 2024
bibkey: kupyn2024dataset
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.08249'}]
tags: ["Datasets"]
short_authors: Orest Kupyn, Christian Rupprecht
---
We present a method for expanding a dataset by incorporating knowledge from
the wide distribution of pre-trained latent diffusion models. Data
augmentations typically incorporate inductive biases about the image formation
process into the training (e.g. translation, scaling, colour changes, etc.).
Here, we go beyond simple pixel transformations and introduce the concept of
instance-level data augmentation by repainting parts of the image at the level
of object instances. The method combines a conditional diffusion model with
depth and edge maps control conditioning to seamlessly repaint individual
objects inside the scene, being applicable to any segmentation or detection
dataset. Used as a data augmentation method, it improves the performance and
generalization of the state-of-the-art salient object detection, semantic
segmentation and object detection models. By redrawing all privacy-sensitive
instances (people, license plates, etc.), the method is also applicable for
data anonymization. We also release fully synthetic and anonymized expansions
for popular datasets: COCO, Pascal VOC and DUTS.