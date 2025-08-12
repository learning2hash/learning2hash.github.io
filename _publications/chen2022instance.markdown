---
layout: publication
title: Instance Segmentation Of Dense And Overlapping Objects Via Layering
authors: Long Chen, Yuli Wu, Dorit Merhof
conference: Arxiv
year: 2022
bibkey: chen2022instance
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.03551'}]
tags: []
short_authors: Long Chen, Yuli Wu, Dorit Merhof
---
Instance segmentation aims to delineate each individual object of interest in
an image. State-of-the-art approaches achieve this goal by either partitioning
semantic segmentations or refining coarse representations of detected objects.
In this work, we propose a novel approach to solve the problem via object
layering, i.e. by distributing crowded, even overlapping objects into different
layers. By grouping spatially separated objects in the same layer, instances
can be effortlessly isolated by extracting connected components in each layer.
In comparison to previous methods, our approach is not affected by complex
object shapes or object overlaps. With minimal post-processing, our method
yields very competitive results on a diverse line of datasets: C. elegans
(BBBC), Overlapping Cervical Cells (OCC) and cultured neuroblastoma cells
(CCDB). The source code is publicly available.