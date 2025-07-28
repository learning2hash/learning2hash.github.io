---
layout: publication
title: Learning Audio-video Modalities From Image Captions
authors: Arsha Nagrani, Paul Hongsuck Seo, Bryan Seybold, Anja Hauth, Santiago Manen,
  Chen Sun, Cordelia Schmid
conference: Lecture Notes in Computer Science
year: 2022
bibkey: nagrani2022learning
citations: 37
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.00679'}]
tags: []
short_authors: Nagrani et al.
---
A major challenge in text-video and text-audio retrieval is the lack of
large-scale training data. This is unlike image-captioning, where datasets are
in the order of millions of samples. To close this gap we propose a new video
mining pipeline which involves transferring captions from image captioning
datasets to video clips with no additional manual effort. Using this pipeline,
we create a new large-scale, weakly labelled audio-video captioning dataset
consisting of millions of paired clips and captions. We show that training a
multimodal transformed based model on this data achieves competitive
performance on video retrieval and video captioning, matching or even
outperforming HowTo100M pretraining with 20x fewer clips. We also show that our
mined clips are suitable for text-audio pretraining, and achieve state of the
art results for the task of audio retrieval.