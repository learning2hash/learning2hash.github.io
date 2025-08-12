---
layout: publication
title: Leveraging Contrastive Learning For Few-shot Geolocation Of Social Posts
authors: Menglin Li, Kwan Hui Lim
conference: Arxiv
year: 2024
bibkey: li2024leveraging
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.00786'}]
tags: ["Few Shot & Zero Shot", "Self-Supervised"]
short_authors: Menglin Li, Kwan Hui Lim
---
Social geolocation is an important problem of predicting the originating
locations of social media posts. However, this task is challenging due to the
need for a substantial volume of training data, alongside well-annotated
labels. These issues are further exacerbated by new or less popular locations
with insufficient labels, further leading to an imbalanced dataset. In this
paper, we propose \textbf\{ContrastGeo\}, a \textbf\{Contrast\}ive learning
enhanced framework for few-shot social \textbf\{Geo\}location. Specifically, a
Tweet-Location Contrastive learning objective is introduced to align
representations of tweets and locations within tweet-location pairs. To capture
the correlations between tweets and locations, a Tweet-Location Matching
objective is further adopted into the framework and refined via an online hard
negative mining approach. We also develop three fusion strategies with various
fusion encoders to better generate joint representations of tweets and
locations. Comprehensive experiments on three social media datasets highlight
ContrastGeo's superior performance over several state-of-the-art baselines in
few-shot social geolocation.