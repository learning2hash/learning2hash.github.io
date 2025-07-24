---
layout: publication
title: 'Retailklip : Finetuning Openclip Backbone Using Metric Learning On A Single
  GPU For Zero-shot Retail Product Image Classification'
authors: Muktabh Mayank Srivastava
conference: Proceedings of the 19th International Joint Conference on Computer Vision,
  Imaging and Computer Graphics Theory and Applications
year: 2024
bibkey: srivastava2024retailklip
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.10282'}]
tags: ["Distance Metric Learning", "Evaluation", "Few Shot & Zero Shot"]
short_authors: Muktabh Mayank Srivastava
---
Retail product or packaged grocery goods images need to classified in various
computer vision applications like self checkout stores, supply chain automation
and retail execution evaluation. Previous works explore ways to finetune deep
models for this purpose. But because of the fact that finetuning a large model
or even linear layer for a pretrained backbone requires to run at least a few
epochs of gradient descent for every new retail product added in classification
range, frequent retrainings are needed in a real world scenario. In this work,
we propose finetuning the vision encoder of a CLIP model in a way that its
embeddings can be easily used for nearest neighbor based classification, while
also getting accuracy close to or exceeding full finetuning. A nearest neighbor
based classifier needs no incremental training for new products, thus saving
resources and wait time.