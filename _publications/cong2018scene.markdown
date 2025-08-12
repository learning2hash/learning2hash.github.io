---
layout: publication
title: Scene Graph Generation Via Conditional Random Fields
authors: Weilin Cong, William Wang, Wang-Chien Lee
conference: Arxiv
year: 2018
bibkey: cong2018scene
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.08075'}]
tags: []
short_authors: Weilin Cong, William Wang, Wang-Chien Lee
---
Despite the great success object detection and segmentation models have
achieved in recognizing individual objects in images, performance on cognitive
tasks such as image caption, semantic image retrieval, and visual QA is far
from satisfactory. To achieve better performance on these cognitive tasks,
merely recognizing individual object instances is insufficient. Instead, the
interactions between object instances need to be captured in order to
facilitate reasoning and understanding of the visual scenes in an image. Scene
graph, a graph representation of images that captures object instances and
their relationships, offers a comprehensive understanding of an image. However,
existing techniques on scene graph generation fail to distinguish subjects and
objects in the visual scenes of images and thus do not perform well with
real-world datasets where exist ambiguous object instances. In this work, we
propose a novel scene graph generation model for predicting object instances
and its corresponding relationships in an image. Our model, SG-CRF, learns the
sequential order of subject and object in a relationship triplet, and the
semantic compatibility of object instance nodes and relationship nodes in a
scene graph efficiently. Experiments empirically show that SG-CRF outperforms
the state-of-the-art methods, on three different datasets, i.e., CLEVR, VRD,
and Visual Genome, raising the Recall@100 from 24.99% to 49.95%, from 41.92% to
50.47%, and from 54.69% to 54.77%, respectively.