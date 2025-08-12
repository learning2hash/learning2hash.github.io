---
layout: publication
title: Visual Re-ranking With Non-visual Side Information
authors: Gustav Hanning, Gabrielle Flood, Viktor Larsson
conference: Lecture Notes in Computer Science
year: 2025
bibkey: hanning2025visual
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.11134'}]
tags: ["Re-Ranking"]
short_authors: Gustav Hanning, Gabrielle Flood, Viktor Larsson
---
The standard approach for visual place recognition is to use global image descriptors to retrieve the most similar database images for a given query image. The results can then be further improved with re-ranking methods that re-order the top scoring images. However, existing methods focus on re-ranking based on the same image descriptors that were used for the initial retrieval, which we argue provides limited additional signal. In this work we propose Generalized Contextual Similarity Aggregation (GCSA), which is a graph neural network-based re-ranking method that, in addition to the visual descriptors, can leverage other types of available side information. This can for example be other sensor data (such as signal strength of nearby WiFi or BlueTooth endpoints) or geometric properties such as camera poses for database images. In many applications this information is already present or can be acquired with low effort. Our architecture leverages the concept of affinity vectors to allow for a shared encoding of the heterogeneous multi-modal input. Two large-scale datasets, covering both outdoor and indoor localization scenarios, are utilized for training and evaluation. In experiments we show significant improvement not only on image retrieval metrics, but also for the downstream visual localization task.