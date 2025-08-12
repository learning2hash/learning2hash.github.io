---
layout: publication
title: Multi-label Plant Species Classification With Self-supervised Vision Transformers
authors: Murilo Gustineli, Anthony Miyaguchi, Ian Stalter
conference: Arxiv
year: 2024
bibkey: gustineli2024multi
citations: 0
additional_links: [{name: Code, url: 'https://github.com/dsgt-kaggle-clef/plantclef-2024'},
  {name: Paper, url: 'https://arxiv.org/abs/2407.06298'}]
tags: ["Self-Supervised"]
short_authors: Murilo Gustineli, Anthony Miyaguchi, Ian Stalter
---
We present a transfer learning approach using a self-supervised Vision
Transformer (DINOv2) for the PlantCLEF 2024 competition, focusing on the
multi-label plant species classification. Our method leverages both base and
fine-tuned DINOv2 models to extract generalized feature embeddings. We train
classifiers to predict multiple plant species within a single image using these
rich embeddings. To address the computational challenges of the large-scale
dataset, we employ Spark for distributed data processing, ensuring efficient
memory management and processing across a cluster of workers. Our data
processing pipeline transforms images into grids of tiles, classifying each
tile, and aggregating these predictions into a consolidated set of
probabilities. Our results demonstrate the efficacy of combining transfer
learning with advanced data processing techniques for multi-label image
classification tasks. Our code is available at
https://github.com/dsgt-kaggle-clef/plantclef-2024.