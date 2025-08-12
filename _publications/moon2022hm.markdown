---
layout: publication
title: 'HM: Hybrid Masking For Few-shot Segmentation'
authors: Seonghyeon Moon, Samuel S. Sohn, Honglu Zhou, Sejong Yoon, Vladimir Pavlovic,
  Muhammad Haris Khan, Mubbasir Kapadia
conference: Lecture Notes in Computer Science
year: 2022
bibkey: moon2022hm
citations: 8
additional_links: [{name: Code, url: 'https://github.com/moonsh/HM-Hybrid-Masking'},
  {name: Paper, url: 'https://arxiv.org/abs/2203.12826'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Moon et al.
---
We study few-shot semantic segmentation that aims to segment a target object
from a query image when provided with a few annotated support images of the
target class. Several recent methods resort to a feature masking (FM) technique
to discard irrelevant feature activations which eventually facilitates the
reliable prediction of segmentation mask. A fundamental limitation of FM is the
inability to preserve the fine-grained spatial details that affect the accuracy
of segmentation mask, especially for small target objects. In this paper, we
develop a simple, effective, and efficient approach to enhance feature masking
(FM). We dub the enhanced FM as hybrid masking (HM). Specifically, we
compensate for the loss of fine-grained spatial details in FM technique by
investigating and leveraging a complementary basic input masking method.
Experiments have been conducted on three publicly available benchmarks with
strong few-shot segmentation (FSS) baselines. We empirically show improved
performance against the current state-of-the-art methods by visible margins
across different benchmarks. Our code and trained models are available at:
https://github.com/moonsh/HM-Hybrid-Masking