---
layout: publication
title: Image Semantic Relation Generation
authors: Mingzhe Du
conference: Arxiv
year: 2022
bibkey: du2022image
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.11253'}]
tags: ["Image Retrieval"]
short_authors: Mingzhe Du
---
Scene graphs provide structured semantic understanding beyond images. For
downstream tasks, such as image retrieval, visual question answering, visual
relationship detection, and even autonomous vehicle technology, scene graphs
can not only distil complex image information but also correct the bias of
visual models using semantic-level relations, which has broad application
prospects. However, the heavy labour cost of constructing graph annotations may
hinder the application of PSG in practical scenarios. Inspired by the
observation that people usually identify the subject and object first and then
determine the relationship between them, we proposed to decouple the scene
graphs generation task into two sub-tasks: 1) an image segmentation task to
pick up the qualified objects. 2) a restricted auto-regressive text generation
task to generate the relation between given objects. Therefore, in this work,
we introduce image semantic relation generation (ISRG), a simple but effective
image-to-text model, which achieved 31 points on the OpenPSG dataset and
outperforms strong baselines respectively by 16 points (ResNet-50) and 5 points
(CLIP).