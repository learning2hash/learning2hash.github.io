---
layout: publication
title: Organizing Unstructured Image Collections Using Natural Language
authors: Mingxuan Liu, Zhun Zhong, Jun Li, Gianni Franchi, Subhankar Roy, Elisa Ricci
conference: Arxiv
year: 2024
bibkey: liu2024organizing
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.05217'}]
tags: []
short_authors: Liu et al.
---
Organizing unstructured image collections into semantic clusters is a long-standing challenge. Traditional deep clustering techniques address this by producing a single data partition, whereas multiple clustering methods uncover diverse alternative partitions-but only when users predefine the clustering criteria. Yet expecting users to specify such criteria a priori for large, unfamiliar datasets is unrealistic. In this work, we introduce the task of Open-ended Semantic Multiple Clustering (OpenSMC), which aims to automatically discover clustering criteria from large, unstructured image collections, revealing interpretable substructures without human input. Our framework, X-Cluster: eXploratory Clustering, treats text as a reasoning proxy: it concurrently scans the entire image collection, proposes candidate criteria in natural language, and groups images into meaningful clusters per criterion. To evaluate progress, we release COCO-4c and Food-4c benchmarks, each annotated with four grouping criteria. Experiments show that X-Cluster effectively reveals meaningful partitions and enables downstream applications such as bias discovery and social media image popularity analysis. We will open-source code and data to encourage reproducibility and further research.