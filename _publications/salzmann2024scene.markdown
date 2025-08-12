---
layout: publication
title: 'Scene-graph Vit: End-to-end Open-vocabulary Visual Relationship Detection'
authors: Tim Salzmann, Markus Ryll, Alex Bewley, Matthias Minderer
conference: Arxiv
year: 2024
bibkey: salzmann2024scene
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.14270'}]
tags: []
short_authors: Salzmann et al.
---
Visual relationship detection aims to identify objects and their
relationships in images. Prior methods approach this task by adding separate
relationship modules or decoders to existing object detection architectures.
This separation increases complexity and hinders end-to-end training, which
limits performance. We propose a simple and highly efficient decoder-free
architecture for open-vocabulary visual relationship detection. Our model
consists of a Transformer-based image encoder that represents objects as tokens
and models their relationships implicitly. To extract relationship information,
we introduce an attention mechanism that selects object pairs likely to form a
relationship. We provide a single-stage recipe to train this model on a mixture
of object and relationship detection data. Our approach achieves
state-of-the-art relationship detection performance on Visual Genome and on the
large-vocabulary GQA benchmark at real-time inference speeds. We provide
ablations, real-world qualitative examples, and analyses of zero-shot
performance.