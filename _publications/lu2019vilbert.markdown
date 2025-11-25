---
layout: publication
title: 'Vilbert: Pretraining Task-agnostic Visiolinguistic Representations For Vision-and-language
  Tasks'
authors: Jiasen Lu, Dhruv Batra, Devi Parikh, Stefan Lee
conference: Arxiv
year: 2019
bibkey: lu2019vilbert
citations: 1672
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.02265'}]
tags: ["Datasets", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Lu et al.
---
We present ViLBERT (short for Vision-and-Language BERT), a model for learning
task-agnostic joint representations of image content and natural language. We
extend the popular BERT architecture to a multi-modal two-stream model,
pro-cessing both visual and textual inputs in separate streams that interact
through co-attentional transformer layers. We pretrain our model through two
proxy tasks on the large, automatically collected Conceptual Captions dataset
and then transfer it to multiple established vision-and-language tasks --
visual question answering, visual commonsense reasoning, referring expressions,
and caption-based image retrieval -- by making only minor additions to the base
architecture. We observe significant improvements across tasks compared to
existing task-specific models -- achieving state-of-the-art on all four tasks.
Our work represents a shift away from learning groundings between vision and
language only as part of task training and towards treating visual grounding as
a pretrainable and transferable capability.