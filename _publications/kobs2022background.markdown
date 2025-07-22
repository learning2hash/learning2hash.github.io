---
layout: publication
title: On Background Bias In Deep Metric Learning
authors: Kobs Konstantin, Hotho Andreas
conference: Fifteenth International Conference on Machine Vision (ICMV 2022)
year: 2023
bibkey: kobs2022background
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.01615'}]
tags: ["Evaluation", "Distance-Metric-Learning", "Datasets"]
short_authors: Kobs Konstantin, Hotho Andreas
---
Deep Metric Learning trains a neural network to map input images to a
lower-dimensional embedding space such that similar images are closer together
than dissimilar images. When used for item retrieval, a query image is embedded
using the trained model and the closest items from a database storing their
respective embeddings are returned as the most similar items for the query.
Especially in product retrieval, where a user searches for a certain product by
taking a photo of it, the image background is usually not important and thus
should not influence the embedding process. Ideally, the retrieval process
always returns fitting items for the photographed object, regardless of the
environment the photo was taken in. In this paper, we analyze the influence of
the image background on Deep Metric Learning models by utilizing five common
loss functions and three common datasets. We find that Deep Metric Learning
networks are prone to so-called background bias, which can lead to a severe
decrease in retrieval performance when changing the image background during
inference. We also show that replacing the background of images during training
with random background images alleviates this issue. Since we use an automatic
background removal method to do this background replacement, no additional
manual labeling work and model changes are required while inference time stays
the same. Qualitative and quantitative analyses, for which we introduce a new
evaluation metric, confirm that models trained with replaced backgrounds attend
more to the main object in the image, benefitting item retrieval systems.