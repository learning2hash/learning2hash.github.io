---
layout: publication
title: Self-supervised Vision Transformers For Writer Retrieval
authors: Tim Raven, Arthur Matei, Gernot A. Fink
conference: Lecture Notes in Computer Science
year: 2024
bibkey: raven2024self
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.00751'}]
tags: ["Datasets", "Evaluation", "Self-Supervised", "Supervised"]
short_authors: Tim Raven, Arthur Matei, Gernot A. Fink
---
While methods based on Vision Transformers (ViT) have achieved
state-of-the-art performance in many domains, they have not yet been applied
successfully in the domain of writer retrieval. The field is dominated by
methods using handcrafted features or features extracted from Convolutional
Neural Networks. In this work, we bridge this gap and present a novel method
that extracts features from a ViT and aggregates them using VLAD encoding. The
model is trained in a self-supervised fashion without any need for labels. We
show that extracting local foreground features is superior to using the ViT's
class token in the context of writer retrieval. We evaluate our method on two
historical document collections. We set a new state-at-of-art performance on
the Historical-WI dataset (83.1% mAP), and the HisIR19 dataset (95.0% mAP).
Additionally, we demonstrate that our ViT feature extractor can be directly
applied to modern datasets such as the CVL database (98.6% mAP) without any
fine-tuning.