---
layout: publication
title: 'Focallens: Instruction Tuning Enables Zero-shot Conditional Image Representations'
authors: Cheng-Yu Hsieh, Pavan Kumar Anasosalu Vasu, Fartash Faghri, Raviteja Vemulapalli,
  Chun-Liang Li, Ranjay Krishna, Oncel Tuzel, Hadi Pouransari
conference: Arxiv
year: 2025
bibkey: hsieh2025focallens
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.08368'}]
tags: ["Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Hsieh et al.
---
Visual understanding is inherently contextual -- what we focus on in an image
depends on the task at hand. For instance, given an image of a person holding a
bouquet of flowers, we may focus on either the person such as their clothing,
or the type of flowers, depending on the context of interest. Yet, most
existing image encoding paradigms represent an image as a fixed, generic
feature vector, overlooking the potential needs of prioritizing varying visual
information for different downstream use cases. In this work, we introduce
FocalLens, a conditional visual encoding method that produces different
representations for the same image based on the context of interest, expressed
flexibly through natural language. We leverage vision instruction tuning data
and contrastively finetune a pretrained vision encoder to take natural language
instructions as additional inputs for producing conditional image
representations. Extensive experiments validate that conditional image
representation from FocalLens better pronounce the visual features of interest
compared to generic features produced by standard vision encoders like CLIP. In
addition, we show FocalLens further leads to performance improvements on a
range of downstream tasks including image-image retrieval, image
classification, and image-text retrieval, with an average gain of 5 and 10
points on the challenging SugarCrepe and MMVP-VLM benchmarks, respectively.