---
layout: publication
title: Bridging The Gap Between Object Detection And User Intent Via Query-modulation
authors: Marco Fornoni, Chaochao Yan, Liangchen Luo, Kimberly Wilber, Alex Stark,
  Yin Cui, Boqing Gong, Andrew Howard
conference: Arxiv
year: 2021
bibkey: fornoni2021bridging
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.10258'}]
tags: [Evaluation, Image Retrieval, Scalability]
short_authors: Fornoni et al.
---
When interacting with objects through cameras, or pictures, users often have
a specific intent. For example, they may want to perform a visual search. With
most object detection models relying on image pixels as their sole input,
undesired results are not uncommon. Most typically: lack of a high-confidence
detection on the object of interest, or detection with a wrong class label. The
issue is especially severe when operating capacity-constrained mobile object
detectors on-device. In this paper we investigate techniques to modulate mobile
detectors to explicitly account for the user intent, expressed as an embedding
of a simple query. Compared to standard detectors, query-modulated detectors
show superior performance at detecting objects for a given user query. Thanks
to large-scale training data synthesized from standard object detection
annotations, query-modulated detectors also outperform a specialized referring
expression recognition system. Query-modulated detectors can also be trained to
simultaneously solve for both localizing a user query and standard detection,
even outperforming standard mobile detectors at the canonical COCO task.