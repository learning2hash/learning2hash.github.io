---
layout: publication
title: 'Scene-centric Vs. Object-centric Image-text Cross-modal Retrieval: A Reproducibility
  Study'
authors: Mariya Hendriksen, Svitlana Vakulenko, Ernst Kuiper, Maarten de Rijke
conference: Lecture Notes in Computer Science
year: 2023
bibkey: hendriksen2023scene
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.05174'}]
tags: [Evaluation, Datasets, Multimodal Retrieval]
short_authors: Hendriksen et al.
---
Most approaches to cross-modal retrieval (CMR) focus either on object-centric
datasets, meaning that each document depicts or describes a single object, or
on scene-centric datasets, meaning that each image depicts or describes a
complex scene that involves multiple objects and relations between them. We
posit that a robust CMR model should generalize well across both dataset types.
Despite recent advances in CMR, the reproducibility of the results and their
generalizability across different dataset types has not been studied before. We
address this gap and focus on the reproducibility of the state-of-the-art CMR
results when evaluated on object-centric and scene-centric datasets. We select
two state-of-the-art CMR models with different architectures: (i) CLIP; and
(ii) X-VLM. Additionally, we select two scene-centric datasets, and three
object-centric datasets, and determine the relative performance of the selected
models on these datasets. We focus on reproducibility, replicability, and
generalizability of the outcomes of previously published CMR experiments. We
discover that the experiments are not fully reproducible and replicable.
Besides, the relative performance results partially generalize across
object-centric and scene-centric datasets. On top of that, the scores obtained
on object-centric datasets are much lower than the scores obtained on
scene-centric datasets. For reproducibility and transparency we make our source
code and the trained models publicly available.