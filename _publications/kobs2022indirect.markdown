---
layout: publication
title: 'Indirect: Language-guided Zero-shot Deep Metric Learning For Images'
authors: Konstantin Kobs, Michael Steininger, Andreas Hotho
conference: 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2023
bibkey: kobs2022indirect
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.12760'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Few Shot & Zero Shot", "Image Retrieval", "Supervised"]
short_authors: Konstantin Kobs, Michael Steininger, Andreas Hotho
---
Common Deep Metric Learning (DML) datasets specify only one notion of
similarity, e.g., two images in the Cars196 dataset are deemed similar if they
show the same car model. We argue that depending on the application, users of
image retrieval systems have different and changing similarity notions that
should be incorporated as easily as possible. Therefore, we present
Language-Guided Zero-Shot Deep Metric Learning (LanZ-DML) as a new DML setting
in which users control the properties that should be important for image
representations without training data by only using natural language. To this
end, we propose InDiReCT (Image representations using Dimensionality Reduction
on CLIP embedded Texts), a model for LanZ-DML on images that exclusively uses a
few text prompts for training. InDiReCT utilizes CLIP as a fixed feature
extractor for images and texts and transfers the variation in text prompt
embeddings to the image embedding space. Extensive experiments on five datasets
and overall thirteen similarity notions show that, despite not seeing any
images during training, InDiReCT performs better than strong baselines and
approaches the performance of fully-supervised models. An analysis reveals that
InDiReCT learns to focus on regions of the image that correlate with the
desired similarity notion, which makes it a fast to train and easy to use
method to create custom embedding spaces only using natural language.