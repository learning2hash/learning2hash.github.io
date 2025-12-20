---
layout: publication
title: 'Img2loc: Revisiting Image Geolocalization Using Multi-modality Foundation
  Models And Image-based Retrieval-augmented Generation'
authors: Zhongliang Zhou, Jielu Zhang, Zihan Guan, Mengxuan Hu, Ni Lao, Lan Mu, Sheng
  Li, Gengchen Mai
conference: Proceedings of the 47th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2024
bibkey: zhou2024img2loc
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.19584'}]
tags: ["Datasets", "Evaluation", "SIGIR"]
short_authors: Zhou et al.
---
Geolocating precise locations from images presents a challenging problem in
computer vision and information retrieval.Traditional methods typically employ
either classification, which dividing the Earth surface into grid cells and
classifying images accordingly, or retrieval, which identifying locations by
matching images with a database of image-location pairs. However,
classification-based approaches are limited by the cell size and cannot yield
precise predictions, while retrieval-based systems usually suffer from poor
search quality and inadequate coverage of the global landscape at varied scale
and aggregation levels. To overcome these drawbacks, we present Img2Loc, a
novel system that redefines image geolocalization as a text generation task.
This is achieved using cutting-edge large multi-modality models like GPT4V or
LLaVA with retrieval augmented generation. Img2Loc first employs CLIP-based
representations to generate an image-based coordinate query database. It then
uniquely combines query results with images itself, forming elaborate prompts
customized for LMMs. When tested on benchmark datasets such as Im2GPS3k and
YFCC4k, Img2Loc not only surpasses the performance of previous state-of-the-art
models but does so without any model training.