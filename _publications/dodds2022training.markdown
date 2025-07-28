---
layout: publication
title: Training And Challenging Models For Text-guided Fashion Image Retrieval
authors: Eric Dodds, Jack Culpepper, Gaurav Srivastava
conference: Arxiv
year: 2022
bibkey: dodds2022training
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.11004'}]
tags: ["Image Retrieval"]
short_authors: Eric Dodds, Jack Culpepper, Gaurav Srivastava
---
Retrieving relevant images from a catalog based on a query image together
with a modifying caption is a challenging multimodal task that can particularly
benefit domains like apparel shopping, where fine details and subtle variations
may be best expressed through natural language. We introduce a new evaluation
dataset, Challenging Fashion Queries (CFQ), as well as a modeling approach that
achieves state-of-the-art performance on the existing Fashion IQ (FIQ) dataset.
CFQ complements existing benchmarks by including relative captions with
positive and negative labels of caption accuracy and conditional image
similarity, where others provided only positive labels with a combined meaning.
We demonstrate the importance of multimodal pretraining for the task and show
that domain-specific weak supervision based on attribute labels can augment
generic large-scale pretraining. While previous modality fusion mechanisms lose
the benefits of multimodal pretraining, we introduce a residual attention
fusion mechanism that improves performance. We release CFQ and our code to the
research community.