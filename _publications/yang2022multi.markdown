---
layout: publication
title: A Multi-person Video Dataset Annotation Method Of Spatio-temporally Actions
authors: Fan Yang
conference: Arxiv
year: 2022
bibkey: yang2022multi
citations: 1
additional_links: [{name: Code, url: 'https://github.com/Whiffe/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset'},
  {name: Paper, url: 'https://arxiv.org/abs/2204.10160'}]
tags: ["Datasets"]
short_authors: Fan Yang
---
Spatio-temporal action detection is an important and challenging problem in
video understanding. However, the application of the existing large-scale
spatio-temporal action datasets in specific fields is limited, and there is
currently no public tool for making spatio-temporal action datasets, it takes a
lot of time and effort for researchers to customize the spatio-temporal action
datasets, so we propose a multi-Person video dataset Annotation Method of
spatio-temporally actions.First, we use ffmpeg to crop the videos and frame the
videos; then use yolov5 to detect human in the video frame, and then use deep
sort to detect the ID of the human in the video frame. By processing the
detection results of yolov5 and deep sort, we can get the annotation file of
the spatio-temporal action dataset to complete the work of customizing the
spatio-temporal action dataset.
https://github.com/Whiffe/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset