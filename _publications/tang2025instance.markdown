---
layout: publication
title: Instance Segmentation Of Scene Sketches Using Natural Image Priors
authors: Mia Tang, Yael Vinker, Chuan Yan, Lvmin Zhang, Maneesh Agrawala
conference: Arxiv
year: 2025
bibkey: tang2025instance
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.09608'}]
tags: ["Robustness"]
short_authors: Tang et al.
---
Sketch segmentation involves grouping pixels within a sketch that belong to
the same object or instance. It serves as a valuable tool for sketch editing
tasks, such as moving, scaling, or removing specific components. While image
segmentation models have demonstrated remarkable capabilities in recent years,
sketches present unique challenges for these models due to their sparse nature
and wide variation in styles. We introduce InkLayer, a method for instance
segmentation of raster scene sketches. Our approach adapts state-of-the-art
image segmentation and object detection models to the sketch domain by
employing class-agnostic fine-tuning and refining segmentation masks using
depth cues. Furthermore, our method organizes sketches into sorted layers,
where occluded instances are inpainted, enabling advanced sketch editing
applications. As existing datasets in this domain lack variation in sketch
styles, we construct a synthetic scene sketch segmentation dataset, InkScenes,
featuring sketches with diverse brush strokes and varying levels of detail. We
use this dataset to demonstrate the robustness of our approach.