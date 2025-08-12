---
layout: publication
title: 'Semmeldetector: Application Of Machine Learning In Commercial Bakeries'
authors: Thomas H. Schmitt, Maximilian Bundscherer, Tobias Bocklet
conference: 2023 International Conference on Machine Learning and Applications (ICMLA)
year: 2023
bibkey: schmitt2023semmeldetector
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.04050'}]
tags: ["Efficiency", "ICML"]
short_authors: Thomas H. Schmitt, Maximilian Bundscherer, Tobias Bocklet
---
The Semmeldetector, is a machine learning application that utilizes object
detection models to detect, classify and count baked goods in images. Our
application allows commercial bakers to track unsold baked goods, which allows
them to optimize production and increase resource efficiency. We compiled a
dataset comprising 1151 images that distinguishes between 18 different types of
baked goods to train our detection models. To facilitate model training, we
used a Copy-Paste augmentation pipeline to expand our dataset. We trained the
state-of-the-art object detection model YOLOv8 on our detection task. We tested
the impact of different training data, model scale, and online image
augmentation pipelines on model performance. Our overall best performing model,
achieved an AP@0.5 of 89.1% on our test set. Based on our results, we conclude
that machine learning can be a valuable tool even for unforeseen industries
like bakeries, even with very limited datasets.