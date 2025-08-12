---
layout: publication
title: 'Benchmarking A Benchmark: How Reliable Is MS-COCO?'
authors: Eric Zimmermann, Justin Szeto, Jerome Pasquero, Frederic Ratle
conference: Arxiv
year: 2023
bibkey: zimmermann2023benchmarking
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.02709'}]
tags: ["Datasets", "Evaluation"]
short_authors: Zimmermann et al.
---
Benchmark datasets are used to profile and compare algorithms across a
variety of tasks, ranging from image classification to segmentation, and also
play a large role in image pretraining algorithms. Emphasis is placed on
results with little regard to the actual content within the dataset. It is
important to question what kind of information is being learned from these
datasets and what are the nuances and biases within them. In the following
work, Sama-COCO, a re-annotation of MS-COCO, is used to discover potential
biases by leveraging a shape analysis pipeline. A model is trained and
evaluated on both datasets to examine the impact of different annotation
conditions. Results demonstrate that annotation styles are important and that
annotation pipelines should closely consider the task of interest. The dataset
is made publicly available at https://www.sama.com/sama-coco-dataset/ .