---
layout: publication
title: 'CLIP The Landscape: Automated Tagging Of Crowdsourced Landscape Images'
authors: Ilya Ilyankou, Natchapon Jongwiriyanurak, Tao Cheng, James Haworth
conference: Arxiv
year: 2025
bibkey: ilyankou2025clip
citations: 0
additional_links: [{name: Code, url: 'https://github.com/SpaceTimeLab/ClipTheLandscape\'},
  {name: Other, url: 'https://www.kaggle.com/competitions/predict-geographic-context-from-landscape-photos\'},
  {name: Paper, url: 'https://arxiv.org/abs/2506.12214'}]
tags: ["Datasets", "Evaluation", "Multimodal Retrieval"]
short_authors: Ilyankou et al.
---
We present a CLIP-based, multi-modal, multi-label classifier for predicting geographical context tags from landscape photos in the Geograph dataset--a crowdsourced image archive spanning the British Isles, including remote regions lacking POIs and street-level imagery. Our approach addresses a Kaggle competition\footnote\{https://www.kaggle.com/competitions/predict-geographic-context-from-landscape-photos\} task based on a subset of Geograph's 8M images, with strict evaluation: exact match accuracy is required across 49 possible tags. We show that combining location and title embeddings with image features improves accuracy over using image embeddings alone. We release a lightweight pipeline\footnote\{https://github.com/SpaceTimeLab/ClipTheLandscape\} that trains on a modest laptop, using pre-trained CLIP image and text embeddings and a simple classification head. Predicted tags can support downstream tasks such as building location embedders for GeoAI applications, enriching spatial understanding in data-sparse regions.