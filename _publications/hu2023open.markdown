---
layout: publication
title: 'Open-domain Visual Entity Recognition: Towards Recognizing Millions Of Wikipedia
  Entities'
authors: Hexiang Hu, Yi Luan, Yang Chen, Urvashi Khandelwal, Mandar Joshi, Kenton
  Lee, Kristina Toutanova, Ming-Wei Chang
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: hu2023open
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.11154'}]
tags: ["Datasets", "Evaluation", "ICCV", "Scalability"]
short_authors: Hu et al.
---
Large-scale multi-modal pre-training models such as CLIP and PaLI exhibit
strong generalization on various visual domains and tasks. However, existing
image classification benchmarks often evaluate recognition on a specific domain
(e.g., outdoor images) or a specific task (e.g., classifying plant species),
which falls short of evaluating whether pre-trained foundational models are
universal visual recognizers. To address this, we formally present the task of
Open-domain Visual Entity recognitioN (OVEN), where a model need to link an
image onto a Wikipedia entity with respect to a text query. We construct
OVEN-Wiki by re-purposing 14 existing datasets with all labels grounded onto
one single label space: Wikipedia entities. OVEN challenges models to select
among six million possible Wikipedia entities, making it a general visual
recognition benchmark with the largest number of labels. Our study on
state-of-the-art pre-trained models reveals large headroom in generalizing to
the massive-scale label space. We show that a PaLI-based auto-regressive visual
recognition model performs surprisingly well, even on Wikipedia entities that
have never been seen during fine-tuning. We also find existing pretrained
models yield different strengths: while PaLI-based models obtain higher overall
performance, CLIP-based models are better at recognizing tail entities.