---
layout: publication
title: A Semi-supervised Deep Learning Approach To Dataset Collection For Query-by-humming
  Task
authors: Amantur Amatov, Dmitry Lamanov, Maksim Titov, Ivan Vovk, Ilya Makarov, Mikhail
  Kudinov
conference: Arxiv
year: 2023
bibkey: amatov2023semi
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.01092'}]
tags: ["Datasets"]
short_authors: Amatov et al.
---
Query-by-Humming (QbH) is a task that involves finding the most relevant song
based on a hummed or sung fragment. Despite recent successful commercial
solutions, implementing QbH systems remains challenging due to the lack of
high-quality datasets for training machine learning models. In this paper, we
propose a deep learning data collection technique and introduce Covers and
Hummings Aligned Dataset (CHAD), a novel dataset that contains 18 hours of
short music fragments, paired with time-aligned hummed versions. To expand our
dataset, we employ a semi-supervised model training pipeline that leverages the
QbH task as a specialized case of cover song identification (CSI) task.
Starting with a model trained on the initial dataset, we iteratively collect
groups of fragments of cover versions of the same song and retrain the model on
the extended data. Using this pipeline, we collect over 308 hours of additional
music fragments, paired with time-aligned cover versions. The final model is
successfully applied to the QbH task and achieves competitive results on
benchmark datasets. Our study shows that the proposed dataset and training
pipeline can effectively facilitate the implementation of QbH systems.