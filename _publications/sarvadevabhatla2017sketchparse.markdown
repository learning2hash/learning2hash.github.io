---
layout: publication
title: 'Sketchparse : Towards Rich Descriptions For Poorly Drawn Sketches Using Multi-task
  Hierarchical Deep Networks'
authors: Ravi Kiran Sarvadevabhatla, Isht Dwivedi, Abhijat Biswas, Sahil Manocha,
  R. Venkatesh Babu
conference: Arxiv
year: 2017
bibkey: sarvadevabhatla2017sketchparse
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.01295'}]
tags: [Scalability, Evaluation, Image Retrieval, Datasets]
short_authors: Sarvadevabhatla et al.
---
The ability to semantically interpret hand-drawn line sketches, although very
challenging, can pave way for novel applications in multimedia. We propose
SketchParse, the first deep-network architecture for fully automatic parsing of
freehand object sketches. SketchParse is configured as a two-level fully
convolutional network. The first level contains shared layers common to all
object categories. The second level contains a number of expert sub-networks.
Each expert specializes in parsing sketches from object categories which
contain structurally similar parts. Effectively, the two-level configuration
enables our architecture to scale up efficiently as additional categories are
added. We introduce a router layer which (i) relays sketch features from shared
layers to the correct expert (ii) eliminates the need to manually specify
object category during inference. To bypass laborious part-level annotation, we
sketchify photos from semantic object-part image datasets and use them for
training. Our architecture also incorporates object pose prediction as a novel
auxiliary task which boosts overall performance while providing supplementary
information regarding the sketch. We demonstrate SketchParse's abilities (i) on
two challenging large-scale sketch datasets (ii) in parsing unseen,
semantically related object categories (iii) in improving fine-grained
sketch-based image retrieval. As a novel application, we also outline how
SketchParse's output can be used to generate caption-style descriptions for
hand-drawn sketches.