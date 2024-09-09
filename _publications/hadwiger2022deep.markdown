---
layout: publication
title: Deep Metric Color Embeddings for Splicing Localization in Severely Degraded Images
authors: Hadwiger Benjamin, Riess Christian
conference: "Arxiv"
year: 2022
bibkey: hadwiger2022deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2206.10737"}
tags: ['ARXIV', 'TIP']
---
One common task in image forensics is to detect spliced images, where multiple source images are composed to one output image. Most of the currently best performing splicing detectors leverage high-frequency artifacts. However, after an image underwent strong compression, most of the high frequency artifacts are not available anymore. In this work, we explore an alternative approach to splicing detection, which is potentially better suited for images in-the-wild, subject to strong compression and downsampling. Our proposal is to model the color formation of an image. The color formation largely depends on variations at the scale of scene objects, and is hence much less dependent on high-frequency artifacts. We learn a deep metric space that is on one hand sensitive to illumination color and camera white-point estimation, but on the other hand insensitive to variations in object color. Large distances in the embedding space indicate that two image regions either stem from different scenes or different cameras. In our evaluation, we show that the proposed embedding space outperforms the state of the art on images that have been subject to strong compression and downsampling. We confirm in two further experiments the dual nature of the metric space, namely to both characterize the acquisition camera and the scene illuminant color. As such, this work resides at the intersection of physics-based and statistical forensics with benefits from both sides.
