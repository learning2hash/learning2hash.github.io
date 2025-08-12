---
layout: publication
title: Fine-grained Classification For Poisonous Fungi Identification With Transfer
  Learning
authors: Christopher Chiu, Maximilian Heil, Teresa Kim, Anthony Miyaguchi
conference: Arxiv
year: 2024
bibkey: chiu2024fine
citations: 0
additional_links: [{name: Code, url: 'https://github.com/dsgt-kaggle-clef/fungiclef-2024'},
  {name: Paper, url: 'https://arxiv.org/abs/2407.07492'}]
tags: ["Supervised"]
short_authors: Chiu et al.
---
FungiCLEF 2024 addresses the fine-grained visual categorization (FGVC) of
fungi species, with a focus on identifying poisonous species. This task is
challenging due to the size and class imbalance of the dataset, subtle
inter-class variations, and significant intra-class variability amongst
samples. In this paper, we document our approach in tackling this challenge
through the use of ensemble classifier heads on pre-computed image embeddings.
Our team (DS@GT) demonstrate that state-of-the-art self-supervised vision
models can be utilized as robust feature extractors for downstream application
of computer vision tasks without the need for task-specific fine-tuning on the
vision backbone. Our approach achieved the best Track 3 score (0.345), accuracy
(78.4%) and macro-F1 (0.577) on the private test set in post competition
evaluation. Our code is available at
https://github.com/dsgt-kaggle-clef/fungiclef-2024.